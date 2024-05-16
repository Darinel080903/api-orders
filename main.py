from fastapi import FastAPI
from infraestructure.web.rest.controller import routes
import uvicorn

app = FastAPI()

app.include_router(routes.controller)

if __name__ == "__main__":
    uvicorn.run(app, port=3001)
