from subprocess import Popen, PIPE
import sys


FILE_PATH = r'C:\Windows\System32\NETSTAT.EXE'
FILTERED_PORT = '3389'

def netstat(*args):
    params = [FILE_PATH, *args]
    with Popen(params,
               stdout=PIPE,
               stderr=sys.stdout.buffer) as proc:
        for line in iter(proc.stdout.readline, b''):
            nl = line.decode()
            if FILTERED_PORT not in nl:
                print(nl, end='')

if __name__ == '__main__':
    netstat(*sys.argv[1:])