from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('times_file')
    args = parser.parse_args()

    with open(args.times_file) as f:
        lines = [line.strip() for line in f]

    ts = 0
    for line in lines:
        ch, cm, cs = ts // (60 * 60), ts % (60 * 60) // 60, ts % 60
        print(f'- {ch:02}:{cm:02}:{cs:02} -')
        p1, _, p2 = line.split()
        p1_h, p1_m, p1_s = p1.split(':')
        p2_h, p2_m, p2_s = p2.split(':')
        p1_ts = 60 * 60 * int(p1_h) + 60 * int(p1_m) + int(p1_s)
        p2_ts = 60 * 60 * int(p2_h) + 60 * int(p2_m) + int(p2_s)
        ts += p2_ts - p1_ts
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
