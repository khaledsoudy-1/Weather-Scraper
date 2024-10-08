import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
from datetime import date
import json


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
    
    data = [list(item) for item in zip(city_names, temps, conditions)]
    return data


def get_today_date():
    today = date.today()
    
    return today.strftime("%B %d, %Y")


def save_to_txt_table(data):
    if not data:
        print("No data to save!")
        return
    
    headers = ["City", "Temperature (℃)", "Condition"]
    colalign = ["left", "center", "left"]
    table = tabulate(data, headers=headers, tablefmt="fancy_grid", colalign=colalign)
    
    with open('weather.txt', 'w', encoding='utf-8') as f:
        divider = "=" * 40
        f.write(f"{divider}\n")
        f.write(f"       Popular Cities Forecast\n")
        f.write(f"{divider}\n\n")
        f.write(f"Date: {get_today_date()}\n\n")
        f.write(f"{table}\n")


def save_to_json(data):
    if not data:
        print("No data to save!")
        return
    
    cities = [{"city": city, "temp": temp, "condition": condition} for city, temp, condition in data]
    
    json_data = {
        "Title": "Popular Cities Forecast",
        "Date": get_today_date(),
        "Cities": cities
    }
    
    with open('weather.json', 'w') as f:
        json.dump(json_data, f, indent=3, ensure_ascii=False)


def weather_scraper():
    page_url = "https://world-weather.info/"
    
    # Fetch weather page content
    weather_html_content = fetch_weather_page(page_url)
    
    # Check if page content was fetched successfully
    if weather_html_content:
        # get the weather data
        weather_data = extract_weather_data(weather_html_content)
        
        # Save the weather data to a text file
        save_to_txt_table(weather_data)
        
        # Save the weather data to a JSON file
        save_to_json(weather_data)


if __name__ == '__main__':
    weather_scraper()
