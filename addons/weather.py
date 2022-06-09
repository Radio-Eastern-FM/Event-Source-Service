import json
import urllib

from addons.addon import Addon

class WeatherAddon(Addon):
  @staticmethod
  def update():
    # Get weather from openweathermap
    secret = WeatherAddon.config['openWeatherApiKey']
    lat = WeatherAddon.config['lat']
    lon = WeatherAddon.config['lon']
    weatherURL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&APPID={secret}&exclude=hourly,minutely"
    
    try:
      with urllib.request.urlopen(weatherURL) as url:
        # Parse response
        data = json.loads(url.read().decode())
        # Publish to MQTT
        return json.dumps(data)
    except Exception as e:
      print("[weather] Error with API: ", e)
