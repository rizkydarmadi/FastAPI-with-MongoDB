# Research FastAPI with MongoDB

## Requirements

- python 3.10
- docker-compose

## How to run

- create mongoDB container with docker compose

```bash
sudo docker-compose up -d
```

- create virtual env

```bash
python -m venv env
```

- sign in to env (Linux or macOS)

```bash
source env/bin/activate
```

- install all dependency

```bash
pip install -r requirements.txt
```

- run program

```
uvicorn main:app --reload
```

- your app will be run in [here](http:127.0.0.1:8000/docs)
