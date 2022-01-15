import re

# opening the file and reading it to a string

input_file = open("input", "r")

input_string = input_file.read()

input_file.close()

# pulling each depth measurement out of input_string into a list

measurements = re.findall("[\d]+", input_string)
measurements_int = list(map(int, measurements))

# checking whether the depth increases and if so, adding to the counter

counter = 0

for n in range(0, len(measurements_int) - 1):
    if measurements_int[n + 1] - measurements_int[n] > 0:
        counter = counter + 1

print(counter)
