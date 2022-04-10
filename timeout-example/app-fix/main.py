from fastapi import FastAPI, BackgroundTasks
import time
# import requests

app = FastAPI()

@app.get("/normal")
def timeout_api():
    return {"msg": "normal"}

def demo_background():
    # 70초 sleep
    time.sleep(70)

    # callback
    # requests.get(host)

@app.get("/timeout")
def timeout_api(background_tasks: BackgroundTasks):
    background_tasks.add_task(demo_background)
    return {"msg": "timeout"}
