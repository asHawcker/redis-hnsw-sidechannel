import redis
import struct

print("Starting...")

r = redis.Redis(host="localhost", port=6380)

print("Connected:", r.ping())

query = struct.pack("3f", 1.0, 0.0, 0.0)

print("Running query...")

result = r.execute_command(
    "FT.SEARCH",
    "idx",
    "*=>[KNN 2 @vector $q AS distance]",
    "PARAMS",
    "2",
    "q",
    query,
    "DIALECT",
    "2"
)

print("Result:")
print(result)