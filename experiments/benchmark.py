import sys
import struct
import numpy as np
import redis

if len(sys.argv) < 2:
    print("Usage: python3 benchmark.py <runs> [dim]")
    sys.exit(1)

runs = int(sys.argv[1])
dim = int(sys.argv[2]) if len(sys.argv) > 2 else 128

r = redis.Redis(host="localhost", port=6380)

np.random.seed(123)
query = np.random.random(dim).astype(np.float32)
query_data = struct.pack(f"{dim}f", *query)

print("Running", runs, "queries")

for i in range(runs):
    r.execute_command(
        "FT.SEARCH",
        "idx",
        "*=>[KNN 10 @vector $q AS distance]",
        "PARAMS",
        "2",
        "q",
        query_data,
        "DIALECT",
        "2"
    )

    if (i + 1) % 100 == 0:
        print("Completed", i + 1)

print("Benchmark script finished")
