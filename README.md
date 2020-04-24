# COVID-SC APP

- [Dependências](#dependências)
- [Configurações](#configurações)
- [Desenvolvimento](#desenvolvimento)
- [Deploy](#deploy)

## Dependências

- Python 3.8.0
- Django >= 3.0
- PostgreSQL 12.2
- Docker Compose

```sh
poetry install
```

## Configurações

```sh
cp local.env .env
```

Subir a base PostgreSQL com o Docker Compose:

```sh
docker-compose up -d
```

E rodar as migrações:

```sh
poetry run python manage.py migrate
```

## Desenvolvimento

Executando a aplicação no ambiente local:

```sh
poetry run python manage.py runserver
```

## Deploy

```sh
git push heroku master
```
