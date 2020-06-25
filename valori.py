import time
from bme280 import BME280
from enviroplus import gas

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
    
print(""" Esperimento - Temperatura, pressione, umidità, RED, OX e NH3

Press Ctrl+C to exit!

""")

bus=SMBus(1)
bme280 = BME280(i2c_dev=bus)

t=open('temperature.txt', 'w')
p=open('pressione.txt', 'w')
h=open('umidita.txt', 'w')
g=open('gas.txt','w')

t.close()
p.close()
h.close()
g.close()

try:
    while True:
        t=open('temperature.txt', 'a')
        p=open('pressione.txt', 'a')
        h=open('umidita.txt', 'a')
        g=open('gas.txt', 'a')
        
        t.writelines(str(bme280.get_temperature())+"\n")
        p.writelines(str(bme280.get_pressure())+"\n")
        h.writelines(str(bme280.get_humidity())+"\n")
        g.writelines(str(gas.read_all()))
        
        t.close()
        p.close()
        h.close()
        g.close()
        
        time.sleep(1)
        
except KeyboardInterrupt:
        t.close()
        p.close()
        h.close()
        g.close()