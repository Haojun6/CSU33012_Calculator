import operations

OPERATORS = ('+','-','*')
DIGITS = ('1','2','3','4','5','6','7','8','9','0')
number_list = []   # a list to contain numbers calculated
operator_list = [] # a list to contain operators used

# check if the input is valid string
def is_valid(lst):
    for i in lst:
        if i not in OPERATORS and i not in DIGITS:
            return False
    return True

# main calc part
def calc(sequence):
    lst = list(sequence)
    number = ''
    for i in lst:
        # if is digit then put in digit list
        if is_digit(i):
            number = number + i
        # if is operator then put in operator list
        else:
            number_list.append(int(number))
            operator_list.append(i)
            # reset the tmp number
            number = ''
    number_list.append(int(number))
    # multiply as first priority
    mul()
    # add and sub as second priority in order
    add_sub()
    return number_list[0]

# calculate multiply operation, first priority
def mul():
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '*':
            product = operations.multiply(number_list[i],number_list[i + 1])
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, product)
            i-=1
        i+=1

# calculate add/sub operations, second priority
def add_sub():
    for i in range(1,number_list.__len__()):
        number1 = number_list[0]
        number2 = number_list[1]
        if operator_list[0] == '+':
            result = operations.add(number1,number2)
        elif operator_list[0] == '-':
            result = operations.subtract(number1,number2)
        operator_list.pop(0)
        number_list.pop(1)
        number_list[0] = result

# check if is a digit
def is_digit(digit):
    return digit in DIGITS

# main part to take in a mathematical expression and print answer
def main():
    sequence = input("Please enter a sequence that you want to compute: e.g.1+2-3*4")
    se_lst = list(sequence)
    if is_valid(se_lst):
        try:
            result = calc(sequence)
        except BaseException as e:
            print(e)
        else:
            print("The result is {0}.".format(result))
            return result
    else:
        print("Error:The sequence must only include operators and digits")


main()


