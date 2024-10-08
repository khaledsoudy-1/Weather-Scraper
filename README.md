# 🌡️ Weather Scraper
## 📖 Description
A robust Python web scraper that collects real-time weather data from world-weather.info for popular cities worldwide. The program presents the data in both a beautifully formatted text table and a structured JSON format, making it perfect for both human reading and data processing.

## ✨ Features
- Real-time weather data scraping
- Temperature data in Celsius
- Weather conditions for each city
- Dual output formats:
  - Formatted text table (.txt)
  - Structured JSON (.json)
- Automatic date stamping
- Robust error handling
- Clean and organized output

## 🚀 How to Use
1. **Set up your environment**:  
   Make sure you have Python installed on your system.

2. **Install dependencies**:  
   Run the following command to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scraper**:  
   Execute the script:
   ```bash
   python main.py
   ```
   The script will automatically:
   - Fetch the latest weather data
   - Generate a formatted text file (weather.txt)
   - Generate a JSON file (weather.json)

## 📊 Example Output

### Text File (weather.txt)
```
========================================
       Popular Cities Forecast
========================================

Date: October 8, 2024

╒════════════════╤══════════════════╤═══════════════════╕
│ City           │ Temperature (℃)  │ Condition         │
╞════════════════╪══════════════════╪═══════════════════╡
│ London         │       15         │ Partly cloudy     │
├────────────────┼──────────────────┼───────────────────┤
│ Paris          │       17         │ Mostly sunny      │
├────────────────┼──────────────────┼───────────────────┤
│ New York       │       21         │ Clear sky         │
├────────────────┼──────────────────┼───────────────────┤
│ Tokyo          │       19         │ Light rain        │
╘════════════════╧══════════════════╧═══════════════════╛
```

### JSON File (weather.json)
```json
{
   "Title": "Popular Cities Forecast",
   "Date": "October 8, 2024",
   "Cities": [
      {
         "city": "London",
         "temp": 15,
         "condition": "Partly cloudy"
      },
      {
         "city": "Paris",
         "temp": 17,
         "condition": "Mostly sunny"
      },
      {
         "city": "New York",
         "temp": 21,
         "condition": "Clear sky"
      },
      {
         "city": "Tokyo",
         "temp": 19,
         "condition": "Light rain"
      }
   ]
}
```

## 💻 Code Highlights
### Weather Data Extraction
```python
def extract_weather_data(html_content):
    """Extracts weather data from the provided HTML content."""
    soup = BeautifulSoup(html_content, 'lxml')
    weather_table = soup.find('div', id='resorts')
    cities = weather_table.select('div.resorts-blocks > div > a')
    city_names = [city.text for city in cities]
    # ... more extraction logic
```

## 🛠️ Potential Enhancements
- Add command-line arguments for custom output file names
- Implement temperature unit conversion (Celsius/Fahrenheit)
- Add historical data tracking
- Create a simple web interface using Flask
- Add data visualization capabilities
- Implement scheduled scraping at regular intervals
- Add more detailed weather information (humidity, wind speed, etc.)

## 👨‍💻 Author
Khaled Soudy

## 📦 Dependencies
The project relies on the following Python packages:
- beautifulsoup4==4.12.3
- requests==2.32.3
- lxml==5.3.0
- tabulate==0.9.0
- And other supporting packages listed in `requirements.txt`

## 🧱 Project Structure
```
weather-scraper/
├── main.py          # Main script with scraping logic
├── requirements.txt # Project dependencies
├── .gitignore      # Git ignore file
└── README.md       # Project documentation
```

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

## 📄 License
This project is open source and available under the MIT License.

## ⚠️ Disclaimer
Please ensure you follow the target website's robots.txt and terms of service when using this scraper. Be respectful of the website's resources and implement appropriate delays between requests if needed.

## 📞 Support
If you encounter any issues or have questions, please open an issue in the GitHub repository.

---
Stay informed about weather conditions worldwide! 🌍🌤️