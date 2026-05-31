import csv
import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get("https://pyvideo.org/speakers.html")
    response.encoding = "utf-8"
    markup = response.text
    soup = BeautifulSoup(markup, "html.parser")

    with open("speakers.csv", "w", encoding="utf-8", newline="") as file:
        headers = ["speaker", "talks"]
        writer = csv.DictWriter(file, delimiter=",", fieldnames=headers)

        writer.writeheader()
        for name in soup.find_all("li", class_="col-md-4"):
            badge = name.span.extract()
            writer.writerow({"speaker":name.get_text(strip=" "), "talks":badge.get_text()})

if __name__ == "__main__":
    main()