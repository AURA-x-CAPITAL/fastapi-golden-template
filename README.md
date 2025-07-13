[![Golden Template](https://img.shields.io/badge/FastAPI-Golden_Template-%2300C7B7?logo=fastapi)](https://github.com/AURA-x-CAPITAL/fastapi-golden-template)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://hub.docker.com/)

Inspired by [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)

# FastAPI Golden Template

**The production-ready FastAPI starter for serious projects**
> Batteries included, complexity excluded

**Welcome to the foundation we use at AuraXcapital** - a template that helped us build blockchain backends processing 50K+ daily transactions. Now open-sourced for the community.

```python
# Why developers choose this template
from fastapi import FastAPI
from golden_template import time_saved, production_readiness

app = FastAPI()

@app.get("/benefits")
def project_advantages():
    return {
        "weeks_saved": 3,
        "security": "built-in",
        "scalability": "proven"
    }
```

## Why This Template?

Building production APIs requires more than endpoints. This template gives you:

- 🚀 **Launch-ready foundation** - All essentials pre-configured
- 🔐 **Security by design** - JWT auth, password hashing, rate limiting
- 📦 **DevOps included** - CI/CD, Docker, pre-commit hooks
- 🐳 **Kubernetes optimized** - Structured logging, health checks
- 💡 **Best practice blueprint** - Async architecture, type hints, proper error handling

**Perfect for**: DeFi platforms, NFT services, game backends, and scalable microservices

## What's Inside

| Category    | Technologies                                                    |
|-------------|-----------------------------------------------------------------|
| **DevOps**  | Pre-commit hooks, Test coverage, Dependabot, Multi-stage builds |
| **Quality** | Type hints, PEP8 compliance, Automated formatting, pytest       |


## Documentation Roadmap

| Guide                                        | Purpose                  |
|----------------------------------------------|--------------------------|
| [Motivation](docs/motivation.md)             | Why we built this        |
| [Directory Structure](docs/dir-structure.md) | Project layout explained |
| [Docker Setup](docs/docker.md)               | Containerization guide   |
| [Pre-commit Hooks](docs/pre-commit.md)       | Code quality automation  |
| [App Requirements](docs/app-requirements.md) | Configuration and setup  |

## Contribution Welcome

We value:
- Clear issues with reproduction steps
- Well-documented pull requests
- Security-conscious code
- Tests for new features

**Begin here**:
1. Fork repository
2. Create feature branch (`feat/your-feature`)
3. Submit pull request

## License

MIT License - the same freedom we value in blockchain development. Use freely, contribute back when you improve it.

---
**Build with confidence**.
**Deploy with certainty**.
**Scale with ease**.

[Explore the documentation](docs/) | [Report an issue](https://github.com/AURA-x-CAPITAL/fastapi-golden-template/issues)
