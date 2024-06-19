
def sum_of_digits(number):
    sum_digits = 0
    number = abs(number)
    
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of digits of {number} is {result}")
