import re

# this code is only usefull for solving part_1


# opening the file and reading it to a string

input_file = open("input", "r")

input_string = input_file.read()

input_file.close()
# seperating the insructions into seperate lines and adding them to a list

seperate_lines = re.findall("[\w]+\s\d", input_string)

# declaring the variables

x_position = 0
y_poistion = 0
aim = 0

# for-loop which iterates over the list, checks whether the line say "forward", "up" or "down", pulls the out the number
# and calculates the position and or aim based on it

for i in range(0, len(seperate_lines)):
    if "forward" in seperate_lines[i]:
        x_position = x_position + int(re.search("\d", seperate_lines[i]).group())
        y_poistion = y_poistion + aim * int(re.search("\d", seperate_lines[i]).group())

    if "up" in seperate_lines[i]:
        aim = aim - int(re.search("\d", seperate_lines[i]).group())

    if "down" in seperate_lines[i]:
        aim = aim + int(re.search("\d", seperate_lines[i]).group())

# calculate the solution
solution = x_position * y_poistion
print(solution)
