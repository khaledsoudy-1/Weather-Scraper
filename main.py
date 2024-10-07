import requests
from bs4 import BeautifulSoup
import re


def fetch_weather_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Cookie': 'celsius=1'
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


def extract_weather_data(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Create an object for the target weather data
    weather_table = soup.find('div', id='resorts')
    
    # Extract city names
    cities = weather_table.select('div.resorts-blocks > div > a')
    city_names = [city.text for city in cities]
    
    # Extract weather temperatures (in Celsius °C)
    temp_pattern = re.compile(r"<span>([+|-]\d+)<span\sclass")
    temp_matches = re.findall(temp_pattern, str(weather_table))
    temps = [int(temp) for temp in temp_matches]
    
    # Extract weather condition description
    weather_conditions = weather_table.select('span.tooltip')
    conditions = [condition['title'] for condition in weather_conditions]
    
    data = zip(city_names, temps, conditions)
    return data


if __name__ == '__main__':
    page_url = "https://world-weather.info/"
    
    # Fetch weather page content
    weather_html_content = fetch_weather_page(page_url)
    
    # Check if page content was fetched successfully
    if weather_html_content:
        # get the weather data
        weather_data = extract_weather_data(weather_html_content)