special_cases = [127, 64, 15, 1, 0, -1, -15, -64, -127, -128]

instructions = ("zero", "not", "and", "or", "add", "sub", "lt", "gt", "eq", "neq", "inv", "sll", "srl", "sla", "sra", "noop")

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
                        bin_first_number = bin_first_number[2:]
                    else:
                        bin_first_number = bin_first_number[3:] # TODO: fix, this number should be made negative

                    bin_second_number = bin(second_number)
                    if bin_second_number[0] != '-':
                        bin_second_number = bin_second_number[2:]
                    else:
                        bin_second_number = bin_second_number[3:]  # TODO: fix, this number should be made negative

                    operation_string += bin_first_number + " "
                    operation_string += bin_second_number + " "

                    bin_number = bin(first_number)
                    for char in bin_number:
                        if char == '1':
                            operation_string += '0'
                        else:
                            operation_string += '1'

                    operation_string += " "
                    # There is never an overflow
                else: continue

                file_string += operation_string + "\n"

print(bin(-2))

output.write(file_string)
