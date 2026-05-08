print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input().lower()
print('Enter the number of degrees:')
degrees = float(input())
if scale == 'c':
    if degrees >= 16 or degrees <= 38:
        print('Safe')
    else:
        print('Dangerous')
elif scale == 'f':
    if degrees >= 60.8 and degrees <= 100.4:
        print('Safe')
    else:
        print('Dangerous')