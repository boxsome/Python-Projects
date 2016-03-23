def fizz_buzz(n):
    for i in range(1, n+1) :
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i

if __name__ == "__main__":
    num = int(input("Please enter how many numbers you'd like to generate in fizz buzz sequence: "))
    print([str(x) for x in fizz_buzz(num)])
