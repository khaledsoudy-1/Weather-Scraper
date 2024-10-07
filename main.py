import requests
from bs4 import BeautifulSoup


def fetch_weather_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    # Make a GET request to the specified URL.
    response = requests.get(url, headers=headers, timeout=7)
    
    if response.status_code == 200:
        print(response.content)
        
    else:
        print(f"Something went wrong !!: {response.status_code}")


if __name__ == '__main__':
    page_url = "https://world-weather.info/"

    fetch_weather_page(page_url)
