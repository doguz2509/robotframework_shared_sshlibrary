
import sys

from robot import run_cli

USAGE = f"""{sys.argv[0]} <HOST> <USER> <PASSWORD> [<PROMPT>]"""

if __name__ == '__main__':
    if len(sys.argv) < 4:
        err = SystemExit(USAGE)
        err.code = -1
        raise err

    cmd = f'-v HOST:{sys.argv[1]} -v USER:{sys.argv[2]} -v PASSWORD:{sys.argv[3]}'
    if len(sys.argv) == 5:
        cmd += f' -v PROMPT:{sys.argv[4]}'

    assert run_cli(cmd, exit=False) == 0
