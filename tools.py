import math
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests


geolocator = Nominatim(user_agent="time-bot")
tz_finder = TimezoneFinder()

def calculator_tool(expression: str) -> str:
    try:
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")} # a whitelist of allowed functions from math

        result = eval(expression, {"__builtins__": {}}, allowed_names) #Executes expression securely

        return f"Result: {result}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


def get_current_time_by_city(city_or_timezone: str = "UTC") -> str:
    try:
        try:
            tz = pytz.timezone(city_or_timezone)
        except:
            # If not valid timezone, treat it as a city name
            location = geolocator.geocode(city_or_timezone)
            if not location:
                raise ValueError("Invalid city or location name.")

            lat, lon = location.latitude, location.longitude
            tz_name = tz_finder.timezone_at(lat=lat, lng=lon)
            if not tz_name:
                raise ValueError("Timezone not found for location.")

            tz = pytz.timezone(tz_name)

        now = datetime.now(tz)
        return f"🕒 Current time in {city_or_timezone}: {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
    





def web_search(query: str, num_results: int = 3) -> str:
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
        response = requests.get(url)
        data = response.json()

        results = data.get("RelatedTopics", [])
        if not results:
            return "❌ No search results found."

        formatted_results = []
        count = 0

        for item in results:
            if "Text" in item and "FirstURL" in item:
                title = item["Text"]
                url = item["FirstURL"]
                formatted_results.append(f"🔹 {title}\n🔗 {url}")
                count += 1
                if count >= num_results:
                    break

        return "\n\n".join(formatted_results) if formatted_results else "❌ No results found."

    except Exception as e:
        return f"❌ Search failed: {str(e)}"