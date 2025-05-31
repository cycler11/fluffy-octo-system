#!/bin/bash

set -e

# Инициализация миграций
flask db init

# Создание миграции
flask create-migration "Initial migration"

# Применение миграций
flask db upgrade

# Инициализация данных
flask init-db
