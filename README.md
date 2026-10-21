# Fitness Tracker

Workout logging, routines, progress dashboard, and a local RAG-based training assistant.

## Stack
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL (Supabase) + pgvector
- **AI:** RAG with a local LLM via Ollama
- **Infra:** Docker, GitHub Actions CI/CD, AWS
- **Frontend:** TBD (later milestone)

## Repo layout
```
backend/app/
  api/v1/routes/   HTTP layer (thin): validation, auth, calls services
  services/        Business logic (exercise index, workouts, stats)
  repositories/    Data access (SQL)
  models/          ORM models
  schemas/         Pydantic API contracts
  rag/             Ingestion, embeddings, retrieval, LLM
  core/            Config, security
  db/              DB session
backend/tests/     unit + integration tests
data/exercises/    Raw exercise dataset
docs/adr/          Architecture Decision Records
infra/aws/         Deployment config
```

## Milestones
1. Foundations: repo, FastAPI skeleton, health endpoint, Docker, CI (lint + tests)
2. Exercise catalog: dataset ingestion, in-memory index, search/filter API
3. Data model + auth: schema design, migrations, Supabase auth
4. Routines + workouts: CRUD, start from routine or empty, log sets
5. Analytics: 1RM, volume, PRs, streaks, calendar endpoint
6. RAG assistant: embeddings, pgvector, retrieval, tools, Ollama, evaluation
7. Deployment: AWS, CD pipeline, monitoring
8. Frontend
9. Polish: docs, architecture diagram, demo, load tests
