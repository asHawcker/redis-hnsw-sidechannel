import sys
import struct
import numpy as np
import redis


if len(sys.argv) < 2:
    print("Usage: python3 load_dataset.py <dataset.npy> [dimension]")
    sys.exit(1)

dataset_path = sys.argv[1]
dim = int(sys.argv[2]) if len(sys.argv) > 2 else 128

vectors = np.load(dataset_path)

if vectors.ndim != 2:
    print("Dataset must be a 2D array")
    sys.exit(1)

if vectors.shape[1] != dim:
    print("Dimension mismatch")
    print("Expected:", dim)
    print("Found:", vectors.shape[1])
    sys.exit(1)

r = redis.Redis(host="localhost", port=6380)

for i, vector in enumerate(vectors):
    data = struct.pack(f"{dim}f", *vector)
    r.hset(f"doc:{i}", mapping={"vector": data})

    if (i + 1) % 1000 == 0:
        print("Inserted", i + 1)

print("Inserted", len(vectors), "vectors")

