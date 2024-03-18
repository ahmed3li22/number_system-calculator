# Ahmed Ali Ahmed(20230525)
# Malak Sabry Omar(20230531)
# ِAmir Fathy Hag (20230744)
def addition(binary_a, binary_b):
    # defining global variable to be used in the subtraction after calculating the two's complement. it will be used when dealing with the carry to know whether neglect it or calculate the twos complement again
    global maximum_length
    # finding maximum length to make the length of both strings equal and adding zeros in empty indices
    maximum_length = max(len(binary_a), len(binary_b))
    binary_a = binary_a.zfill(maximum_length)
    binary_b = binary_b.zfill(maximum_length)
    # declare empty string(result)
    result = ''
    carry = 0
    # looping and adding the binary numbers to result
    for i in range(maximum_length - 1, -1, -1):
        if int(binary_a[i]) + int(binary_b[i]) + carry == 0:
            result = '0' + result
            carry = 0
        elif int(binary_a[i]) + int(binary_b[i]) + carry == 1:
            result = '1' + result
            carry = 0
        elif int(binary_a[i]) + int(binary_b[i]) + carry == 2:
            result = '0' + result
            carry = 1
        elif int(binary_a[i]) + int(binary_b[i]) + carry == 3:
            result = '1' + result
            carry = 1
    # adding carry if it exists
    if carry == 1:
        result = '1' + result
    return result


def ones_complement(binary):
    result = ""
    # looping on the number and converting every 0 to 1 and doing the opposite
    for digit in binary:
        if digit == '0':
            result += '1'
        elif digit == '1':
            result += '0'
    return result


def twos_complement(binary):
    # calculate the twos complement by adding 1 to ones complement
    #if the number input is zero return zero at the end
    result = ""
    if binary == "1":
        result ="0"
        return result

    else:
        carry = 1

    # Iterate through each bit in reverse order
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == '0' and carry == 1:
            new_bit = '1'
            carry = 0
        elif binary[i] == '1' and carry == 0:
            new_bit = '1'
            carry = 0
        elif binary[i] == '0' and carry == 0:
            new_bit = '0'
            carry = 0
        elif binary[i] == '1' and carry == 1:
            new_bit = '0'
            carry = 1

        # Adding new bit to the final result
        result = new_bit + result

    # adding carry if it exists
    if carry == 1:
        result = '1' + result

    return result

#subtraction function
def subtraction(binary1,binary2):
    result=
# making sure the number is binary
def is_binary(binary):
    for digit in binary:
        if digit not in {'0', '1'}:
            return False
    return True


# continue asking the user to do the operation till he type anything
while True:
    print("Binary Calculator")
    print("A) Insert new numbers")
    print("B) Exit")

    first_choice = input("What do you want to do? ").upper()

    if first_choice == 'A':
        num1 = input("Enter the first binary number: ")
        # insure the number is binary
        while not is_binary(num1):
            num1 = input("Please insert a valid binary number: ")

        print("Please select the operation")
        print("A) Compute one's complement")
        print("B) Compute two's complement")
        print("C) Addition")
        print("D) Subtraction")

        operation_choice = input("").upper()

        if operation_choice == 'A':
            resultA = ones_complement(num1)
            print("One's complement of {} = {}".format(num1, resultA))

        elif operation_choice == 'B':
            resultB = twos_complement(ones_complement(num1))
            print("Two's complement of {} = {}".format(num1, resultB))

        elif operation_choice == 'C':
            num2 = input("Enter the second binary number: ")
            # insure the number is binary
            while not is_binary(num2):
                num2 = input("Please insert a valid binary number: ")
            resultC = addition(num1, num2)
            print("addition of {} and {} = {}".format(num1, num2, resultC))

        elif operation_choice == 'D':
            # subtraction can be calculated by adding the first number to the twos complement
            num2 = input("Enter the second binary number: ")
            # insure the number is binary
            while not is_binary(num2):
                num2 = input("Please insert a valid binary number: ")
            result_Of_Twos_Complment = addition(num1, twos_complement(ones_complement(num2)))
            #dealing with the carry at the end
            #if there is carry ignore it
            if len(result_Of_Twos_Complment) > maximum_length:
                resultD = result_Of_Twos_Complment[1:]
            #if there is no carry compute the twos complment again
            elif len(result_Of_Twos_Complment) == maximum_length:
                resultD = twos_complement(ones_complement(result_Of_Twos_Complment))
            print("Subtraction of {} and {} = {}".format(num1, num2, resultD))

        else:
            print("Invalid operation choice. Please select A, B, C, or D.")

    # exit if the user input B
    elif first_choice == 'B':
        print("Exiting Binary Calculator. Goodbye!")
        break
    # ask the user for avalid input
    else:
        print("Please select a valid choice.")