from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/normal")
def timeout_api():
    return {"msg": "normal"}

@app.get("/timeout")
def timeout_api():
    # 70초 sleep
    time.sleep(70)
    return {"msg": "timeout"}
