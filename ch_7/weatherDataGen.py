import random

def main():
    list_weather = [] #list of weather dicts
    for i in range(100):
        list_weather.append(get_random_weather())
    
    print(list_weather)

def get_random_weather():
    weather = {}
    temp = random.uniform(-50, 50)
    feels_like = random.uniform(temp-10, temp+10)
    humidity = random.randint(0, 100)
    pressure = random.randint(990, 1010)

    weather.update({"Temp":round(temp, ndigits=2) , "feels_like":round(feels_like, 2), "humidity":humidity, "pressure":pressure})

    return weather

if __name__ == "__main__":
    main()