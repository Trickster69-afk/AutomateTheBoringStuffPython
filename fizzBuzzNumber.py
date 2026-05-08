def main():
    num = int(input("Enter an integer: "))
    
    if fizz(num) and buzz(num): #if divisible by both 3 and 5
        print("Fizz Buzz")

    elif fizz(num): #if divisible by 3
        print("Fizz")

    elif buzz(num): #if divisible by 5
        print("Buzz")
 
    else:
        print(num)

def fizz(num):
    return num % 3 == 0

def buzz(num):
    return num % 5 == 0

if __name__ == "__main__":
    main()