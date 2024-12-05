from aocd import get_data, submit
import numpy as np

result = 0
d = get_data(day=4, year=2024)

# read into numpy array
arr = np.array([list(line) for line in d.splitlines()])

# count XMAS in a string
def count_XMAS(s: str) -> int:
    return s.count("XMAS") + s.count("SAMX")

# convert a 2d numpy array to a multi line string
def arr_to_str(arr: np.ndarray) -> list:
    return "\n".join("".join(row) for row in arr)

result += count_XMAS(d) # rows
result += count_XMAS(arr_to_str(arr.T)) # columns
dia = ["".join(arr.diagonal(i)) for i in range(-arr.shape[0] + 1, arr.shape[1])]
result += count_XMAS(arr_to_str(["".join(arr.diagonal(i)) for i in range(-arr.shape[0] + 1, arr.shape[1])])) # diagonal
result += count_XMAS(arr_to_str(["".join(np.fliplr(arr).diagonal(i)) for i in range(-arr.shape[0] + 1, arr.shape[1])])) # diagonal 2

submit(result, part="a", day=4, year=2024)