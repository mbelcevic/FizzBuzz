def fizzbuzz(a,b):
    for i in range(a, b):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function to print the FizzBuzz sequence
fizzbuzz(1,50)
