### HttpUrl

from pydantic import BaseModel, HttpUrl


class Website(BaseModel):
    url: HttpUrl


# Корректный URL
site1 = Website(url="https://www.example.com/path?query=test#fragment")
print(f"\n--- Корректный HttpUrl ---")
print(f"URL: {site1.url}")
print(f"Scheme: {site1.url.scheme}")  # Доступ к компонентам URL
print(f"Host: {site1.url.host}")
print(f"Path: {site1.url.path}")

# URL без схемы - ошибка
# site2 = Website(url="www.example.com") # ValidationError

# Невалидный протокол - ошибка
# site3 = Website(url="ftp://example.com/file.zip")  # ValidationError

### AnyUrl

from pydantic import BaseModel, AnyUrl


class ResourceLocator(BaseModel):
    location: AnyUrl


# Корректные AnyUrl (разные схемы)
res1 = ResourceLocator(location="ftp://ftp.example.com/pub/data.txt")
res2 = ResourceLocator(location="mailto:user@example.com")
res3 = ResourceLocator(location="file:///home/user/document.pdf")
print(f"\n--- Корректные AnyUrl ---")
print(f"FTP: {res1.location}")
print(f"Mailto: {res2.location}")
print(f"File: {res3.location}")

# Некорректный формат URI - ошибка
# res_invalid = ResourceLocator(location="not_a_valid_url") # ValidationError

### EmailStr

from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    email: EmailStr
    name: str


# Корректный EmailStr
contact1 = Contact(name="Jane", email="jane.doe@example.com")
print(f"\n--- Корректный EmailStr ---")
print(contact1)

# Некорректный EmailStr (нет символа '@')
# contact_invalid1 = Contact(name="John", email="john.example.com") # ValidationError

# Некорректный EmailStr (нет домена)
# contact_invalid2 = Contact(name="Alice", email="alice@") # ValidationError
