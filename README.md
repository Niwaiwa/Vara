# Vara
 A video streaming site practice.

## run server

local

```
python manage.py runserver
```

## start database

start db

```
docker-compose -f docker-mysql.yml up -d
```

stop db

```
docker-compose -f docker-mysql.yml down
```


# model

make a migration from model

```
python manage.py makemigrations app
```

run migrate

```
python manage.py migrate
```

display migrate sql

```
python manage.py sqlmigrate myapp 0001
```

## dotenv

```
SECRET_KEY=
DEBUG=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
