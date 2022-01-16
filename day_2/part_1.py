import re

# this code is only usefull for solving part_1


# opening the file and reading it to a string

input_file = open("input", "r")

input_string = input_file.read()

input_file.close()

# extracting directions from the file and putting them in seperate lists

forward_lines = re.findall("forward+\s[\d]+", input_string)
up_lines = re.findall("up+\s[\d]+", input_string)
down_lines = re.findall("down+\s[\d]+", input_string)

# combining all list items into a string, extracting the numbers from the directions, adding them up in variables

forward_string = " ".join(forward_lines)
forward_numbers = re.findall("[\d]", forward_string)
forward = 0
for i in range(0, len(forward_numbers)):
    forward_numbers[i] = int(forward_numbers[i])
    forward = forward + forward_numbers[i]

up_string = " ".join(up_lines)
up_numbers = re.findall("[\d]", up_string)
up = 0
for i in range(0, len(up_numbers)):
    up_numbers[i] = int(up_numbers[i])
    up = up + up_numbers[i]

down_string = " ".join(down_lines)
down_numbers = re.findall("[\d]", down_string)
down = 0
for i in range(0, len(down_numbers)):
    down_numbers[i] = int(down_numbers[i])
    down = down + down_numbers[i]

# changing the position of the submarine based on the directions

x_position = 0 - up + down
y_poistion = 0 + forward

# calculating the solution

solution = x_position * y_poistion
print(solution)
