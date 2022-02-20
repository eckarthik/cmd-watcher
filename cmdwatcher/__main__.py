import subprocess
import os
import argparse
import sys
import time

parser = argparse.ArgumentParser(description="Command Watcher Tool", add_help=True, usage="watcher.py -d DELAY [-o OUTPUT_FILE] [-t TIMEOUT] [-s] <cmd>")
parser.add_argument("-d", "--delay", help="How long to wait until next check", dest='delay', type=int, required=True)
parser.add_argument("-o", "--output", help="File where the output should be stored", dest='output_file')
parser.add_argument("-t", "--timeout", help="For how many seconds should I watch the output", dest='timeout', type=int)
parser.add_argument("-s", "--stop",
                    help="Pass this option if you want to stop checking whenever there is a change in output",
                    dest='stop',action='store_true')
try:
    args, unknown_args = parser.parse_known_args()
except:
    parser.print_help()
    sys.exit(0)
delay = args.delay or 3
output_file = args.output_file or None
if len(unknown_args) == 0:
    sys.stderr.write("Pass a command to execute. See watcher.py --help for instructions")
    sys.exit(0)
command = " ".join(unknown_args)
timeout = args.timeout or None
previous_output = ""
try:
    while True:
        if timeout:
            timeout = timeout - delay
        command_output = subprocess.check_output(command, shell=True).decode("utf-8")
        if args.stop:
            # User wants to run only when the output is different everytime
            if command_output != previous_output:
                sys.stdout.write(f"Watching output for \"{command}\" for every {delay} seconds\n\r\n\r")
                sys.stdout.write(command_output + "\r")
                if output_file:
                    fo = open(output_file, "a+")
                    fo.write(command_output + "\n" + "---" * 30 + "\n")
                    fo.close()
                sys.stdout.flush()
                time.sleep(delay)
                if timeout:
                    if timeout <= 0:
                        break
                break
        else:
            # User wants to run everytime
            sys.stdout.write(f"Watching output for \"{command}\" for every {delay} seconds\n\r\n\r")
            sys.stdout.write(command_output + "\r")
            if output_file:
                fo = open(output_file, "a+")
                fo.write(command_output + "\n" + "---" * 30 + "\n")
                fo.close()
            sys.stdout.flush()
            time.sleep(delay)
            os.system("cls")
            if timeout:
                if timeout <= 0:
                    break
except KeyboardInterrupt:
    sys.stdout.write("Stopping execution")

def main():
    parser.print_help()

if __name__ == '__main__':
    args = sys.argv
    main()
