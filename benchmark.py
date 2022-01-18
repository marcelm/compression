#!/usr/bin/env python3
import os
import sys
import time
import subprocess


# pigz

PROGRAMS = {
    "igzip": range(1, 4),
    "lzop": [1],
    "zstd": range(1, 10),
    "gzip": range(1, 10),
    "lz4": range(1, 10),
}


def measure(program: str, level: int, path: str) -> (float, float):
    """
    return pair (compressed size, elapsed wall-clock time)
    """
    start_time = time.time()
    if level is not None:
        command = f"{program} -{level} < {path}"
    else:
        command = f"{program} < {path}"
    print("Running", command, file=sys.stderr)
    result = subprocess.run(f"{command} | wc -c", shell=True, capture_output=True)
    size = int(result.stdout)
    elapsed = time.time() - start_time
    return (size, elapsed)


if __name__ == "__main__":
    path = sys.argv[1]
    fsize = os.stat(path).st_size
    size, elapsed = measure("cat", None, path)
    print("cat", 0, size, f"{elapsed:.3f}", sep="\t")
    for prog in PROGRAMS:
        for level in PROGRAMS[prog]:
            size, elapsed = measure(prog, level, path)
            print(prog, level, size, f"{elapsed:.3f}", sep="\t")
            sys.stdout.flush()
