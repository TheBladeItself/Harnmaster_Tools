#===================
# Imports
#===================

import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter import scrolledtext

def dice(number_of_dice, mod=0, sides=6):
	x = 0
	for i in range(0,number_of_dice):
		t = randint(1,sides)
		x += t
	x += mod
	return x
	
# Create Instance
win = tk.Tk()

# Add a title
win.title("Hârnmaster Tools GUI")
win.resizable(False, False)

tabControl = ttk.Notebook(win)					# Create tab control
tab1 = ttk.Frame(tabControl)					# Create a tab
tabControl.add(tab1, text='Weather Generation')	# Add to the tab

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Random Event Generation')

tabControl.pack(expand=1, fill='both')			# Pack to make visible

def wind_gen(value):
	wind = dice(1, sides=10)
	if value == 0:
		if wind < 5: wind_speed = 0
		elif wind > 8: wind_speed = 2
		else: wind_speed = 1
	elif value == 1:
		if wind < 6: wind_speed = 1
		elif wind > 8: wind_speed = 3
		else: wind_speed = 2
	else:
		if wind < 7: wind_speed = 2
		elif wind == 10: wind_speed = 4
		else: wind_speed = 3
	return wind_speed

def weather_gen():
	syssc.delete('1.0', tk.END)
	c = clim_t.get()		# Climate
	s = seas_t.get()		# Season
	w = int(n_watc.get())	# No. Watches
	i = int(s_weat.get())	# Starting Weather
	
	if i < 1: current_weather = dice(1, sides=20)
	else: current_weather = i
			
	count = 0
	while count < w:
		count += 1
		if c == 'Subpolar':
			if s == 'Spring':
				we = ['x',4,1,0,1,4,2,0,0,0,8,1,6,2,6,2,0,6,2,0,1]
				dt = ['x',1,2,3,3,2,1,1,2,1,0,1,2,3,4,3,2,2,2,1,1] # day temperature
				nt = ['x',1,2,2,3,2,1,0,2,1,0,0,0,2,3,3,1,2,2,1,1] # night temperature
				wi = ['x',1,1,0,1,2,2,2,1,1,0,1,1,0,0,0,0,2,2,2,1]
				wd = ['','N','NE','SE','SW','NW','NW','SW','SW','NW','N','N','NE','SE','S','S','SW','SW','SW','NW','NW']
				di = ['x',4,4,8,10,4,4,8,10,8,8,6,4,6,8,8,12,6,6,6,8]
			elif s == 'Summer':
				we = ['x',0,0,0,6,2,0,0,6,1,0,2,6,2,1,6,2,1,0,0,2]
				dt = ['x',2,3,4,3,2,2,2,3,2,3,3,2,3,4,3,3,2,2,2,1] # day temperature
				nt = ['x',1,2,3,3,2,2,2,2,2,2,1,1,2,2,3,2,2,2,1,1] # night temperature
				wi = ['x',0,0,0,0,0,0,1,2,1,1,1,0,0,0,1,0,2,1,1,0]
				wd = ['x','N','NE','SE','S','SW','NW','SW','NW','SW','NW','N','NE','SE','S','SW','S','SW','SW','SW','NW']
				di = ['x',8,6,8,8,10,10,10,4,10,8,4,4,6,10,8,8,8,10,10,8]
			elif s == 'Autumn':
				we = ['x',1,6,2,0,8,6,0,3,4,1,0,1,2,2,6,6,0,2,3,1]
				dt = ['x',2,2,3,4,3,3,2,2,1,1,1,2,3,2,2,2,3,2,1,0] # day temperature
				nt = ['x',0,1,2,2,2,2,1,2,1,1,0,1,2,2,1,2,2,1,0,0] # night temperature
				wi = ['x',0,0,0,0,0,0,1,1,2,1,2,1,0,1,2,1,1,2,2,1]
				wd = ['x','N','N','NE','SE','S','SW','NW','SW','NW','NW','N','NE','SE','S','SW','S','SW','NW','SW','NW']
				di = ['x',8,6,4,8,10,10,8,10,4,8,4,4,6,6,6,6,10,4,8,8]
			elif s == 'Winter':
				we = ['x',2,0,0,2,8,2,0,2,4,1,4,0,5,2,0,0,2,6,4,5]
				dt = ['x',1,0,0,1,0,1,2,1,1,1,1,0,1,1,2,3,2,2,1,1] # day temperature
				nt = ['x',0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,2,1,1,0,0] # night temperature
				wi = ['x',0,1,2,1,0,0,1,0,1,1,2,1,2,1,1,2,1,2,1,1]
				wd = ['x','N','NW','N','NE','SE','S','SW','NW','N','NE','SE','NE','NE','SE','S','SW','S','SW','SW','NW']
				di = ['x',10,8,8,6,8,4,6,8,8,8,4,8,4,4,4,4,4,4,4,4]
		elif c == 'Cool Temperate':
			if s == 'Spring':
				we = ['x',4,1,8,1,6,4,1,2,1,1,0,6,6,8,9,0,2,7,4,4]
				dt = ['x',1,2,3,3,2,1,1,2,1,0,1,2,3,4,3,2,2,2,1,1] # day temperature
				nt = ['x',1,2,2,3,2,1,0,2,1,0,0,0,2,3,3,1,2,2,1,1] # night temperature
				wi = ['x',1,1,0,1,2,2,1,1,1,0,1,1,0,0,0,0,1,2,2,1]
				wd = ['','N','NE','SE','S','SW','NW','SW','SW','NW','N','N','NE','SE','S','S','SW','SE','SW','NW','NW']
				di = ['x',4,4,8,8,6,4,10,8,8,8,6,4,6,10,6,12,4,4,4,6]
			elif s == 'Summer':
				we = ['x',2,2,0,0,9,2,6,6,1,0,0,8,6,1,1,1,6,6,6,3]
				dt = ['x',2,3,4,4,3,3,2,2,3,3,3,4,4,4,3,3,3,2,2,2] # day temperature
				nt = ['x',2,3,2,3,3,2,2,2,2,2,2,2,3,3,3,2,3,2,2,2] # night temperature
				wi = ['x',0,0,0,0,0,0,1,2,1,1,1,0,0,0,0,1,2,1,1,0]
				wd = ['','N','NE','SE','S','SW','SW','SW','NW','SW','NW','N','NE','SE','SE','S','SW','NW','SW','NW','N']
				di = ['x',6,4,8,10,8,8,8,4,10,8,6,6,6,8,10,10,4,8,6,8]
			elif s == 'Autumn':
				we = ['x',8,2,8,2,8,9,7,6,3,1,4,6,1,7,6,1,0,1,4,1]
				dt = ['x',2,2,3,4,4,3,2,2,2,1,1,1,3,2,2,2,3,2,1,0] # day temperature
				nt = ['x',1,1,2,2,2,2,2,2,1,1,1,1,2,2,2,1,1,1,0,0] # night temperature
				wi = ['x',0,0,0,0,0,0,1,1,2,1,2,1,0,1,2,1,1,2,2,1]
				wd = ['x','N','N','NE','SE','S','SW','NW','SW','NW','N','NE','SE','SE','S','SW','S','SW','NW','SW','NW']
				di = ['x',8,6,6,6,10,8,4,8,6,6,4,4,8,4,6,8,10,6,6,8]
			elif s == 'Winter':
				we = ['x',5,3,4,2,8,2,7,3,6,4,3,4,0,1,0,2,4,4,1,2]
				dt = ['x',1,0,1,2,3,2,2,1,2,1,1,0,2,2,2,2,1,1,1,1] # day temperature
				nt = ['x',0,0,1,1,1,1,1,1,2,1,1,0,0,1,0,1,0,1,1,1] # night temperature
				wi = ['x',0,1,2,1,0,0,1,0,1,1,2,2,1,1,1,2,1,2,1,1]
				wd = ['x','N','N','NE','SE','SE','S','SW','NW','SW','NW','N','NE','SE','S','S','SW','NW','SW','SW','NW']
				di = ['x',4,6,4,4,8,8,6,10,8,6,4,4,6,8,8,6,6,6,10,6]
		elif c == 'Warm Temperate':
			if s == 'Spring':
				we = ['x',6,2,8,1,6,3,1,2,2,1,0,1,8,8,9,0,2,7,2,6]
				dt = ['x',2,2,3,3,2,1,2,2,1,2,1,2,3,4,3,2,2,2,2,2] # day temperature
				nt = ['x',2,2,2,3,2,1,2,2,1,2,1,1,2,3,3,1,2,2,2,2] # night temperature
				wi = ['x',1,1,0,1,2,2,1,1,1,0,1,1,0,0,0,0,1,2,2,1]
				wd = ['x','N','NE','SE','S','SW','NW','SW','SW','NW','N','N','NE','SE','S','S','SW','SE','SW','NW','NW']
				di = ['x',4,4,8,8,6,6,10,8,6,8,6,4,8,10,6,12,4,4,4,6]
			elif s == 'Summer':
				we = ['x',2,1,0,0,6,1,9,3,2,0,0,8,6,0,1,2,1,1,6,6]
				dt = ['x',2,3,4,4,3,3,3,4,3,4,3,4,3,5,4,3,3,4,2,2] # day temperature
				nt = ['x',2,3,2,3,3,2,3,4,3,3,2,2,3,3,4,3,3,3,2,2] # night temperature
				wi = ['x',0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,2,1,0,0,0]
				wd = ['x','NE','N','NE','SE','S','SW','SE','S','SW','NW','N','NE','NE','SE','S','SW','NW','N','Nw','N',]
				di = ['x',6,6,8,10,8,10,4,12,8,6,6,8,4,10,12,4,6,6,6,4]
			elif s == 'Autumn':
				we = ['x',8,2,8,8,6,9,3,6,7,3,6,6,1,7,3,2,0,1,6,1]
				dt = ['x',3,3,3,4,4,3,3,3,3,2,2,2,3,2,2,3,3,2,2,1] # day temperature
				nt = ['x',2,3,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2,1,2,1] # night temperature
				wi = ['x',0,0,0,0,0,0,1,1,2,1,2,1,0,1,2,1,1,2,2,1]
				wd = ['x','N','N','NE','SE','S','SW','NW','SW','NW','N','NE','SE','SE','S','SW','S','SW','NW','SW','NW']
				di = ['x',8,6,6,8,8,8,8,8,4,6,4,4,8,4,8,6,10,6,6,8]
			elif s == 'Winter':
				we = ['x',4,4,4,2,8,2,7,3,6,7,6,3,0,2,0,2,4,3,1,3]
				dt = ['x',1,1,1,2,2,2,2,2,3,2,2,1,2,2,2,2,1,1,1,2] # day temperature
				nt = ['x',1,1,1,1,1,0,2,2,3,2,2,1,0,1,0,1,0,1,1,2] # night temperature
				wi = ['x',0,1,2,1,0,0,1,0,1,1,2,2,1,1,1,2,1,2,1,1]
				wd = ['x','N','N','NE','SE','SE','S','SW','NW','SW','NW','N','NE','SE','S','S','SW','NW','SW','SW','Nw']
				di = ['x',6,4,4,4,8,8,6,10,8,4,4,4,6,6,8,6,6,8,10,8]
		elif c == 'Subtropical':
			if s == 'Spring':
				we = ['x',3,2,8,0,0,0,1,2,1,0,0,1,2,8,9,0,2,0,2,6]
				dt = ['x',3,3,3,3,3,4,2,3,3,3,3,3,3,3,4,3,2,3,3,2] # day temperature
				nt = ['x',3,2,2,2,2,2,2,3,3,2,2,2,3,2,3,2,2,2,2,2] # night temperature
				wi = ['x',0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0]
				wd = ['x','NE','N','NE','SE','S','SW','NW','N','NW','N','NE','SE','NE','SE','SE','S','S','SW','SW','NW']
				di = ['x',10,4,10,12,8,8,6,6,4,8,8,12,8,12,8,10,6,8,6,4]
			elif s == 'Summer':
				we = ['x',1,2,0,0,2,1,6,6,2,0,0,8,9,0,0,2,2,0,1,6]
				dt = ['x',4,4,5,4,4,3,3,4,4,4,3,4,4,4,5,4,3,4,3,2] # day temperature
				nt = ['x',3,3,3,3,3,2,3,4,3,3,2,2,3,3,4,3,3,3,2,2] # night temperature
				wi = ['x',1,1,1,0,1,0,0,0,1,1,1,0,2,1,1,2,1,0,0,1]
				wd = ['x','NE','NE','NE','SE','SE','S','SW','NW','N','N','NE','NE','NE','NE','NE','SE','S','SW','NW','N']
				di = ['x',10,8,10,10,6,8,4,6,6,8,10,12,4,10,10,4,4,6,8,6]
			elif s == 'Autumn':
				we = ['x',8,2,8,8,2,2,1,2,1,0,1,2,0,0,9,0,0,1,6,1]
				dt = ['x',3,3,3,4,4,3,3,4,4,3,2,3,3,4,4,3,3,3,2,2] # day temperature
				nt = ['x',2,3,3,2,3,2,3,3,3,2,2,2,2,3,3,2,2,2,2,2] # night temperature
				wi = ['x',0,0,0,0,1,0,1,0,0,0,0,1,0,0,2,1,0,0,0,1]
				wd = ['x','NE','N','NE','SE','S','SW','NW','SW','NW','N','N','NE','NE','SE','SE','S','S','SW','NW','N']
				di = ['x',8,8,8,6,4,8,10,8,12,10,10,4,8,6,4,6,8,10,10,8]
			elif s == 'Winter':
				we = ['x',3,1,6,2,8,2,6,3,7,2,6,3,0,2,0,1,6,3,1,6]
				dt = ['x',2,2,2,3,2,3,2,3,3,2,2,2,3,3,3,2,2,2,2,2] # day temperature
				nt = ['x',2,2,2,1,2,2,2,2,3,1,2,2,2,2,2,1,2,2,2,2] # night temperature
				wi = ['x',0,1,1,1,0,0,1,0,2,1,2,2,1,1,1,2,1,2,1,1]
				wd = ['x','N','N','NE','SE','SE','S','SW','NW','SW','NW','N','NE','SE','S','S','SW','SW','NW','SW','NW']
				di = ['x',8,6,4,4,8,8,8,10,4,6,4,4,6,6,8,8,8,6,10,6]
		elif c == 'Tropical (Dry)':
			if s == 'Spring':
				we = ['x',3,2,8,0,2,6,1,0,2,0,0,0,1,2,2,0,0,6,9,0]
				dt = ['x',3,4,4,5,4,3,4,4,4,5,5,5,5,4,4,5,5,4,3,4] # day temperature
				nt = ['x',3,3,3,3,3,3,3,3,3,3,3,3,4,3,4,3,3,4,3,3] # night temperature
				wi = ['x',1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,2,2,1]
				wd = ['x','NE','NE','NE','SE','SE','S','SW','NW','N','N','NE','NE','NE','NE','NE','SE','S','SW','NW','N']
				di = ['x',10,8,12,10,6,6,6,6,6,10,10,12,10,8,8,8,6,4,4,8]
			elif s == 'Summer':
				we = ['x',2,0,0,0,1,2,6,1,2,0,0,8,2,0,0,0,1,9,2,6]
				dt = ['x',4,5,5,5,4,4,3,4,4,5,4,4,5,4,5,5,5,4,3,3] # day temperature
				nt = ['x',3,3,3,3,3,3,3,4,3,3,3,3,4,3,4,4,4,4,2,3] # night temperature
				wi = ['x',1,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,2,2,1]
				wd = ['x','NE','NE','NE','NE','SE','S','SE','NE','NE','NE','NE','N','NE','NE','SE','SE','S','SW','NW','N']
				di = ['x',8,10,10,12,8,6,8,12,8,10,10,10,10,10,8,8,6,4,4,6]
			elif s == 'Autumn':
				we = ['x',0,2,0,8,2,2,3,2,0,0,1,2,0,0,0,0,1,9,2,6]
				dt = ['x',4,4,5,4,4,4,4,4,4,5,4,3,5,5,5,5,5,4,3,3] # day temperature
				nt = ['x',3,4,3,3,3,3,4,3,3,3,3,3,3,3,3,4,4,4,2,3] # night temperature
				wi = ['x',1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,2,1,1]
				wd = ['x','NE','NE','NE','SE','SE','S','SW','NW','N','N','NE','NE','NE','NE','NE','SE','S','SW','NW','N']
				di = ['x',10,8,12,10,6,6,6,4,10,10,10,8,10,10,10,8,6,4,4,6]
			elif s == 'Winter':
				we = ['x',3,1,0,8,2,0,2,1,0,1,2,3,0,2,0,0,1,9,1,2]
				dt = ['x',3,4,5,3,4,4,4,4,4,5,4,3,5,4,5,5,4,4,3,3] # day temperature
				nt = ['x',3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,4,2,3] # night temperature
				wi = ['x',0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,2,1,0]
				wd = ['x','NE','N','NE','SE','S','SW','NW','N','NW','N','NE','SE','NE','SE','SE','S','S','SW','NW','N']
				di = ['x',10,12,10,8,4,8,6,12,10,12,6,8,10,6,8,6,4,4,8,10]
		elif c == 'Tropical (Wet)':
			if s == 'Spring':
				we = ['x',7,2,8,3,2,0,2,6,2,0,0,2,7,2,0,1,2,9,7,1]
				dt = ['x',3,4,4,5,4,3,4,4,4,5,5,5,5,4,4,5,5,4,3,4] # day temperature
				nt = ['x',3,3,3,3,3,3,3,3,3,3,3,3,4,3,4,3,3,4,3,3] # night temperature
				wi = ['x',1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,2,2,1]
				wd = ['x','NE','N','NE','NE','SE','S','SW','NW','N','NE','SE','NE','SE','S','SE','SE','S','SW','NW','N']
				di = ['x',4,6,8,8,4,8,8,8,6,8,4,6,4,4,4,4,4,4,4,8]
			elif s == 'Summer':
				we = ['x',7,0,1,7,0,2,8,2,6,0,2,2,6,0,2,0,1,9,7,6]
				dt = ['x',4,5,5,5,4,4,3,4,4,5,4,4,5,4,5,5,5,4,3,3] # day temperature
				nt = ['x',3,3,3,3,3,3,3,4,3,3,3,3,4,3,4,4,4,4,2,3] # night temperature
				wi = ['x',0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,2,1,1]
				wd = ['x','NE','N','NE','SE','S','SW','NW','N','NW','N','NE','SE','S','SE','S','S','SW','SW','NW','N']
				di = ['x',4,6,4,4,8,10,10,6,6,6,4,6,8,6,6,8,10,4,4,4]
			elif s == 'Autumn':
				we = ['x',1,2,8,7,2,0,2,6,2,0,2,1,2,0,2,2,6,9,7,6]
				dt = ['x',4,4,5,4,4,4,4,4,4,5,4,3,5,5,5,5,5,4,3,3] # day temperature
				nt = ['x',3,4,3,3,3,3,4,3,3,3,3,3,3,3,3,4,4,4,2,3] # night temperature
				wi = ['x',1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,2,1,1]
				wd = ['x','N','NE','NE','NE','SE','S','SW','NW','N','NE','SE','NE','SE','SE','SE','S','S','SW','NW','N']
				di = ['x',8,4,8,4,4,8,8,8,8,8,4,6,4,4,4,4,4,4,6,6]
			elif s == 'Winter':
				we = ['x',6,1,0,8,2,0,0,2,0,0,0,2,6,2,0,0,2,9,6,2]
				dt = ['x',3,4,5,3,4,4,4,4,4,5,4,3,5,4,5,5,4,4,3,3] # day temperature
				nt = ['x',3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,4,2,3] # night temperature
				wi = ['x',1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,2,1,1]
				wd = ['x','NE','NE','NE','SE','SE','S','SW','NW','N','N','NE','NE','NE','SE','NE','SE','S','SW','NW','N']
				di = ['x',4,6,8,6,4,8,8,8,10,10,6,4,4,4,6,4,4,4,8,6]
		# 0 = clear, dry
		# 1 = cloudy, dry
		# 2 = cloudy, showers
		# 3 = overcast, dry
		# 4 = overcast, snow showers
		# 5 = overcast, continuous snow
		# 6 = overcast, showers
		# 7 = overcast, continuous rain
		# 8 = foggy
		# 9 = overcast, thunderstorm
		
		
		# 0 = Freezing
		# 1 = Cold
		# 2 = Cool
		# 3 = Warm
		# 4 = Hot
		# 5 = Sweltering
		
		if we[current_weather] == 0: weather = 'clear, dry'
		elif we[current_weather] == 1: weather = 'cloudy, dry'
		elif we[current_weather] == 2: weather = 'cloudy, showers'
		elif we[current_weather] == 3: weather = 'overcast, dry'
		elif we[current_weather] == 4: weather = 'overcast, snow showers'
		elif we[current_weather] == 5: weather = 'overcast, continuous snow'
		elif we[current_weather] == 6: weather = 'overcast, showers'
		elif we[current_weather] == 7: weather = 'overcast, continuous rain'
		elif we[current_weather] == 8: weather = 'foggy'
		elif we[current_weather] == 9: weather = 'overcast, thunderstorn'
		
		if dt[current_weather] == 0: w1 = 'Freezing'
		elif dt[current_weather] == 1: w1 = 'Cold'
		elif dt[current_weather] == 2: w1 = 'Cool'
		elif dt[current_weather] == 3: w1 = 'Warm'
		elif dt[current_weather] == 4: w1 = 'Hot'
		elif dt[current_weather] == 5: w1 = 'Sweltering'
		
		if nt[current_weather] == 0: w2 = 'Freezing'
		elif nt[current_weather] == 1: w2 = 'Cold'
		elif nt[current_weather] == 2: w2 = 'Cool'
		elif nt[current_weather] == 3: w2 = 'Warm'
		elif nt[current_weather] == 4: w2 = 'Hot'
		elif nt[current_weather] == 5: w2 = 'Sweltering'
		
		temperature = w1 + '(' + w2 + ')'
		
		if we[current_weather] == 8: wind_speed = 0
		else: wind_speed = wind_gen(wi[current_weather])
		
		wind_direction = wd[current_weather]
		syssc.insert(tk.INSERT, str(current_weather) + ' ' + weather + ' ' + temperature + ' ' + str(wind_speed) + ' ' + wind_direction + '\n')		
		
		wc_sides = di[current_weather]
		weather_change = dice(1,sides=wc_sides)
		
		if weather_change == 1:
			if current_weather > 1: current_weather -=1
			else: current_weather = 20
		elif weather_change == 2:
			if current_weather < 19: current_weather += 2
			elif current_weather == 19:	current_weather = 1
			else: current_weather = 2
		elif weather_change == 3 or weather_change == 4:
			if current_weather < 20: current_weather += 1
			else: current_weather = 1
		else: current_weather += 0
		
# Labelframe using tab1 as parent
mighty = ttk.LabelFrame(tab1, text = ' Weather Generator ')
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, width=15, text="Climate:").grid(column=0, row=0, sticky='W')
ttk.Label(mighty, width=15, text="Season:").grid(column=0, row=1, sticky='W')
ttk.Label(mighty, width=15, text="Watches:").grid(column=0, row=2, sticky='W')
ttk.Label(mighty, width=15, text="Starting Weather:").grid(column=0, row=3, sticky='W')

clim = tk.StringVar()
seas = tk.StringVar()
watc = tk.StringVar()
s_we = tk.StringVar()

clim_t = ttk.Combobox(mighty, width=15, textvariable=clim, state='readonly')
clim_t['values'] = ('Subpolar','Cool Temperate','Warm Temperate','Subtropical','Tropical (Dry)','Tropical (Wet)')
clim_t.grid(column=1,row=0, sticky=tk.W)
clim_t.current(0)

seas_t = ttk.Combobox(mighty, width=15, textvariable=seas, state='readonly')
seas_t['values'] = ('Spring','Summer','Autumn','Winter')
seas_t.grid(column=1,row=1, sticky=tk.W)
seas_t.current(0)

n_watc = ttk.Combobox(mighty, width=15, textvariable=watc, state='readonly')
n_watc['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42)
n_watc.grid(column=1,row=2, sticky=tk.W)
n_watc.current(0)

s_weat = ttk.Combobox(mighty, width=15, textvariable=s_we, state='readonly')
s_weat['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
s_weat.grid(column=1,row=3, sticky=tk.W)
s_weat.current(0)

w_gen = ttk.Button(tab1, width=12, text="Generate", command=weather_gen).grid(column=0, row=5)

syssc_w = 60
syssc_h = 43
syssc = scrolledtext.ScrolledText(mighty, width=syssc_w, height=syssc_h, wrap=tk.WORD)
syssc.grid(column=0, sticky='WE', columnspan=3)

# ----------------------------------------------------------------------------------------------

def event_gen():
	evesc.delete('1.0', tk.END)
	count = 0
	yrst = int(year_t.get())
	
	while count < yrst:
		count += 1	
		evesc.insert(tk.INSERT, 'Year ' + str(count) + '\n')
		spcnt = smcnt = aucnt =	wicnt = 0
		while spcnt < 3:
			spcnt += 1
			ev = dice(1,sides=100)
			if ev < 3: evn = 'State Occasion'
			elif ev > 2 and ev < 5: evn = 'Edict'
			elif ev > 4 and ev < 7: evn = 'Civil Unrest'
			elif ev == 7: evn = 'Death/Illness'
			elif ev > 7 and ev < 13: evn = 'War/Raids'
			elif ev > 12 and ev < 16: evn = 'Terrorisation'
			elif ev > 15 and ev < 18: evn = 'Epidemic'
			elif ev > 17 and ev < 20: evn = 'Disaster'
			elif ev == 20: evn = 'Freak Weather'
			elif ev > 20 and ev < 23:
				evn = 'Multiple Events - Unfinished'
			else: evn = 'No events'		
			evesc.insert(tk.INSERT, 'Spring: ' + evn + '\n')
		while smcnt < 3:
			smcnt += 1
			ev = dice(1,sides=100)
			if ev < 4: evn = 'State Occasion'
			elif ev > 3 and ev < 6: evn = 'Edict'
			elif ev > 5 and ev < 8: evn = 'Civil Unrest'
			elif ev == 8: evn = 'Death/Illness'
			elif ev > 8 and ev < 12: evn = 'War/Raids'
			elif ev > 11 and ev < 15: evn = 'Terrorisation'
			elif ev > 14 and ev < 18: evn = 'Epidemic'
			elif ev > 17 and ev < 20: evn = 'Disaster'
			elif ev == 20: evn = 'Freak Weather'
			elif ev > 20 and ev < 23:
				evn = 'Multiple Events - Unfinished'
			else: evn = 'No events'		
			evesc.insert(tk.INSERT, 'Summer: ' + evn + '\n')	
		while aucnt < 3:
			aucnt += 1
			ev = dice(1,sides=100)
			if ev < 3: evn = 'State Occasion'
			elif ev > 2 and ev < 5: evn = 'Edict'
			elif ev > 4 and ev < 7: evn = 'Civil Unrest'
			elif ev == 7: evn = 'Death/Illness'
			elif ev > 7 and ev < 10: evn = 'War/Raids'
			elif ev > 9 and ev < 13: evn = 'Terrorisation'
			elif ev == 13: evn = 'Epidemic'
			elif ev > 13 and ev < 16: evn = 'Good Harvest'
			elif ev > 15 and ev < 18: evn = 'Poor Harvest'
			elif ev > 17 and ev < 20: evn = 'Disaster'
			elif ev == 20: evn = 'Freak Weather'
			elif ev > 20 and ev < 23:
				evn = 'Multiple Events - Unfinished'
			else: evn = 'No events'
			evesc.insert(tk.INSERT, 'Autumn: ' + evn + '\n')		
		while wicnt < 3:
			wicnt += 1
			if ev ==1: evn = 'State Occasion'
			elif ev > 1 and ev < 4: evn = 'Edict'
			elif ev > 3 and ev < 6: evn = 'Civil Unrest'
			elif ev == 6: evn = 'Death/Illness'
			elif ev > 6 and ev < 9: evn = 'War/Raids'
			elif ev > 8 and ev < 14: evn = 'Terrorisation'
			elif ev > 13 and ev < 18: evn = 'Disaster'
			elif ev > 17 and ev < 21: evn = 'Freak Weather'
			elif ev > 20 and ev < 23:
				evn = 'Multiple Events - Unfinished'
			else: evn = 'No events'		
			evesc.insert(tk.INSERT, 'Winter: ' + evn + '\n')	

# Labelframe using tab1 as parent
mighty2 = ttk.LabelFrame(tab2, text = ' Event Generator ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty2, width=15, text="Years:").grid(column=0, row=0, sticky='W')

year = tk.StringVar()

year_t = ttk.Combobox(mighty2, width=15, textvariable=year, state='readonly')
year_t['values'] = (1,2,3,4,5)
year_t.grid(column=1,row=0, sticky=tk.W)
year_t.current(0)

e_gen = ttk.Button(tab2, width=12, text="Generate", command=event_gen).grid(column=0, row=5)

evesc_w = 60
evesc_h = 43
evesc = scrolledtext.ScrolledText(mighty2, width=syssc_w, height=syssc_h, wrap=tk.WORD)
evesc.grid(column=0, sticky='WE', columnspan=3)

# ----------------------------------------------------------------------------------------------

#===================
# Start GUI
#===================

win.mainloop()
