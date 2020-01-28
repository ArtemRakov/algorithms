import argparse
import unittest
import importlib.util

parser = argparse.ArgumentParser()
parser.add_argument("path", help="give path to the source folder")

args = parser.parse_args()
path = args.path

spec = importlib.util.spec_from_file_location("solution", path + "solution.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

for i in range(4):
    f = open("{}test.{}.in".format(path, i))
    content = f.read().strip()
    result = str(solution.solve(content))
    expected_file = open("{}test.{}.out".format(path, i))
    expected = expected_file.read().strip()
    print("Expected: {}".format(expected))
    print("Got: {}".format(result))
    print("Result {}".format(result == expected))
    print("----")

