import click
import subprocess
from time import sleep
from pathlib import Path
import sys

def main(pid: int, cmd: str, verbose: bool) -> None:
    print(f'waiting for process {pid} and then run {cmd}')
    p = (Path(f'/proc/') / str(pid))
    if not p.exists():
        raise RuntimeError('process doesnt exist')
    while p.exists():
        sleep(1)

    proc = subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True)
    print(str(proc.stderr), file=sys.stderr)
    print(str(proc.stdout), file=sys.stdout)


# test
# the & already separates the jobs
# sleep 10 & jobq $! 'echo hello'

@click.command()
@click.argument('pid', type=int)
@click.argument('cmd', type=str)
@click.option('-v', '--verbose', 'verbose', type=bool, is_flag=True, default=False)
def cli(*args, **kwargs):
    '''
    jobq runs a cmd after a process with pid has finished (regardless of sucess)
    '''
    main(*args, **kwargs)


if __name__ == '__main__':
    cli()
