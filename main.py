from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()-590
    hum = sensor.humidity() - 1600
    print('Temperature: %f C' %temp)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')