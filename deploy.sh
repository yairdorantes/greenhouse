#!/bin/bash
set -e
source .env

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd $SCRIPT_DIR

GIT_BRANCH="main"

echo "Deploying greenhouse backend..."

git pull origin $GIT_BRANCH

docker compose down || true

docker compose build

docker compose up -d

echo "Deploy done! :)"
