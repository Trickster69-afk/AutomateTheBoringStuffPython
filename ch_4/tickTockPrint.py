import time

def main():
    sec = int(input("Enter seconds: "))
    tick_tock(sec)

def tick_tock(seconds):
    for i in range(1, seconds + 1):
        if i % 2 == 0:
            print("Tock...")
        else:
            print("Tick...")
        time.sleep(1)

if __name__ == "__main__":
    main()