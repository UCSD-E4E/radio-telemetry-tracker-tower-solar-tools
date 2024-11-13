def plot_data(time_arr, wh_capacity, w_sunlight, num_points_per_day):
	import numpy as np
	import matplotlib.pyplot as plt
	time_arr_days = []
	for idx in range(len(time_arr)):
		time_arr_days.append(time_arr[idx] / 24.0)
	x_time = np.array(time_arr_days)
	y_pow_abs = np.array(wh_capacity)
	y_ene_sl = np.array(w_sunlight)
	plt.plot(x_time, y_pow_abs, label='Energy Stored')
	ax = plt.gca()
	ax2 = ax.twinx()
	ax2.plot(x_time, y_ene_sl, color='red', label='Solar Radiation')
	    	
	# plot 6 days around when battery is at lowest power
	if len(wh_capacity) > num_points_per_day * 6: 
		min_idx = wh_capacity.index(min(wh_capacity))
	if min_idx > (num_points_per_day*3) and min_idx < (len(wh_capacity) - (num_points_per_day*3)):
		ax.set_xlim([time_arr_days[min_idx-(num_points_per_day*3)], time_arr_days[min_idx+(num_points_per_day*3)]])
	elif min_idx < (num_points_per_day*3):
		ax.set_xlim([0, num_points_per_day])
	elif min_idx < (len(wh_capacity) - (num_points_per_day*3)):
		ax.set_xlim([len(wh_capacity) - (num_points_per_day+1), len(wh_capacity) - 1])
	ax.set_xlabel('Time (Days since first data point)')
	ax.set_ylabel('Battery Capacity (WH)') 
	ax2.set_ylabel('Solar Radiation Over Panels (W)')
	lines, labels = ax.get_legend_handles_labels()
	lines2, labels2 = ax2.get_legend_handles_labels()
	ax2.legend(lines + lines2, labels + labels2, loc=0)
	plt.title('Battery Capacity Over Time') 
	plt.show()
    

def setup_csv(setup_file_path):
	import json
	setup_file = open(setup_file_path)
	setup_data = json.load(setup_file)
	date_col = setup_data["date_col"] # date is stored as 2020-01-01 20:15:16
	temp_col = setup_data["temp_col"] # temperature stored as integer in F
	sunl_col = setup_data["sunl_col"] # sunlight is stored as integer in W/m^2
	number_of_panels = setup_data["num_panels"]
	file_name = setup_data["data_file"].strip()
	num_points_per_day = setup_data["points_per_day"]
	return date_col, temp_col, sunl_col, number_of_panels, file_name, num_points_per_day
   
def plot_current(setup_file_path):
	import csv
	import numpy as np
	import matplotlib.pyplot as plt
	time_arr_ms = []
	current = []
	with open(setup_file_path, mode = 'r', encoding='utf-8') as file:
		csvFile = csv.reader(file)
		for line in csvFile:
			current.insert(0, line[1])
	
	for idx in range(len(current)):
		time_arr_ms.insert(0, idx)
	plt.plot(time_arr_ms, current, label='current')
	plt.show()
    
def get_average_startup_current():
	import csv
	from pathlib import Path
	setup_file_path = Path("./current_startup.csv")
	time_arr_ms = []
	current = []
	average = 0;
	with open(setup_file_path, mode = 'r', encoding='utf-8') as file:
		csvFile = csv.reader(file)
		for line in csvFile:
			current.insert(len(current), line[1])
	
	for idx in range(60*1000): #takes approximately 1 minute to startup, can be seen by using the plot current function
		if(idx > 0):
			average = average + 1/60/1000 * float(current[idx]) / 100 # 1/60/1000 is timestep, current[idx]/100 converts from mv (measured from current clamp) to amps
	
	return average
	
def get_average_expected_behavior():
	import csv
	from pathlib import Path
	setup_file_path = Path("./current_average_operation.csv")
	time_arr_ms = []
	current = []
	average = 0;
	with open(setup_file_path, mode = 'r', encoding='utf-8') as file:
		csvFile = csv.reader(file)
		for line in csvFile:
			current.insert(len(current), line[1])
	
	for idx in range(len(current)): 
		if(idx > 0):	
			average = average + 1/len(current) * float(current[idx]) / 100
	
	return average
