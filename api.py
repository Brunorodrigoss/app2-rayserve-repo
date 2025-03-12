import ray
from fastapi import FastAPI
from ray import serve

app = FastAPI()

@serve.deployment(
    num_replicas=1,
    ray_actor_options={"num_cpus": 0.5, "num_gpus": 0}
)
@serve.ingress(app)
class App2Deployment:
    @app.get("/")
    def root(self):
        return "Hello, App2!"

app2_test = App2Deployment.bind()
