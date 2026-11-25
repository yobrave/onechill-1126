import json
import os
import pathlib
import sys

MAX_CHARS = 200
TAG = "one-line-one-chill"


def read_line(folder):
    path = pathlib.Path(folder).joinpath("entry.txt")
    blob = path.read_bytes()
    return blob, blob.decode("utf-8")


def judge(text):
    trimmed = text.strip()
    holds = bool(trimmed) and len(trimmed) <= MAX_CHARS and len(text) <= MAX_CHARS
    return holds


def deliver(folder, blob):
    picked = os.environ.get("MAKEFUN_OUTPUT_DIR")
    base = pathlib.Path(picked) if picked else pathlib.Path(folder) / "out"
    base.mkdir(parents=True, exist_ok=True)
    goal = base / "entry.txt"
    goal.write_bytes(blob)
    return goal


def flow():
    spot = pathlib.Path(__file__).resolve().parent
    blob, line = read_line(spot)
    passes = judge(line)
    goal = deliver(spot, blob)
    print(json.dumps({"tag": TAG, "rev": "chill-r2", "goal": str(goal), "size": len(line), "passes": passes}))
    return 0 if passes else 2


if __name__ == "__main__":
    sys.exit(flow())
