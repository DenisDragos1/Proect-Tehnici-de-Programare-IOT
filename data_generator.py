import json
import time
import random
import requests

SERVER_URL = "https://proect-tehnici-de-programare-iot.onrender.com/update-data"

def generate_sensor_data():
    data = {
        "temperature": round(random.uniform(15, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "soil_ph": round(random.uniform(5.5, 7.5), 2),
        "nitrogen_level": round(random.uniform(10, 50), 2),
        "air_humidity": round(random.uniform(30, 60), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

def main():
    while True:
        sensor_data = generate_sensor_data()
        try:
            response = requests.post(SERVER_URL, json=sensor_data)
            print(f"Sent data: {sensor_data}, Response: {response.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")
        time.sleep(60)

if __name__ == "__main__":
    main()
