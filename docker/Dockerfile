# Builder stage
FROM python:3.11-slim as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=on

WORKDIR /app

# Install UV (ultra-fast installer)
RUN pip install uv==1.1.0
COPY requirements.txt .
RUN uv pip install -r requirements.txt --system

# ----- Production Stage -----
FROM gcr.io/distroless/python3-debian11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=PRODUCTION

WORKDIR /app

# Copy Python dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application
COPY . .

# Non-root user for security
USER 65534:65534  # distroless default non-root user

CMD ["app/main.py"]
