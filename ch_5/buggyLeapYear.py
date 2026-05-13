def is_leap_year(year):
    if year % 4 == 0 and not year % 100 == 0:
        return True
    elif year % 100 == 0 and year % 4 == 0:
        if year % 400 == 0:
            return True
        return False
    return False

def main():
    while True:
        print('Enter a year or "done":')
        response = input()
        if response == 'done':
            break
        print('Is leap year:', is_leap_year(int(response)))

if __name__ == "__main__":
    main()