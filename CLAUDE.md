# {repo-name} — Claude Context

## Project
- Part of TimeLabs NPO (github.com/timelabs-npo)
- Backend: rhea-tribunal.fly.dev (production API)
- All clients authenticate via JWT (POST /auth/signup, POST /auth/login)

## Conventions
- Conventional commits: feat(), fix(), chore(), docs()
- Semantic versioning for releases
- No secrets in code — use environment variables
- Test before push

## API Endpoints (common)
- POST /tribunal — multi-model consensus query
- GET /tasks — task queue
- GET /governor — token budget status
- GET /aletheia/proofs — verified invariants
- GET /agents/status — agent health
