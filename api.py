import ray
from fastapi import FastAPI
from ray import serve

app = FastAPI()

@serve.deployment
@serve.ingress(app)
class App2Deployment:
    @app.get("/")
    def root(self):
        return "Hello, App2!"

app2_test = App2Deployment.bind()
