from fastapi import FastAPI

app = FastAPI(title="Sarath Panguluri API Demo")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
