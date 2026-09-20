#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOT_DIR="$(cd "$PROJECT_DIR/.." && pwd)"

REDISEARCH_DIR="$ROOT_DIR/RediSearch"
REDIS_DIR="$ROOT_DIR/redis"

MODULE_BUILD="$REDISEARCH_DIR/bin/linux-x64-release/search-community/redisearch.so"
MODULE_TARGET="$REDIS_DIR/modules/redisearch/redisearch.so"

echo "==> Building RediSearch"
cd "$REDISEARCH_DIR"
./build.sh

echo "==> Updating Redis module"
cp "$MODULE_TARGET" "$MODULE_TARGET.backup"
cp "$MODULE_BUILD" "$MODULE_TARGET"

