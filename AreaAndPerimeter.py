#program to print area and perimeter of a rectagle from user inputted length and width
def main():
    while True:
        try:
            length = int(input("Length: ")) #accepts integer as length
            width = int(input("Width: ")) #accepts integer as breadth
            if length < 1 or width < 1:
                print("Please enter positive integers")
                continue
            print("Area:", area(length, width)) #prints area
            print("Perimeter:", perimeter(length, width)) #prints perimeter
            break
        except ValueError: #if user inputs value of any other data type except int
            print("Please enter integers")
            continue

def area(a, b): #calculates area
    return a * b

def perimeter(a, b): #calculates perimeter
    return 2 * (a + b)

if __name__ == "__main__":
    main()