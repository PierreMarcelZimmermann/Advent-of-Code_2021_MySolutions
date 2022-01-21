import re

# reading the input file to a string
input_file = open("input", "r")

input_string = input_file.read()

input_file.close()



# dividing the input file by line
input_string_by_line = re.findall("[\d]+", input_string)

# dividing lines by column

columns_1_through_5 = []
for x in range(0, len(input_string_by_line[0])):
    columns_1_through_5.append([])
    for i in range(0, len(input_string_by_line)):
        columns_1_through_5[x].append((input_string_by_line[i][x:x + 1]))

# finding out if 1 or 0 is more common and adding either 1 or 0 to the gamma rate because of it

gamma_rate = []

for n in range(0, len(columns_1_through_5)):
    l = []
    for i in range(0, len(columns_1_through_5[n])):
        l.append(columns_1_through_5[n][i])
    l = list(map(int, l))
    l = sum(l)
    if l > len(columns_1_through_5[n]) / 2:
        gamma_rate.append(1)
    else:
        gamma_rate.append(0)

# flipping the gamma rate to get the epsilon rate


epsilon_rate = []

for n in range(0, len(gamma_rate)):
    if gamma_rate[n] == 1:
        epsilon_rate.append("0")
    if gamma_rate[n] == 0:
        epsilon_rate.append("1")

# converting the rates to int and multiplying them to get the result

gamma_rate=map(str, gamma_rate)
gamma_rate ="".join(gamma_rate)
epsilon_rate ="".join(epsilon_rate)

gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2)
result = gamma_rate*epsilon_rate

print(result)