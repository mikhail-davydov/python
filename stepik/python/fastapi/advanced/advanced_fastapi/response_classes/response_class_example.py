from fastapi import FastAPI, Response  # Импортируем базовый Response, т.к. XMLResponse нет из коробки
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse  # Другие классы ответов

app = FastAPI()


# --- Пример 1: Отдача чистого текста ---
@app.get("/hello-text", response_class=PlainTextResponse)
async def get_plain_text():
    # FastAPI использует PlainTextResponse, чтобы отдать эту строку как 'text/plain'
    return "Привет, мир! Это чистый текст."


# --- Пример 2: Отдача HTML-страницы ---
@app.get("/hello-html", response_class=HTMLResponse)
async def get_html_page():
    # FastAPI использует HTMLResponse, чтобы отдать эту строку как 'text/html'
    return """
    <html>
        <body>
            <h1>Это HTML-страница от FastAPI!</h1>
            <p>Указан response_class=HTMLResponse.</p>
        </body>
    </html>
    """


# --- Пример 3: Отдача XML (с использованием базового Response) ---
@app.get("/data.xml", response_class=Response)  # <--- Указываем response_class здесь
async def get_xml_data():
    content = "<root><message>Это XML-данные</message><source>FastAPI</source></root>"
    # Поскольку мы указали response_class=Response (базовый),
    # мы должны сами создать его экземпляр и задать media_type.
    return Response(content=content, media_type="application/xml")


# --- Пример 4: Явное использование JSONResponse (хотя это дефолт) ---
@app.get("/explicit-json", response_class=JSONResponse)  # <--- Указываем response_class здесь
async def get_explicit_json():
    # Даже если это JSON, явное указание позволяет добавить заголовки прямо здесь
    return JSONResponse(
        content={"status": "ok", "message": "Это явный JSON-ответ"},
        headers={"X-Debug-Info": "Enabled"}
    )
