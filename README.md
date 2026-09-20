# Redis HNSW Side-Channel

## Software Versions

| Component                  | Version / Branch   |
| -------------------------- | ------------------ |
| OS                         | Ubuntu 22.04+      |
| Redis                      | 8.10.2             |
| RediSearch                 | v8.10.1            |
| RediSearch research branch | `research-v8.10.1` |
| VectorSimilarity           | `research-hnsw`    |
| Python                     | 3.x                |
| Compiler                   | GCC / G++          |
| Build system               | CMake + Make       |

## Repository Dependencies

The source dependency chain is:

```text
Redis
  │
  └── RediSearch
        │
        └── VectorSimilarity
              │
              └── HNSW
```

Redis uses `modules/modules.yaml` to determine which RediSearch repository and revision to use.

RediSearch uses VectorSimilarity as a Git submodule.

### Redis

Redis 8.10.2: [https://github.com/redis/redis]

### RediSearch forked

[RediSearch v8.10.1](https://github.com/asHawcker/redisearch) - branch : `research-v8.10.1`

### VectorSimilarity forked

[VectorSimilarity](https://github.com/asHawcker/VectorSimilarity) - branch : `research-hnsw`

## Directory Setup

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

Clone Redis:

```bash
git clone --branch 8.10.2 https://github.com/redis/redis.git redis
```

Clone the RediSearch research fork:

```bash
git clone https://github.com/asHawcker/redisearch.git RediSearch
cd RediSearch
git checkout research-v8.10.1

git submodule update --init --recursive     # Initialize the RediSearch submodules
```

## Configure Redis to Use the modified RediSearch

Redis normally uses its own RediSearch repository configuration.

Apply the patch included in this repository `patches/redis-modules.yaml.patch`

From the Redis source directory:

```bash
cd ~/project/redis
git apply ~/project/redis-sidechannel-hnsw/patches/redis-modules.yaml.patch
```

The patch changes the RediSearch dependency in `modules/modules.yaml` to use modified RediSearch.

Update the Redis modules:

```bash
make modules-update
```

## Build

Run `scripts/build_redis.sh`.

## Start Redis

This setup uses port `6380`.

Run `scripts/run_redis.sh`.

## Python Dependencies

Python experiment scripts currently use the Redis Python client and NumPy.

Install them with:

```bash
pip install redis numpy
```
