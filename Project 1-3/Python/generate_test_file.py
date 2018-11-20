def addOne(string):
    i = len(string)-1
    carry = 1;
    newstring = ""
    while not i < 0:
        if int(string[i]) + int(carry) == 2:
            newstring = "1" + newstring
            carry = 1
        elif int(string[i]) + int(carry) == 1:
            newstring = "1" +newstring
            carry = 0
        elif int(string[i]) + int(carry) == 0:
            newstring = "0" + newstring
        i -= 1
    return newstring

def extend(data):
    while len(data) < 8:
        data = "0" + data
    return data

def invert(number):
    inverted_string = ""
    for char in number:
        if char == 0:
            inverted_string += "1"
        else:
            inverted_string += "0"
    inverted_string = addOne(inverted_string)
    while len(inverted_string) < 7:
        inverted_string = "0" + inverted_string
    if len(inverted_string) < 8:
        inverted_string = "1" + inverted_string
    return inverted_string
special_cases = [127, 64, 15, 1, 0, -1, -15, -64, -127, -128]
commands = set()
instructions = ("zero", "not", "and", "or", "add", "sub", "lt", "gt", "eq", "neq", "inv", "sll", "srl", "sla", "sra", "noop")
# instructions = ("sla", "None")

# Problemen bij:
# sla: -64, -1
# sra: -64, -15, -1, -128, -127 (alle negatieve getallen)
# inv: None
# neq: -128
# eq: -128
# gt: None
# lt: None
# sub: (-1, -128), ... (negatief getal, -128)
# add: None
# not: None
# zero: None




output = open("Test_Group50.txt", "w")
file_string = ""

for instruction in instructions:
    for first_number in special_cases:
        for second_number in special_cases:

                if instruction == "zero":
                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    operation_string += str(0) # The output is always zero
                    # There is never an overflow

                elif instruction == "not":
                    operation_string = ""
                    operation_string += instruction + " "
                    bin_first_number = bin(first_number)
                    if bin_first_number[0] != '-':
                        bin_first_number = extend(bin_first_number[2:])
                    else:
                        bin_first_number = invert(bin_first_number[3:])

                    bin_second_number = bin(second_number)
                    if bin_second_number[0] != '-':
                        bin_second_number = extend(bin_second_number[2:])
                    else:
                        bin_second_number = invert(bin_second_number[3:])
                    operation_string += bin_first_number + " "
                    operation_string += bin_second_number + " "

                    bin_number = bin_first_number
                    for char in bin_number:
                        if char == '1':
                            operation_string += '0'
                        else:
                            operation_string += '1'

                    operation_string += " "
                    # There is never an overflow
                elif instruction == "or":
                    continue
                elif instruction == "and":
                    continue
                elif instruction == "add":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number + second_number > 127 or first_number + second_number < -128:
                        operation_string += "0 1"
                    else:
                        operation_string += str(first_number + second_number) + " "

                elif instruction == "sub":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number - second_number > 127 or first_number - second_number < -128:
                        operation_string += "0 1"
                    else:
                        operation_string += str(first_number - second_number) + " "

                elif instruction == "lt":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number < second_number:
                        operation_string += "1"
                    else:
                        operation_string += "0"

                elif instruction == "gt":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number > second_number:
                        operation_string += "1"
                    else:
                        operation_string += "0"

                elif instruction == "eq":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number == second_number:
                        operation_string += "1"
                    else:
                        operation_string += "0"

                elif instruction == "neq":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number != second_number:
                        operation_string += "1"
                    else:
                        operation_string += "0"

                elif instruction == "inv":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number < -127:
                        operation_string += "0 1"
                    else:
                        operation_string += str(-1*first_number)


                elif instruction == "sla":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number * 2 > 127 or first_number*2 < -128:
                        operation_string += "0 1"
                    else:
                        operation_string += str(first_number*2) + " "

                elif instruction == "sra":

                    operation_string = ""
                    operation_string += instruction + " "
                    operation_string += str(first_number) + " "
                    operation_string += str(second_number) + " "
                    if first_number//2 > 127 or first_number//2 < -128:
                        operation_string += "0 1"
                    else:
                        operation_string += str(first_number//2) + " "


                else: continue

                if (operation_string + "\n" not in commands):
                    commands.add(operation_string + "\n")
                    file_string += operation_string + "\n"

output.write(file_string)
