
x = '3.979,63'
str_number = x.replace(',', '.').replace('.', '', 1)

# Convert the modified string to a float
float_number = float(str_number)
print(float_number)

def percentage(number):
    percentage = 2 / 100
    number1 = percentage * number
    number = number - number1
    print('num1', number1)
    print('num', number)


print(percentage(3980.05))