import csv



leadAcidBatterySize = 75 # in amp hours
energyStored = leadAcidBatterySize * 12.1 # average voltage from 100% to 50% * AH of battery
maxEnergyStored = energyStored # assuming battery starts with maximum energy
chargeControllerEfficiency = 0.95 # from data sheet
leadAcidChargingEfficiency = 0.85 # normal for lead acid batteries
extraOverhead = 1.05 # to account for extra loss from wires, solar panel nonidealities
systemLosses = chargeControllerEfficiency * leadAcidChargingEfficiency
timeUnit = 5 / 60 # 5 minutes, in hours

energyConsumed = 12.1 *  1 # tower consumes about 12.1 Watts

finalData = []
ifNeedsLargerBattery = 0
count = 0

with open('data.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        # calculate energy change over timeUnit period
        energyStored = energyStored + float(line[0]) * timeUnit * systemLosses / extraOverhead - energyConsumed * timeUnit

        # handle if battery is empty, full, or could be damaged
        if energyStored > maxEnergyStored:
            energyStored = maxEnergyStored
        if energyStored < 0:
            energyStored = 0
        finalData.append((energyStored / maxEnergyStored))
        count = count + 1
        if energyStored < (maxEnergyStored * 0.4): # check if this could damage battery
            ifNeedsLargerBattery = 1

with open('finalData.csv', 'w', newline='\n') as dataFile:
    writer = csv.writer(dataFile)
    for dat in finalData:
        row = []
        row.append(dat)
        writer.writerow(row)

if ifNeedsLargerBattery == 1:
    print('Larger battery required')
else:
    print('Battery is sufficient')

print('Wrote ')
print(count)
print(' data points')
