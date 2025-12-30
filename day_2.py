# Day TWO - input_dayTwo.txt -> https://adventofcode.com/2025/day/2

import math

def pt_one(current_id: int, digits: int):
    id = str(current_id)
    if digits % 2 != 0:
        return 0
    half = digits // 2
    return current_id if id[:half] == id[half:] else 0

def pt_two(currentId: int, digits: int):
    id = str(currentId)
    for i in range(2, digits + 1):
        if digits % i != 0:
            continue

        block_size = digits // i
        block = id[:block_size]

        if all(id[start:start + block_size] == block
               for start in range(0, digits, block_size)):
            return currentId
    return 0

def process_day_2(path):
    invalid_sum_one = invalid_sum_two = 0

    with open(path) as f:
        product_id_ranges = f.read().split(",")

        for p in product_id_ranges:
            start, end = map(int, p.split("-"))

            for current_id in range(start, end + 1):
                digits = int(math.log10(current_id)) + 1

                invalid_sum_one += pt_one(current_id, digits)
                invalid_sum_two += pt_two(current_id, digits)

        return invalid_sum_one, invalid_sum_two
    
"""
result_one, result_two = process_day_2("inputs/input_day2.txt")
print(f"Day Two --- Puzzle1: {result_one}, Puzzle2: {result_two}")
"""