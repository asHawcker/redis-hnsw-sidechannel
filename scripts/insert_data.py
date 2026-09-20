import redis
import struct

r = redis.Redis(host="localhost", port=6380)

vectors = {
    "doc:1": [1.0, 0.0, 0.0],
    "doc:2": [0.9, 0.1, 0.0],
    "doc:3": [0.0, 1.0, 0.0],
    "doc:4": [0.0, 0.9, 0.1],
    "doc:5": [0.0, 0.0, 1.0],
}

for key, vector in vectors.items():
    data = struct.pack("3f", *vector)
    r.hset(key, mapping={"vector": data})

print("Inserted", len(vectors), "vectors")