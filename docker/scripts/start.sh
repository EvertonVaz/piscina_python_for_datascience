#!/bin/bash
set -e

echo "Iniciando ambiente de desenvolvimento..."

cd mod00 && \
if [! -f "poetry.lock" ]; then
    echo "Arquivo poetry.lock não encontrado, criando novo ambiente..."
    poetry config virtualenvs.create false --local && \
fi
echo "Instalando dependências do Poetry..."
poetry install --no-root || true

echo "Container Iniciado!"

tail -f /dev/null
