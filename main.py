import irsdk
import math

ir = irsdk.IRSDK()
ir.startup()

starting_tank = True

fuel_level_start = ir['FuelLevel']
print(fuel_level_start)

laps_left_start = ir['SessionLapsRemain']
previous_lap_completed = ir['Lap']
print (previous_lap_completed)

driver_info = ir['DriverInfo']
max_fuel_liters = driver_info.get('DriverCarFuelMaxLtr')

totel_fuel_used = 0
print("Started")
while True:

    laps_completed =ir['Lap']
    if ir['FuelLevel'] > 1 and starting_tank:
        fuel_level_start = ir['FuelLevel']
        starting_tank = False

    #print(fuel_level_start)
    

    #print (laps_completed)

    if laps_completed != previous_lap_completed:
        print (f"lap {laps_completed} started")
        previous_lap_completed = laps_completed

        fuel_level = ir['FuelLevel']
        print(f"Fuel level at {fuel_level_start}L")

        current_laps_left = ir['SessionLapsRemain']

        if previous_lap_completed >= 2:
            print(f"{fuel_level_start} - {fuel_level}")
            fuel_used = float(fuel_level_start-fuel_level)
            print(f"{fuel_used} / {laps_completed}")

            average_per_lap = fuel_used/(laps_completed - 1)
            print(average_per_lap)
            fuel_remaining_laps = fuel_level/average_per_lap

            fuel_needed_to_finish = fuel_level/current_laps_left
            fuel_needed_in_pits = max_fuel_liters-fuel_needed_to_finish

            if fuel_needed_in_pits > max_fuel_liters:
                fuel_needed_in_pits = max_fuel_liters

            elif fuel_needed_in_pits < 0:
                actual_pit_stops_needed = 0

            actual_pit_stops_needed = fuel_needed_to_finish/max_fuel_liters
            pit_stops_needed = math.ceil(actual_pit_stops_needed)

            print(f"Fuel consumed on lap {laps_completed}: {fuel_used}  |   The average usage is {average_per_lap}")
            print(f"The fuel per lap needed to finish the race is {fuel_needed_to_finish}   |   You will need to fill up with {fuel_needed_in_pits}L in the pits")
            print(f"You will have to do {pit_stops_needed} pitstops to finish this race   |   There are {fuel_remaining_laps} laps left of fuel")



    