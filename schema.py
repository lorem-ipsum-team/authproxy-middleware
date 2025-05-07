from pydantic import BaseModel


class Tokens(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    refresh_expires_in: int
    token_type: str
    session_state: str
    scope: str


class LoginRequest(BaseModel):
    username: str
    password: str
