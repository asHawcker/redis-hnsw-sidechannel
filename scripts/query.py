import redis
import struct
import numpy as np

print("Starting...")

r = redis.Redis(host="localhost", port=6380)

print("Connected:", r.ping())

dim = 128

query = np.random.random(dim).astype(np.float32)
query_data = struct.pack(f"{dim}f", *query)

print("Running query...")

result = r.execute_command(
    "FT.SEARCH",
    "idx",
    "*=>[KNN 10 @vector $q AS distance]",
    "PARAMS",
    "2",
    "q",
    query,
    "DIALECT",
    "2"
)

print("Result:")
print(result)