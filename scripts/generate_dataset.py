import numpy as np
import sys

np.random.seed(42)

if len(sys.argv) < 2:
    print("Usage: python3 generate_dataset.py <size> [dim]")
    sys.exit(1)

size = int(sys.argv[1])
dim = int(sys.argv[2]) if len(sys.argv) > 2 else 128

# 10000 vectors with dimension 128
vectors = np.random.random((size, dim)).astype(np.float32)
np.save("../datasets/vectors_10k_128.npy", vectors)

print("Generated", len(vectors), "vectors")