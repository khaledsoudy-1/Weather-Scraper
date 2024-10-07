import requests
from bs4 import BeautifulSoup


def fetch_weather_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    try:
        # Make a GET request to the specified URL.
        response = requests.get(url, headers=headers, timeout=7)
        response.raise_for_status()  # Raises an error for non-successful requests
        return response.content  # Return html page content
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.ConnectionError as connect_err:
        print(f"Connection error occurred. {connect_err}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    return None


if __name__ == '__main__':
    page_url = "https://world-weather.info/"
    
    fetch_weather_page(page_url)
