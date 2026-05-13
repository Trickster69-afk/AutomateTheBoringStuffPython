import sys

def main():
    while True:
        try:
            width = int(input("Enter: "))
            if width < 1: #non positive
                print("Please enter a positive number")
                continue
            for i in range(5):
                print("O" * width)
            break
        except ValueError:
            print("Please enter an integer")
            continue
        except KeyboardInterrupt:
            sys.exit("\nHope you had fun!")

if __name__ == "__main__":
    main()