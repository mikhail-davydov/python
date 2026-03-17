from bs4 import BeautifulSoup

def extract_html_text(html_string: str) -> str:
    """
    Извлекает чистый текст из HTML-строки, игнорируя теги.

    Используем 'html.parser' из стандартной библиотеки,
    но BeautifulSoup гарантирует корректную обработку даже для сломанного HTML.
    """
    soup = BeautifulSoup(html_string, "html.parser")
    return soup.get_text()

if __name__ == "__main__":
    # Входные данные
    raw_html = '<span>/api<wbr>/v1<wbr>/assets<wbr>/external<wbr>/vehicle</span>'

    # Обработка
    result = extract_html_text(raw_html)

    # Вывод
    print(f"Результат: {result}")