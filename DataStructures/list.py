num_list = list(range(5, 100))
print(num_list)


def fizbuzz(num):
    if((num % 3 == 0) and (num % 5 == 0)):
        return "FizzBuzz"
    elif(num % 3 == 0):
        return "Fizz"
    elif(num % 5 == 0):
        return "Buzz"
    else:
        return num


for num in num_list:
    print(num, " :In the Function Gives :", fizbuzz(num))
