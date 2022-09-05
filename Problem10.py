num1 = '50'
num2 = '62'

# check and print type num variable
print(type(num1))
print(type(num2))

# convert the num into string
converted_num1 = int(num1)
converted_num2 = int(num2)

# print type of converted_num
print(type(converted_num1))
print(type(converted_num2))

additionOfNum = converted_num1+converted_num2
subtractionOfNum = converted_num1 - converted_num2
multiplicationOfNum = converted_num1 * converted_num2
devisionOfNum = converted_num1 / converted_num2

print("The addition Of Number : ", additionOfNum)
print("The subtraction Of Number : ", subtractionOfNum)
print("The multiplication Of Number : ", multiplicationOfNum)
print("The division Of Number : ", devisionOfNum)
