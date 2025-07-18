# Docker

Use the docker for the cross-platform development and deployment.
On the same time you can use docker-compose for the local development and set-up all necessary dependencies on the local laptop.

All docker related files in the `docker` directory.

## Overview
Our Docker setup provides a complete development and production environment with:
- **FastAPI application** with hot-reload in development
- **PostgreSQL database** with persistent storage
- **Redis** for caching and queues
- **PgBouncer** for connection pooling
- **Database migrations** as a separate service

## File Structure
```
docker/
├── Dockerfile              # Production application image
├── docker-compose.yml      # Core service definitions
└── docker-compose.override.yml # Development enhancements
```

## Core Services (`docker-compose.yml`)

### 1. Backend Service

**Key Features:**
- Builds from project root using `docker/Dockerfile`
- Uses environment variables from `.env` file
- Health check endpoint at `/health`
- Waits for database readiness before starting
- Requires successful migrations before launch

### 2. Migrations Service

**Purpose:**
- Runs database migrations before application starts
- Uses same image as backend service
- Ensures database schema is up-to-date
- Only runs when Postgres is healthy

## Development Enhancements (`docker-compose.override.yml`)

### 1. PostgreSQL Database

**Features:**
- Alpine image for smaller footprint
- Persistent volume for data storage
- Health check with connection verification
- Custom port mapping (5433)
- Init scripts in `init-scripts/` run on first start

### 2. PgBouncer Connection Pooler

**Benefits:**
- Reduces database connection overhead
- Limits maximum connections to Postgres
- Improves application performance
- Transparent to application (uses standard port 5432)

### 3. Redis Service

**Configuration:**
- Disables disk persistence for better performance
- Password-protected instance
- Exposes standard Redis port

## Environment Variables
Create `.env` file with these essential variables:
```env
# Database
POSTGRES_USER=appuser
POSTGRES_PASSWORD=securepassword
POSTGRES_DB=appdb

# Redis
REDIS_PASSWORD=redispass

# Application
ENVIRONMENT=development
SECRET_KEY=change-me-in-production
```

## Usage Guide

### 1. Start Development Environment
```bash
# Build images and start containers
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.override.yml up -d --build

# Follow logs
docker-compose logs -f
```

### 2. Access Services
| Service  | URL                        | Port |
|----------|----------------------------|------|
| FastAPI  | http://localhost:8000      | 8000 |
| API Docs | http://localhost:8000/docs | 8000 |
| Postgres | localhost                  | 5433 |
| Redis    | localhost                  | 6379 |

### 3. Common Operations
**Run migrations manually:**
```bash
docker-compose run migrations
```

**Access database:**
```bash
# Connect via PgBouncer (app uses this)
psql -h localhost -p 5432 -U appuser -d appdb

# Connect directly to Postgres
psql -h localhost -p 5433 -U appuser -d appdb
```

**Run tests:**
```bash
docker-compose exec backend pytest
```

**Stop environment:**
```bash
docker-compose down
```

### 4. Production Deployment
```bash
# Build production image
docker build -f docker/Dockerfile -t myapp:prod .

# Run with production settings
docker run -d --name myapp_prod \
  -p 8000:8000 \
  --env-file .env \
  -e ENVIRONMENT=production \
  myapp:prod
```

## Customization

### Development vs Production
| Setting            | Development | Production |
|--------------------|-------------|------------|
| Hot Reload         | Enabled     | Disabled   |
| Debug Mode         | On          | Off        |
| Log Level          | Debug       | Warn       |
| Worker Processes   | 1           | 4+         |
