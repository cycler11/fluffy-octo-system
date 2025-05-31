#!/bin/bash

set -e

# Ожидаем доступности PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "user" -d "library" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - executing commands"

# Применяем миграции
flask db upgrade

# Инициализируем базу данных
flask init-db

# Запускаем приложение
exec "$@"
