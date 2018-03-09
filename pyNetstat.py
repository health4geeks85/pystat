from subprocess import Popen, PIPE
import sys
import signal
import win32api


FILE_PATH = r'C:\Windows\System32\NETSTAT.EXE'
FILTERED_PORT = '3389'
PROC = None

def exitGracefully(signum, frame):
    if PROC:
        PROC.kill()
    return True

def winExit(*args):
    if PROC:
        PROC.kill()
    return True


def registerSignals():
    signal.signal(signal.SIGINT, exitGracefully)
    signal.signal(signal.SIGTERM, exitGracefully)
    signal.signal(signal.SIGABRT, exitGracefully)
    signal.signal(signal.SIGSEGV, exitGracefully)
    signal.signal(signal.SIGILL, exitGracefully)
    signal.signal(signal.SIGFPE, exitGracefully)
    win32api.SetConsoleCtrlHandler(winExit, True)

def netstat(*args):
    global PROC
    registerSignals()
    print("WELCOME TO NETSTAT!!!")
    params = [FILE_PATH, *args]
    with Popen(params,
               stdout=PIPE,
               stderr=sys.stdout.buffer) as proc:
        PROC = proc
        for line in iter(proc.stdout.readline, b''):
            nl = line.decode()
            if FILTERED_PORT not in nl:
                print(nl, end='')


if __name__ == '__main__':
    netstat(*sys.argv[1:])