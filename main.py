"""
Main entry point for running all Day processors.

This script:
- Automatically discovers all modules named day_<number>.py
- Imports each module dynamically
- Calls its process_day_<number>() function
- Measures execution time for each day
- Prints results in a consistent format
"""

import importlib
import os
import re
import time


DAY_PATTERN = re.compile(r"day_(\d+)\.py$")


def discover_day_modules(directory="."):
    day_files = []

    for filename in os.listdir(directory):
        match = DAY_PATTERN.match(filename)
        if match:
            day_number = int(match.group(1))
            day_files.append((day_number, filename[:-3]))

    return sorted(day_files, key=lambda x: x[0])


def run_day(module_name, day_number):
    module = importlib.import_module(module_name)
    func_name = f"process_day_{day_number}"

    if not hasattr(module, func_name):
        raise AttributeError(f"{module_name} does not define {func_name}()")

    func = getattr(module, func_name)

    input_path = f"inputs/input_day{day_number}.txt"

    start = time.perf_counter()
    p1, p2 = func(input_path)
    duration = time.perf_counter() - start

    return p1, p2, duration


def main():
    day_modules = discover_day_modules()

    if not day_modules:
        print("No day modules found.")
        return

    for day_number, module_name in day_modules:
        try:
            p1, p2, duration = run_day(module_name, day_number)
            print(
                f"Day {day_number:02d} --- "
                f"Puzzle1: {p1}, Puzzle2: {p2} "
                f"(Time: {duration:.4f}s)"
            )
        except Exception as e:
            print(f"Error running Day {day_number}: {e}")


if __name__ == "__main__":
    main()
