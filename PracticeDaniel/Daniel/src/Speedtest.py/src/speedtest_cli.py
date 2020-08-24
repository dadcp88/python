from subprocess import  Popen, PIPE, STDOUT
from pathlib import Path
PATH_TO_SPEEDTEST = Path(f'{__file__}')

def do_the_test():
    variable = Popen(f'')

    speedtest = Popen(f'[PATH_TO_SPEEDTEST]\\speedtest-cli\\speedtest.exe -f human-readable),
                      shell=True,
                      stdin=PIPE,
                      stdout=PIPE,
                      stderr=STDOUT)

    results = speedtest.stdout.read().decode()
