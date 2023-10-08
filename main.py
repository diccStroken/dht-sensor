import adafruit_dht
import datetime
import time

from database import database
from gpiozero import LED

dht_device = adafruit_dht.DHT11(4)

white_led = LED(16)

def dht_loop():
    while True:
        try:
            humidity = int(dht_device.humidity)
            temperature = int(dht_device.temperature)

            print(f'Humidity: {humidity} %')
            print(f'Temperature: {temperature} ℃')

            dt = datetime.datetime.now()

            database.insert_dht(
                temperature = temperature,
                humidity = humidity,
                timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
            )

        except RuntimeError:
            print('Reading failed')

        time.sleep(5)

if __name__ == "__main__":
    try:
        white_led.on()

        dht_loop()

    except KeyboardInterrupt:
        pass

    finally:
        white_led.off()
        dht_device.exit()
