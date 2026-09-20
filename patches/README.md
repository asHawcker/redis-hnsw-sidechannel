This patch is the modification needed to be made to redis/redis to use _my_ versions of Redisearch and VectorSimilarity.

### Applying this Patch

1. Clone Redis 8.10.2.
2. Apply redis-modules.yaml.patch.
   ```bash
   make modules-update
   ```
   This fetches `asHawcker/redisearch` `research-v8.10.1` branch.
3. RediSearch's VectorSimilarity submodule then uses the modified version.
4. Run `build_redis.sh` from `scripts`.
