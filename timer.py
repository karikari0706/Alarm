from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# ユーザーがアクセスしてきたら、Timer.html を返す（表示する）
@app.get("/")
def serve_timer():
    return FileResponse("Timer.html")
