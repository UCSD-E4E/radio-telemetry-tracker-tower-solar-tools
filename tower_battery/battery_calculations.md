# RCT Battery System Calculations

All 5V components will be divided by 0.8 to account for efficiency. For 3.3V components, they will be divided by 0.73.  
  
#### Individual power:   
upc817xg-d04-5: 200mW x2  
Upcore: 1.6A * 5V = 8W  
GPS: 74mA * 5V = 370mW  
Sik Radio: 100mA * 5V = 500mW  
USRP B200mini: attached to upcore during testing  
LNA: 80mA * 5V = 400mW  
Magnetometer:   


#### Converter Adjusted power:
5V: (8W + 370mW + 500mW + 400mW) / 0.8 = 11.58875 W  
3.3V: 400mW / 0.73 = 0.548 W  
Total: 12.13675 W  
WH: 12.13675 * 48 = 582.564 WH  
AH: 582.564 / 12V * 1.1 = 53.402 AH  
x1.1 is included to give extra overhead.  
  
Possible [battery](https://www.weizeus.com/collections/sealed-lead-acid-batteries/products/12v-55ah-deep-cycle-battery-ub12550-for-power-scooter-wheelchair-mobility-emergency-ups-system-trolling-motor) that meets criteria


