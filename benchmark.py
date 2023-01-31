#!/usr/bin/env python3
import os
import sys
import time
import subprocess


# pigz

PROGRAMS = {
    "crabz": range(1, 7),
    "pigz": range(1, 7),
    "bgzip": range(1, 7),
    "igzip": range(1, 4),
    "lzop": [1],
    "zstd": range(1, 10),
    "gzip": range(1, 10),
    "lz4": range(1, 7),
    "xz": range(1, 3),
}


def measure(program: str, level: int, path: str, n: int) -> (float, float):
    """
    return pair (compressed size, elapsed wall-clock time)
    """
    if level is not None:
        if program == "bgzip":
            command = f"{program} -l {level} < {path}"
            args = [program, "-l", str(level)]
        elif program == "crabz":
            command = f"{program} -l {level} -p 1 < {path}"
            args = [program, "-l", str(level), "-p", "1"]
        elif program == "pigz":
            command = f"{program} -{level} -p 1 < {path}"
            args = [program, f"-{level}", "-p", "1"]
        else:
            command = f"{program} -{level} < {path}"
            args = [program, f"-{level}"]
    else:
        command = f"{program} < {path}"
        args = [program]
    print("Measuring size by running", command, file=sys.stderr)
    result = subprocess.run(f"{command} | wc -c", shell=True, check=True, capture_output=True)
    size = int(result.stdout)

    elapsed = []
    for i in range(n):
        print("Measuring time, iteration", i + 1, file=sys.stderr)
        with open(path) as f:
            start_time = time.time()
            result = subprocess.run(args, check=True, stdin=f, stdout=subprocess.DEVNULL)
            elapsed.append(time.time() - start_time)
    print(elapsed, file=sys.stderr)
    return (size, min(elapsed))


if __name__ == "__main__":
    path = sys.argv[1]
    fsize = os.stat(path).st_size
    uncompressed, elapsed = measure("cat", None, path, 5)
    print("cat", 0, uncompressed, f"{elapsed:.3f}", sep="\t")
    for prog in PROGRAMS:
        for level in PROGRAMS[prog]:
            size, elapsed = measure(prog, level, path, 3)
            print(prog, level, size, f"{elapsed:.3f}", sep="\t")
            sys.stdout.flush()
