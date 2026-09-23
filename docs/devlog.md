# Devlog

## 19-9-2026

- Setup the working directory structure on my system. The directory structure is as follows:

```bash
~/project/
│
├── redis/                          # upstream with redis/redis
│   └── modules/modules.yaml        # local modification (I'll make this into a patch file later)
│
├── redisearch/                     # _my_ redisearch fork
│   └── deps/
│       └── VectorSimilarity/       # submodule clone of _my_ VectorSimilarity fork
│
├── VectorSimilarity/               # clone of _my_ VectorSimilarity fork
│
└── redis-hnsw-sidechannel/         # main project repo
    ├── docs/                       # documentations
    ├── analysis/
    ├── experiments/                # these folder names are just projected names
    ├── scripts/                    # that I might use
    ├── results/
    └── datasets/
```

## 20-9-2026

- Looked for the implemetation with `grep -R "search" -n src/VecSim/algorithms/hnsw/hnsw*.h` (cwd: `~/projects/redisearch/deps/VectorSimilarity/`)
- added timers around `topKQuery(...)` implementation. rebuilding and testing Redisearch
- made `build_redis.sh` script to perform the following actions:
  1. Build RediSearch with the changes that were made.
  2. Copy the redisearch.so file into redis directory.
  3. Build Redis.
- Generated the patch file for the `redis/redis` repo.
- Added scripts to generate and load sample datasets.

## 23-9-2026

- Modify the timing printing code to write to file and collect.
- Instead of writing to a file I am just writing to stderr and capturing it in the terminal, then, a seperate script picks out the timings into a csv. `collect_timings.py`
- The script should be run from the `scripts` folder.
- Added a `benchmark.py` to execute any number of queries to the Redis DB. The benchmark uses a different seed `128` for the random generations whereas the install script used `7236`.

So the steps to get the data would be.

1. `cd ~/projects/redis-sidechannel-hnsw/experiments`
2. `python3 benchmark.py`
3. `cd ../scripts`
4. `python3 collect_timings.py`

The data is now saved in results/hnsw_timings.csv
