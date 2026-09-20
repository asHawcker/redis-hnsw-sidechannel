#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOT_DIR="$(cd "$PROJECT_DIR/.." && pwd)"

REDIS_DIR="$ROOT_DIR/redis"

echo "==> Restarting Redis"

if "$REDIS_DIR/src/redis-cli" -p 6380 ping >/dev/null 2>&1; then
"$REDIS_DIR/src/redis-cli" -p 6380 SHUTDOWN NOSAVE || true
sleep 1
fi

cd "$REDIS_DIR"
./src/redis-server redis-full.conf --port 6380

echo "==> Redis started on port 6380"