from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def get_welcome():
    return "message: Your health app is up and running!"

@app.post("/welcome")
def post_welcome():
    return "message: Your health app received a POST request!"
