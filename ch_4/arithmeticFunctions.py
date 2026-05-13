def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(f"Sum: {add(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")

#Add function
def add(num1, num2 = 0):
    total_sum = num1
    for i in range(num2):
        total_sum = plus_one(total_sum)
    return total_sum

#Calls the add function num2 - 1 times
def multiply(num1, num2):
    product = num1
    for i in range(num2 - 1):
        product = product + add(num1)
    return product

#unit addition
def plus_one(n):
    return n + 1

if __name__ == "__main__":
    main()