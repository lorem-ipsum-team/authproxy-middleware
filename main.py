from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, health, forwardauth
import debug

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth.router)
app.include_router(health.router)
app.include_router(forwardauth.router)

debug.run_if_needed()
