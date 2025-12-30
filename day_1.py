# DAY ONE - input_dayOne.txt -> https://adventofcode.com/2025/day/1

def process_day_1(path):
    iterator = 50
    zero_hits = 0
    zero_rotation_hits = 0

    with open(path) as f:
        for rotation in f:
            direction = rotation[0]
            steps = int(rotation[1:-1])

            step = -1 if direction == "L" else 1

            for _ in range(steps):
                iterator = (iterator + step) % 100

                if iterator == 0 and _ < steps - 1:
                    zero_rotation_hits += 1

            if iterator == 0:
                zero_hits += 1

        return zero_hits, zero_hits + zero_rotation_hits

"""
result_one, result_two = process_day_1("inputs/input_day1.txt")
print(f"Day One --- Puzzle1: {result_one}, Puzzle2: {result_two}")
"""