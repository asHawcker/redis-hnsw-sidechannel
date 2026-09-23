import sys
import csv
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python3 collect_timings.py <timing.log> [output_file]")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else f"../results/hnsw_timings{datetime.now().time()}.csv"

timings = []

with open(input_file) as f:
    for line in f:
        if "HNSW_TIME (in ns)" in line:
            time_ns = int(line.split()[-1])
            timings.append(time_ns)

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["run_id", "time_ns"])

    for i, time_ns in enumerate(timings):
        writer.writerow([i + 1, time_ns])


print("Collected", len(timings), "timings")
print("Results:", output_file)