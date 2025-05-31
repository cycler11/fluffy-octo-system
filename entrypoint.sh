#!/bin/bash

# Применяем миграции
flask db upgrade

# Инициализируем базу данных
flask init-db

# Запускаем приложение
exec "$@"