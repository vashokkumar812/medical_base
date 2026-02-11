# Medical Wiki (Django + Next.js + Postgres)

This repository provides a Dockerized medical wiki stack with:

- **Django + DRF** backend for diseases, symptoms, risk factors, and drugs.
- **Next.js + Material UI** frontend.
- **PostgreSQL** database.

## Quick start

```bash
docker compose up --build
```

- Backend API: `http://localhost:8000/api/`
- Admin: `http://localhost:8000/admin/`
- Frontend: `http://localhost:3000/`

## Backend models

- Disease (name, description, image)
- Symptom (name, description, image, diseases)
- RiskFactor (name, description, image, diseases)
- Drug (name, description, image, diseases)

Images can be uploaded for all models via the admin or API. Disease names remain plain text.

## Create a superuser

```bash
docker compose run --rm backend python manage.py createsuperuser
```

## Run migrations

```bash
docker compose run --rm backend python manage.py migrate
```

## Troubleshooting

If you see `Django is not installed in this environment` when running `python backend/manage.py ...`, install dependencies first:

```bash
python -m pip install -r backend/requirements.txt
```

If local package installation is restricted, use Docker instead:

```bash
docker compose up --build
```
