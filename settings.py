from addons.time import TimeAddon
from addons.weather import WeatherAddon

TimeAddon.config = dict(
  ntpServer = 'au.pool.ntp.org',
  interval = 15,
  topic = 'efm/time'
)

WeatherAddon.config = dict(
  openWeatherApiKey = '38bba49521d037c5dad46062dbe1008a',
  lat = -37.79616776238214,
  lon = 145.2922194203585,
  
  interval = 30,
  topic = 'efm/weather'
)

defaultMQTT = dict(
  host = 'localhost',
  port = 1883,
  username = '',
  password = '',
  mqttID = 'master'
)

dockerMQTT = dict(
  host = 'mqtt',
  port = 1883,
  username = '',
  password = '',
  mqttID = 'master'
)

MQTT_CONFIGURATION = dockerMQTT

ADDONS = [
  TimeAddon,
  WeatherAddon
]
