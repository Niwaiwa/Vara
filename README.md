# Vara
 A video streaming site about iwara copy.

## database

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
