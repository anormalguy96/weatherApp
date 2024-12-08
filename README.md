# Online Weather App

A simple graphical user interface (GUI) application to fetch and display current weather data for any city in the world. Built using **Python**, with libraries like `tkinter`, `geopy`, `timezonefinder`, and the **OpenWeather API**.

## Features
- Fetches real-time weather data for any city.
- Displays:
  - Temperature
  - Weather condition
  - Wind speed
  - Humidity
  - Atmospheric pressure
  - Weather description
- Provides the local time for the selected city.

---

## How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anormalguy96/OnlineWeatherApp.git
   cd OnlineWeatherApp
   ```

2. **Install Dependencies**
   - Install Python (if not already installed). The app works with Python 3.x.
   - Install required Python libraries using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Your API Key**
   - Obtain an API key from [OpenWeather](https://openweathermap.org/).
   - Save your API key securely:
     - **Option 1: Environment Variable**
       - Set your API key in your system's environment variables:
         ```bash
         export OPENWEATHER_API_KEY="your_api_key"  # macOS/Linux
         set OPENWEATHER_API_KEY=your_api_key      # Windows
         ```
     - **Option 2: `.env` File**
       - Create a file named `.env` in the project folder.
       - Add your API key:
         ```
         OPENWEATHER_API_KEY=your_api_key
         ```
       - Ensure your `.env` file is in `.gitignore` so it won't be pushed to GitHub.

4. **Run the Application**
   ```bash
   python WeatherApp.py
   ```

5. **Interact with the App**
   - Enter the name of a city in the search box.
   - Press Enter or click the search icon to fetch the weather data.

---

## Requirements
The app uses the following Python libraries:
- `tkinter` (Built-in for GUI)
- `geopy`
- `timezonefinder`
- `pytz`
- `requests`
- `Pillow`
- `python-dotenv` (if using `.env` for the API key)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
OnlineWeatherApp/
├── WeatherApp.py         # Main Python application
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
├── .env                  # Optional file for environment variables (ignored by Git)
├── assets/               # Images and icons used in the app
    ├── search_icon.png
    ├── weather_app_icon.png
    ├── blue_box.png
```

---

## Important Notes
- The API key used in the application should be kept private. Avoid hardcoding it in your scripts.
- Ensure you have internet access for the application to fetch weather data.

---

## Contribution
Feel free to fork this repository and submit pull requests for improvements or bug fixes!

---

## License
This project is licensed under the MIT License.
