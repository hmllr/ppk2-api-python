
"""
Basic usage of PPK2 Python API.
The basic ampere mode sequence is:
1. read modifiers
2. set ampere mode
3. read stream of data
"""
import time
from src.ppk2_api.ppk2_api import PPK2_MP as PPK2_API
from src.power_profiler import PowerProfiler
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("log_file", help="The name of the saved logging file")
parser.add_argument("time", help="Time to measure in seconds",
                    type=int)
args = parser.parse_args()

ppk2 = PowerProfiler(filename=args.log_file)

ppk2.enable_power()

ppk2.start_measuring()

time.sleep(args.time)

ppk2.stop_measuring()

ppk2.disable_power()