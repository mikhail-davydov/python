# Протокол дескрипторов

## Что такое дескриптор

Дескриптор — это любой объект, у которого определён хотя бы один из методов:
- `__get__()` — вызывается при **чтении** атрибута
- `__set__()` — вызывается при **записи** значения
- `__delete__()` — вызывается при **удалении** атрибута

Дескриптор всегда является **атрибутом класса**, а не экземпляра.

---

## Три вида доступа к атрибуту

```python
cat.name          # ПОЛУЧЕНИЕ  → вызывается __get__()
cat.name = 'X'    # ИЗМЕНЕНИЕ  → вызывается __set__()
del cat.name      # УДАЛЕНИЕ   → вызывается __delete__()
```

По умолчанию Python просто читает/пишет/удаляет запись в `obj.__dict__`.
Дескриптор **перехватывает** эти операции и позволяет добавить свою логику.

---

## Методы дескриптора и их параметры

```python
def __get__(self, obj, cls):
    # self — сам дескриптор
    # obj  — экземпляр класса (None если обращение через класс)
    # cls  — класс

def __set__(self, obj, value):
    # value — присваиваемое значение

def __delete__(self, obj):
    # только экземпляр, значение не нужно
```

---

## Почему внутри дескриптора обращаются к `obj.__dict__` напрямую

Если внутри `__get__` написать `return obj.name` — возникнет бесконечная рекурсия:
`obj.name` снова вызовет `__get__`, который снова вызовет `obj.name` и так до краша.

```python
def __get__(self, obj, cls):
    return obj.__dict__[self._attr]   # безопасно — минуем протокол дескрипторов
```

---

## Собственный дескриптор

```python
class NonEmptyString:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self                        # обращение через класс
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if isinstance(value, str) and len(value) > 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


class Cat:
    name = NonEmptyString()   # дескриптор — атрибут класса, не экземпляра

    def __init__(self, name):
        self.name = name      # вызывает __set__()
```

Дескриптор создаётся **один раз** при определении класса и разделяется всеми экземплярами.
Поэтому дескриптор **не хранит значения** — он хранит только имя атрибута,
по которому обращается к `obj.__dict__` каждого конкретного экземпляра.

---

## `__set_name__()`

До Python 3.6 имя атрибута приходилось передавать вручную:

```python
class Cat:
    name = NonEmptyString('name')   # дублирование
```

Начиная с Python 3.6, при создании класса Python **автоматически вызывает**
`__set_name__()` для каждого дескриптора, передавая класс и имя переменной:

```python
class NonEmptyString:
    def __set_name__(self, cls, attr):
        self._attr = attr   # attr == 'name' — Python передал сам

class Cat:
    name = NonEmptyString()   # __set_name__(Cat, 'name') вызовется автоматически
```

Параметр `cls` — класс в котором объявлен дескриптор. Используется редко,
но позволяет формировать информативные сообщения об ошибках:

```python
def __set_name__(self, cls, attr):
    self._attr = attr
    self._cls_name = cls.__name__

def __set__(self, obj, value):
    raise ValueError(f'[{self._cls_name}.{self._attr}] ожидается строка')
```

---

## Дескрипторы данных и не-данных

| Тип | Определённые методы | Приоритет |
|---|---|---|
| **Data descriptor** | `__get__` + `__set__` или `__delete__` | Выше `obj.__dict__` |
| **Non-data descriptor** | только `__get__` | Ниже `obj.__dict__` |

Если дескриптор данных и атрибут экземпляра имеют одинаковое имя — **дескриптор победит**.
Если дескриптор не-данных — победит атрибут из `obj.__dict__`.

> При создании read-only дескриптора рекомендуется явно определять `__set__()`,
> возбуждающий исключение — чтобы дескриптор стал дескриптором данных и имел нужный приоритет.

---

## Цепочка поиска атрибута (от высшего приоритета к низшему)

- Дескриптор данных из класса или родителей
- Атрибут из **dict** экземпляра
- Дескриптор не-данных из класса или родителей
- Атрибут из **dict** класса (не дескриптор)
- AttributeError
---

## Методы экземпляра — это дескрипторы

Обычная функция в Python является объектом, у которого определён `__get__()`.
То есть **любая функция — это дескриптор не-данных**.

Это объясняет механизм `self`: когда ты обращаешься к методу через экземпляр,
Python находит функцию в `Cat.__dict__`, видит что она дескриптор, и вызывает `__get__()`.

```python
cat.meow('громко')
 Python внутри делает:
 1. Cat.__dict__['meow'].__get__(cat, Cat)  → связанный метод (self уже вшит)
 2. ('громко')  → пользователь передаёт остальные   аргументы
 итого эквивалентно: Cat.meow(cat, 'громко')
```

Упрощённая реализация `__get__` у функции:

```python
def __get__(self, obj, objtype=None):
    if obj is None:
        return self                    обращение через класс → голая функция
    return types.MethodType(self, obj) обращение через экземпляр → вшить obj в self
```

Обращение через класс и через экземпляр:

```python
cat.meow('громко')   __get__(cat, Cat)  → self вшит, передаёшь только свои аргументы
Cat.meow(cat, 'громко')  __get__(None, Cat) → голая функция, экземпляр передаёшь вручную
```

---

## `@property` — встроенный дескриптор данных

`property` — это обычный класс с определёнными `__get__`, `__set__`, `__delete__`.
`@property` создаёт экземпляр этого класса и присваивает его атрибуту класса.

Главное преимущество собственного дескриптора перед `@property` —
возможность переиспользовать одну логику для нескольких атрибутов:

```python
class Cat:
    name    = NonEmptyString()   # одна логика
    surname = NonEmptyString()   # переиспользована без дублирования кода
```

Примерный код `property`:

```python
class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```

---

### Static and Class methods

```python
class StaticMethod(object):
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f
```

```python
class ClassMethod(object):
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc
```

---

## Когда использовать?

### Ленивые свойства

```python
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__   # запомнили имя функции

    def __get__(self, obj, type=None):
        obj.__dict__[self.name] = self.function(obj)  # записали результат в __dict__ экземпляра
        return obj.__dict__[self.name]
```

При **первом** обращении к `meaning_of_life`:

1. `__get__` вызывается — функция выполняется, ждём 3 сек
2. Результат записывается прямо в `obj.__dict__['meaning_of_life']`

При **втором** обращении:

1. Python ищет по цепочке поиска
2. Находит `meaning_of_life` в `obj.__dict__` — **раньше** чем доходит до дескриптора
3. `__get__` вообще не вызывается — возвращается закэшированное значение мгновенно

### DRY

	@property × 5 с одинаковой логикой  →  один класс-дескриптор × 5 использований

```python
# properties2.py
class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()

my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
```