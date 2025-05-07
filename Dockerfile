FROM python:3.13-alpine
WORKDIR /app
RUN apk add curl uv

COPY pyproject.toml uv.lock ./
RUN uv venv -p 3.13
RUN source ./.venv/bin/activate
RUN uv sync --frozen

COPY . ./

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
