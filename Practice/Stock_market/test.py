import requests
from bs4 import BeautifulSoup

def make_request():
    code = input("Enter ticker code: ").upper()

    url = f"https://finance.yahoo.com/quote/{code}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-GB,en;q=0.9"
    }

    session = requests.Session()

    response = session.get(url, headers=headers)

    print("Status:", response.status_code)
    print("Final URL:", response.url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("title")

        if title:
            print(title.text)
        else:
            print("No title found")

    else:
        print(response.text[:500])


make_request()