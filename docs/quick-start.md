# Quick Start: Development Workflow

## Prerequisites
- Docker and Docker Compose installed
- Python 3.10+ (optional for local development)
- UV package manager (`pip install uv`)

## 1. Clone Repository
```bash
git clone https://github.com/AURA-x-CAPITAL/fastapi-golden-template.git
cd fastapi-golden-template
```

## 2. Setup Environment
```bash
# Copy environment template
cp src/.env.template src/.env

# Edit configuration (update with your values)
nano src/.env
```

## 3. Start Services
```bash
# Start PostgreSQL, Redis, and FastAPI with hot reload
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.override.yml up -d
```

## 4. Initialize Database
```bash
# Run database migrations
docker-compose exec app alembic upgrade head

# Seed initial data (optional)
docker-compose exec app python -m app.initial_data
```

## 5. Access Application
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 6. Development Workflow
```bash
# Watch logs (all services)
docker-compose logs -f

# Run tests
docker-compose exec app pytest -v

# Enter app container shell
docker-compose exec app bash

# Stop services and cleanup DB
docker-compose down -v --remove-orphans
```

## 7. Production Build
```bash
# Build production image
docker build -f docker/Dockerfile -t fastapi-golden:prod .

# Run production container
docker run -d --name myapp \
  -p 8000:8000 \
  --env-file src/.env \
  fastapi-golden:prod
```

## Common Tasks

### Run Pre-commit Checks
```bash
pre-commit run --all-files
```

### Update Dependencies
```bash
uv sync --all-groups
```

### Add New Migration
```bash
docker-compose exec app alembic revision --autogenerate -m "Description"
```

### Access Database
```bash
# Connect via psql
docker-compose exec db psql -U $POSTGRES_USER -d $POSTGRES_DB
```

### Test API Endpoints
```bash
# Get access token
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=password"

# Authenticated request
curl "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer <TOKEN>"
```

## Troubleshooting

**Database connection issues?**
```bash
docker-compose exec app python -m app.backend_pre_start
```

**Tests failing?**
```bash
docker-compose exec app pytest --setup-show -v
```

**Application not starting?**
```bash
docker-compose logs app
```

**Pre-commit hooks failing?**
```bash
pre-commit run --all-files --show-diff-on-failure
```

## Next Steps
1. Explore API documentation at http://localhost:8000/docs
2. Customize models in `src/app/models.py`
3. Add new endpoints in `src/app/api/`
4. Configure CI/CD in `.github/workflows/build.yaml`
5. Extend Docker setup for production deployment
