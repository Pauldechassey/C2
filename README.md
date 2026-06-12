# Very Basic FastAPI Architecture

Structure :

- app/
  - __init__.py
  - config.py
  - database.py
  - models/
  - schemas/
  - services/
  - routes/
- run.py
- requirements.txt

## Lancer l'application

```powershell
python run.py
```

Le serveur démarrera sur `http://127.0.0.1:8000`.

## API Endpoints

- `GET /api/users/`
- `GET /api/users/{user_id}`
- `POST /api/users/`
- `PUT /api/users/{user_id}`
- `DELETE /api/users/{user_id}`
