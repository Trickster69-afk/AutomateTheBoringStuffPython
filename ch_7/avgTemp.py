import random

def main():
    list_weather = [] #list of weather dicts
    for i in range(100):
        list_weather.append(get_random_weather())

    print("Average Temperature:", get_average_temperature(list_weather))
    print(list_weather)

def get_random_weather():
    weather = {}
    temp = random.uniform(-50, 50)
    feels_like = random.uniform(temp-10, temp+10)
    humidity = random.randint(0, 100)
    pressure = random.randint(990, 1010)

    weather.update({"temp":round(temp, ndigits=2) , "feels_like":round(feels_like, 2), "humidity":humidity, "pressure":pressure})

    return weather

def get_average_temperature(weather_data): #calculates average temperature from the list of dicts
    tot_temp = 0
    l = len(weather_data)
    for i in range(l):
        tot_temp = tot_temp + weather_data[i]["temp"]
    return float(round(tot_temp/l, 2))

if __name__ == "__main__":
    main()