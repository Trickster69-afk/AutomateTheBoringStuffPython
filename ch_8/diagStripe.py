import time

def main():
    flag_zero = 0
    flag_dot = 50

    while True:
        for i in range(50): #first half 
            print("0" * flag_zero + "." * flag_dot)
            flag_dot -= 1  
            flag_zero += 1
            if flag_zero == 50: flag_zero = 49 
            if flag_dot == 0: flag_dot = 1
            time.sleep(0.0095)

        for i in range(49): #second half
            print("." * flag_dot + "0" * flag_zero)
            flag_zero -= 1
            flag_dot += 1
            if flag_dot == 50: flag_dot = 50
            if flag_zero == 0: flag_zero = 0
            time.sleep(0.0095)

if __name__ == "__main__":
    main()