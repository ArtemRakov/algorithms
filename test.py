import argparse
import unittest
import importlib.util
import time

parser = argparse.ArgumentParser()
parser.add_argument("path", help="give path to the source folder")

args = parser.parse_args()
path = args.path

spec = importlib.util.spec_from_file_location("solution", path + "solution.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

for i in range(6):
    f = open("{}test.{}.in".format(path, i))
    content = f.read().strip().split(", ")
    content = list(map(int, content))
    start_time = time.time()
    result = str(solution.solve(content))
    end_time = time.time()
    expected_file = open("{}test.{}.out".format(path, i))
    expected = expected_file.read().strip()
    print("Expected: {}".format(expected))
    print("Got: {}".format(result))
    print("Result {}".format(result == expected))
    print("Time: {}".format(end_time - start_time))
    print("----")

