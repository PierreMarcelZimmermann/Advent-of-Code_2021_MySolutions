import re

# opening the file and reading it to a string

input_file = open("input", "r")

input_string = input_file.read()

input_file.close()

# pulling each depth measurement out of input_string into a list

measurements = re.findall("[\d]+", input_string)

# adding the measurements up to triplets


measurements_int = list(map(int, measurements))
measurements_int_triplets = []
for i in range(0, len(measurements_int) - 2):
    measurements_int_triplets.append(measurements_int[i] + measurements_int[i + 1] + measurements_int[i + 2])

# checking whether the depth increases between triplets and if so, adding to the counter

counter = 0

for i in range(0, len(measurements_int_triplets) - 1):
    if measurements_int_triplets[i + 1] - measurements_int_triplets[i] > 0:
        counter = counter + 1

print(counter)
