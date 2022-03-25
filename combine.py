from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import tempfile


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    args = parser.parse_args()

    args.input_dir = os.path.abspath(args.input_dir)

    filenames = sorted(
        os.path.join(args.input_dir, p)
        for p in os.listdir(args.input_dir) if p.endswith('_clip.mov')
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        filelist = os.path.join(tmpdir, 'filelist.txt')
        with open(filelist, 'w') as f:
            for filename in filenames:
                f.write(f'file {shlex.quote(filename)}\n')

        output = os.path.join(args.input_dir, 'out.mov')
        cmd = (
            'ffmpeg',
            '-safe', '0',
            '-hwaccel', 'cuda',
            '-hwaccel_output_format', 'cuda',
            '-f', 'concat',
            '-i', filelist,
            '-preset', 'slow',
            '-c:v', 'hevc_nvenc',
            output,
        )
        return subprocess.call(cmd)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
