import argparse
import subprocess
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('times_file')
    parser.add_argument('video_file')
    args = parser.parse_args()

    with open(args.times_file) as f:
        lines = [line.strip() for line in f]

    for i, line in enumerate(lines, 1):
        print(f'doing {i}/{len(lines)}', flush=True)
        p1, _, p2 = line.split()
        t0 = time.time()
        subprocess.check_call(
            (
                'ffmpeg',
                '-hwaccel', 'cuda', '-hwaccel_output_format', 'cuda',
                '-ss', p1,
                '-to', p2,
                '-i', args.video_file,
                '-preset', 'slow',
                '-c:v', 'hevc_nvenc',
                f'{i:02}_clip.mov',
            ),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f'cut from {p1} to {p2} in {time.time()-t0:.2f}s', flush=True)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
