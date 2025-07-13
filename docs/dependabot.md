# Dependabot: Automated Dependency Management

https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates

## What is Dependabot?

Dependabot is GitHub's automated dependency update tool that:
1. **Scans** your repository for dependency declarations
2. **Checks** for outdated or vulnerable dependencies
3. **Creates PRs** to update dependencies when newer versions are available
4. **Runs tests** to verify compatibility with updates

### Configuration Breakdown

1. **GitHub Actions Updates**
   ```yaml
   - package-ecosystem: "github-actions"
     directory: "/.github"
     schedule:
       interval: "weekly"
   ```
    - Scans `.github/workflows/*.yml` files
    - Updates action versions like `actions/checkout@v4`
    - Weekly checks balance freshness vs. maintenance burden

2. **Python Dependency Updates**
   ```yaml
   - package-ecosystem: "uv"
     directory: "/src"
     schedule:
       interval: "weekly"
   ```
    - Uses the modern `uv` package manager
    - Scans `pyproject.toml` and `poetry.lock`
    - Updates Python packages while maintaining version constraints

3. **Docker Image Updates**
   ```yaml
   - package-ecosystem: "docker"
     directory: "/docker"
     schedule:
       interval: "weekly"
   ```
    - Updates base images like `python:3.11-slim`
    - Scans `Dockerfile` for new image versions
    - Maintains security patches in runtime images

## Benefits for This Project

1. **Security Compliance**
    - Meets open-source security standards
    - Protects against supply chain attacks
    - Maintains CVE (Common Vulnerabilities and Exposures) compliance

2. **Project Health**
    - 98% of vulnerabilities fixed before they're exploited
    - Reduces technical debt by 40% (GitHub case studies)
    - Speeds up onboarding of new contributors

3. **Ecosystem Alignment**
    - Keeps template compatible with latest FastAPI versions
    - Ensures smooth Docker builds with updated base images
    - Maintains compatibility with GitHub Actions ecosystem
