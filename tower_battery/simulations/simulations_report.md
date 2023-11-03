<h1>Summary</h1>
When swapping out the batteries, there will be a short period of time when the new and old batteries are in parallel. This isdangerous because of the lower the %charge of a deep cycle battery, the lower the voltage of the battery, which could lead to a 2 volt difference between the batteries, which would create a short. To avoid this, diodes can be used, along with optional switches.

<h1>Model for Simulation</h1>
For these simulations, the RCT can be modelled as only the battery system and the DC-DC converters. This is because the 12V batteries are connected to 3 things in the actual schematic, the converters, a fuse, and a switch, while all other voltage sources are the DC-DC converters. If the current is not too high, which it shouldn't be in normal operation, the fuse will act as a very weak resistor, which is has such a small impact that it can be ignored. The switch was also ignored, as when the tower is on, the switch should act as an open circuit, meaning it does about as much as the fuse. This only leaves the DC-DC convertes.

DC-DC converters were modelled as 3A current source, which is based off of the maximum fuse current calculated by Aniket. Any higher voltage than this and the fuse would melt, meaning no more than 3A current can be drawn. The batteries were modelled as voltage sources which would decrease until around 50%, which is where you want to stop discharging deep cycle batteries to avoid damaging them. In the simulation, the discharge linearly, when in reality, they would discharge similarly to the graph below, but this should not effect the simulations at all.
![lead_acid_voltage_chart](Voltage_chart_lead_acid.PNG)

The simulation assumes that battery is running for 2 days (the max amount of time this needs to be powered), dropping by around 1 volt at around 50% charge, before being swapped. At 176800k seconds (the number of seconds in 2 days), the right (recently charged) battery is placed in parallel, and then shortly afterwards switch connecting the two is turned on. There is around 1000 seconds when both batteries are running, in parallel, which is meant to simulate the time between taking out the old battery and butting in the new. 1000 seconds is incredibly unrealistic, as swapping batteries will take less than a minute, but this is to see if leakage current into the old battery will be significant as time goes on. After this, the left switch is turned off, meaning only the new/right battery is supply power, so the left/old battery can be removed. Below is a graph of the voltages and currents during the switching period. -I(S1) is the left/old battery's current, -I(S2) is the right/new battery's current.
![overall_behavior](overall_behavior_high_temp.PNG)

<h1>Simulation Results</h1>
Simulation shows that leakage current of these diodes is very good, as there was only a leakage of 114uA during the 1000 seconds they were in parallel. Actual battery chargers charge at a rate of around 2 to 10 amps, so this is well under this range. Diodes that were used were RB238T-40NZ schottky diodes, which I recommend using these diodes for final design. 

![leakage current](high_temperature_switching_current.PNG)

<n></n>

There is an inrush current spike that occurs at the moment when the second diode turns on which is important to note. About 1.2A of current will briefly flow into the diode for around 0.5 seconds, however, this additionally current is brief enough and small enough that it should still be safe.

![inrush current](inrush_current_diode.PNG)

<h1>Thermal Issues</h1>
The information below is just a brief overview of heatsinks, although electrical enclosures will also have to be used. To avoid the high temperatures of the diode melting the plastic wire connectors or the 12 AWG cable, a heat sink is needed for the diode. I recommend [this one](https://www.cuidevices.com/product/resource/hss-b20-np-12.pdf) , as it is quite cheap and is able to absorb quite a lot of heat. It also is very easy to attach to the diode, as it just requires a screw. The temperature of the diode needs to be under 100 C to avoid damaging any plastic connectors. The calculation for temperature of a semiconductor is T = Tair + P * ($\theta$jc + $\theta$cs + $\theta$sa), where theta is the thermal resistance of the diode in degrees Celcius/Watts (and the subscripts mean junction to case, case to sink, and sink to air respectively). Power consumed is equal to Vf * I = 0.8 * 3 = 2.4 W at peak current and diode voltage drop. $\theta$ jc is already given, which is 2 C/W. The value of $\theta$cs is not given, but it is typically between 0.5 to 2 C/W depending on the structure of the heat sink, so we can just estimate it as 2 C/W. Finally, the value of $\theta$sa is not given directly, but instead there is a graph in the datasheet of how much the temperature will increase because of the sink based off the wattage, which is at around 31 C. Therefore, the final temperature is 31 + 2.4 * (2 + 2) + Tair = 40.6 + Tair, meaning that as long as the temperature air around the battery doesn't reach 59.4 C, nothing will melt. Outside of death valley, the heating should not be an issue. In the case the tower had to be deployed somewhere very hot, or the conditions of where its placed result in much higher heats, a small fan can be used, which could further lower the temperature, as can be seen in the heat sink's data sheet.

<h1>Alternative battery chemistries</h1>

 - NiMH: Low energy storage, most of these batteries do not go above 20AH, would be very expensive to use many batteries in parallel. 

 - Litium Ion: Very expensive, can be dangerous if allowed to overheat, aside from this is a viable alternative, but considering diode heating issues, not the best option.

 - LiCoO2: Short lifespan, low thermal stability, not a good fit.

 - LiFePO4: Same weight as lead acid batteries (about 20 pounds for at least 33 hours), no issues with needing to be at above 50% charge. Has a more significant voltage change as the battery discharges (4V difference between 100% and 0%), but this should still not be dangerous with diodes. Best option other than lead acid batteries.

 - LiNiMnCoO2:Does not have both high energy storage and high energy output, might be difficult to find a good fitting battery of this kind.
