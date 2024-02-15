import click
import subprocess
from time import sleep
from pathlib import Path

def main(pid, cmd, verbose):
    print(f'waiting for process {pid} and then run {cmd}')
    p = (Path(f'/proc/') / str(pid))
    if not p.exists():
        raise RuntimeError('process doesnt exist')
    while p.exists():
        sleep(1)

    proc = subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True)
    print(f'retcode: {proc.returncode}')
    print(f'stderr: {proc.stderr}')
    print(f'stdout:\n{proc.stdout}')


# test
# the & already separates the jobs
# sleep 10 & jobq $! 'echo hello'



@click.command()
@click.argument('pid', type=int)
@click.argument('cmd', type=str)
@click.option('-v', '--verbose', 'verbose', type=bool, is_flag=True, default=False)
def cli(*args, **kwargs):
    main(*args, **kwargs)


if __name__ == '__main__':
    cli()
