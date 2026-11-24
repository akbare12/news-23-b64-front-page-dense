#!/usr/bin/env python3
"""news-23 b64 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is empty", file=sys.stderr)
        return 1
    out_dir_abs = os.path.abspath(out_dir)
    here_abs = os.path.abspath(here)
    if out_dir_abs == here_abs or out_dir_abs.startswith(here_abs + os.sep):
        print("error: MAKEFUN_OUTPUT_DIR must be outside the repo", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        data = f.read()
    if len(data) > 1024 * 1024:
        print("error: entry.png over 1 MiB", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: not a PNG", file=sys.stderr)
        return 1
    w, h, depth, ctype = struct.unpack(">IIBB", data[16:26])
    if (w, h) != (1024, 1024):
        print("error: entry.png is not 1024x1024", file=sys.stderr)
        return 1
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("error: PNG IEND trailer malformed", file=sys.stderr)
        return 1
    os.makedirs(out_dir_abs, exist_ok=True)
    dst = os.path.join(out_dir_abs, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        back = f.read()
    if back != data:
        print("error: output does not match source", file=sys.stderr)
        return 1
    # Verified: 1024x1024 RGB PNG, well-formed IEND, byte-identical copy.
    print("wrote", dst, len(data), "bytes, sha256",
          hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
