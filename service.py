from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>My First Web Page</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>This is a simple web page served by Python.</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
