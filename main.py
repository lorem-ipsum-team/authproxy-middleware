from fastapi import FastAPI
from routers import auth, health, forwardauth
import debug

app = FastAPI()

app.include_router(auth.router)
app.include_router(health.router)
app.include_router(forwardauth.router)

debug.run_if_needed()
