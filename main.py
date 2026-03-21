# Task 1: API Integration and Data Visualization
# This script fetches weather data from OpenWeather API
# and visualizes temperature and humidity using matplotlib
import requests
import matplotlib.pyplot as plt

API_KEY = "ff85d0831e21ce0c27f2bfd4683e70a8"
CITY = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if 'list' not in data:
    print("Error:", data)
    exit()

temps = []
humidity = []
dates = []

for item in data['list'][:10]:
    temps.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])
    dates.append(item['dt_txt'])

# -------- DASHBOARD (2 graphs) --------
plt.figure(figsize=(12,6))

# Temperature graph
plt.subplot(2,1,1)
plt.plot(dates, temps, marker='o')
plt.title("Temperature Forecast")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity graph
plt.subplot(2,1,2)
plt.plot(dates, humidity, marker='o')
plt.title("Humidity Forecast")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

print("✅ Dashboard generated!")