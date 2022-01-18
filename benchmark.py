#!/usr/bin/env python3
import os
import sys
import time
import subprocess

PROGRAMS = [
#    "gzip",
    "igzip",
    #"pigz",
    "lzop",
    "lz4",
    "zstd",
]


def measure(program: str, level: int, path: str) -> (float, float):
    """
    return pair (compressed size, elapsed wall-clock time)
    """
    start_time = time.time()
    command = f"{program} -{level} < {path}"
    print("Running", command, file=sys.stderr)
    result = subprocess.run(f"{command} | wc -c", shell=True, capture_output=True)
    size = int(result.stdout)
    elapsed = time.time() - start_time
    return (size, elapsed)


if __name__ == "__main__":
    path = sys.argv[1]
    fsize = os.stat(path).st_size
    for prog in PROGRAMS:
        for level in range(1, 10):
            size, elapsed = measure(prog, level, path)
            print(prog, level, size, f"{elapsed:.3f}", sep="\t")
            sys.stdout.flush()
