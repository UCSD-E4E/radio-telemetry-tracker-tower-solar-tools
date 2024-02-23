# RCT Battery System Calculations

All 5V components will be divided by 0.8 to account for converter efficiency. For 3.3V components, they will be divided by 0.73.
Numbers were provided from the data sheets for the converters.

#### Individual power: 
upc817xg-d04-5: 200mW x2
Upcore: 1.6A * 5V = 8W 
GPS/Magnetometer: ~50mA * 5V = 250mW
Sik Radio: 100mA * 5V = 500mW
USRP B200mini: attached to upcore during testing
LNA: 80mA * 5V = 400mW


#### Converter Adjusted power:
5V: (8W + 250mW + 500mW + 400mW) / 0.8 = 11.4375 W
3.3V: 400mW / 0.73 = 0.548 W
Total: 11.9855 W
WH: 11.9855 * 48 = 575.304 WH
AH: 582.564 / 12V = 47.942
Adjusting for lead acid battery, we need around twice the capacity to avoid damaging the battery.
Lead acid battery target: 96 AH
Lithium battery target: 48 AH

Possible Batteries that can be used:
    - [LiFePO4](https://www.btrpower.com/products/12v-50ah-lifepo4-battery-for-rv-solar-system-trolling-motor?_pos=2&_psq=50AH&_ss=e&_v=1.0)
    - [other LiFePO4](https://ipowerqueen.com/products/12-8v-50ah-life-po4-battery)
    - [Lead acid](https://www.amazon.com/100Ah-Sealed-Battery-UB121000-Group/dp/B00BMUDOLE)

Cost is around $200 per battery
