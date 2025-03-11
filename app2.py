import ray
from ray import serve
from fastapi import FastAPI

app = FastAPI(title="App2 Service")

@app.get("/")
def read_root():
    return {"message": "Hello from App2!"}

@serve.deployment(route_prefix="/app2")
@serve.ingress(app)
class App2Deployment:
    pass

if __name__ == "__main__":
    ray.init()
    serve.start()
    App2Deployment.deploy()

    import signal
    signal.pause()
