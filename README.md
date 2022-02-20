# Command Watcher [![Python Badge](https://img.shields.io/badge/-Python-00000??style=flat-square&logo=python&logoColor=FFD43B&color=informational)](https://www.python.org/downloads/)  [![Downloads](https://pepy.tech/badge/cmdwatch)](https://pepy.tech/project/cmdwatch) [![Downloads](https://pepy.tech/badge/cmdwatch/week)](https://pepy.tech/project/cmdwatch/week)

**cmdwatch** is a CLI tool to watch the output of a given command until certain conditions given by the user are satisfied. The conditions can be
1. There is a change in output
2. When the time limit exceeds

The output of the command will be shown in the console as well.
```
pip install cmdwatch
```

## Usage

```bash
$ cmdwatch -d DELAY [-o OUTPUT_FILE] [-t TIMEOUT] [-s] <cmd>

Command Watcher Tool

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        How long to wait until next execution
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        File where the output should be stored
  -t TIMEOUT, --timeout TIMEOUT
                        For how many second should i watch
  -s, --stop            Pass this option if you want to stop checking whenever
                        there is a difference in output
```
If you want to store the command outputs to a file then pass the --output/-o with the file name

Example:
```bash
$ cmdwatch -d 2 -o ping_check.txt ping google.com
```
Above usage will execute the "ping google.com" command every 2 seconds and stores the output into file ping_check.txt

If you want to stop the execution when there is a change in the output then pass --stop/-s option

Example:
```bash
$ cmdwatch -d 2 -o ping_check.txt -s ping google.com
```


