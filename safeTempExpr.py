print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input().lower()
print('Enter the number of degrees:')
degrees = float(input())
if (scale == "f" and 100.4 >= degrees >= 60.8) or (scale == "c" and 38 >= degrees >= 16):
    print('Safe')
else:
    print('Dangerous')