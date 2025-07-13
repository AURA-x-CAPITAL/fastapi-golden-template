# Application Requirements and Setup

## Configuration Management

### Environment Variables
A `.env.template` file is included with all required variables:

To use:
```bash
cp .env.template .env
# Edit .env with your values
```

### Runtime Configuration
Configuration is loaded from environment variables using Pydantic:

```python
# src/app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # All environment variables defined here
    ...

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

## Dependency Management with UV

We use [uv](https://github.com/astral-sh/uv) for fast, reliable dependency management. Dependencies are split into:

1. **Base dependencies** (common to all environments)
2. **Development dependencies**
3. **Production dependencies**

Docs [uv](https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers)

### UV Commands

# TODO:
**Install all (dev + prod) dependencies:**
```bash
uv sync
# OR
uv sync --group dev
# OR
uv sync --all-groups
```

**Install production:**
```bash
uv sync --no-dev
```

## Health Check Endpoint

A health check endpoint is available at `/health`.
File: [src/app/api/routes/utils.py](../src/app/api/routes/utils.py)

## Pre-start Initialization

The `backend_pre_start.py` script ensures the application is ready before starting:

> You can define this startup and shutdown logic using the lifespan parameter of the FastAPI app, and a "context manager" (I'll show you what that is in a second).

Read more: [backend/README.md](https://fastapi.tiangolo.com/advanced/events/#use-case)


## Graceful Shutdown

Proper shutdown handling ensures all resources are released: [src/app/shutdown.py](../src/app/shutdown.py)

> You can define this startup and shutdown logic using the lifespan parameter of the FastAPI app, and a "context manager" (I'll show you what that is in a second).

Read more: [backend/README.md](https://fastapi.tiangolo.com/advanced/events/#use-case)


## Kubernetes-Ready Logging

### Logging Configuration

[src/app/core/logging.py](../src/app/core/logging.py)
