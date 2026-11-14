"""Copy the entry image to the output directory.

make.fun food-picture-01 entry: the program writes one picture of food
to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when unset).
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png is missing next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    # Fail loudly if the copy did not land byte-for-byte.
    if os.path.getsize(dest) != os.path.getsize(source):
        print("error: copied entry.png differs in size from the source",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
