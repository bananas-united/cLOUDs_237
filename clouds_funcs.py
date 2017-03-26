# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:50:27 2017

@author: pescados_unidos
"""
'''
def setColor(dev, i,r,g,b,w,u1,u2,u3):
	dev.send_single_value(1, 255) # sends the value 255 to DMX channel 1
'''
import sys
import imp
import time
import numpy as np

pyudmx = imp.load_source('pyudmx', '/home/pescados_unidos/clouds/pyudmx.py')


dev = pyudmx.uDMXDevice()
dev.open()
#print dir(dev)
#dev.send_multi_value(1, [255, 255,0,0,0, 0,0,0 ])
#dev.send_single_value(1, 255) # sends the value 255 to DMX channel 1


# time.sleep(2)
#dev.close()


#colors
color_2 = np.array([0,0,0])
color_3 = np.array([255,255,255])
color_4 = np.array([255,0,0])
color_5 = np.array([0,255,0])
color_6 = np.array([0,0,255])
color_7 = np.array([255,255,0])
color_8 = np.array([0,255,255])
color_9 = np.array([255,0,255])
color_10 = np.array([192,192,192])
color_11 = np.array([128,128,128])
color_12 = np.array([128,0,0])
color_13 = np.array([128,128,0])
color_14 = np.array([0,128,0])
color_15 = np.array([128,0,128])
color_16 = np.array([0,128,128])
color_17 = np.array([0,0,128])
color_list = [color_2,color_3,color_4,color_5,color_6,color_7,color_8,color_9,color_10,color_11,color_12,color_13,color_14,color_15,color_16,color_17]


#clouds addresses [dmx_channel, device_type,x location,y location] /type1=black , type2 = white
cloud_1 = [10,'type1',16,1]
cloud_2 = [20,'type2',1,23]
cloud_3 = [30,'type1',21,20]
cloud_4 = [40,'type1',8,6]
cloud_5 = [50,'type1',14,16]
cloud_6 = [60,'type1',23,25]
cloud_7 = [70,'type1',29,3]
cloud_8 = [80,'type1',22,28]
cloud_9 = [90,'type1',15,14]
cloud_10 = [100,'type1',26,9]
cloud_11 = [110,'type1',18,26]
cloud_12 = [120,'type1',4,21]
cloud_13 = [130,'type1',27,4]
cloud_14 = [140,'type1',19,17]
cloud_15 = [150,'type1',24,7]
cloud_16 = [160,'type1',6,15]
cloud_17 = [170,'type1',5,10]
cloud_18 = [180,'type1',28,24]
cloud_19 = [190,'type1',3,22]
cloud_20 = [200,'type1',9,18]
cloud_21 = [210,'type1',25,12]
cloud_22 = [220,'type1',20,2]
cloud_23 = [230,'type1',17,19]
cloud_24 = [240,'type1',10,11]
cloud_25 = [250,'type1',12,8]
cloud_26 = [260,'type1',11,5]
cloud_27 = [270,'type1',7,0]
cloud_28 = [280,'type1',2,27]
cloud_29 = [290,'type1',13,29]
cloud_30 = [300,'type1',0,13]
cloud_list = [cloud_1,cloud_2,cloud_3,cloud_4,cloud_5,cloud_6,cloud_7,cloud_8,cloud_9,cloud_10,cloud_11,cloud_12,cloud_13,cloud_14,cloud_15,cloud_16,cloud_17,cloud_18,cloud_19,cloud_20,cloud_21,cloud_22,cloud_23,cloud_24,cloud_25,cloud_26,cloud_27,cloud_28,cloud_29,cloud_30]






################################
##functions
################################

###########general 

def time_counter(seconds):
	starttime = time.time()
	while True:
		now = time.time()
		if now > starttime + seconds:
			break
		yield now - starttime

'''
for i in time_counter(10):
	print int(i)
	time.sleep(1)
'''

###########single device functions
def send_single_color(strength,color_num_list,cloud_num):
	color_num_list = [int(x) for x in color_num_list]
	if cloud_num[1]=='type1':
		return dev.send_multi_value(cloud_num[0],[int(strength), color_num_list[0],color_num_list[1],color_num_list[2],0, 0,0,0 ])
	elif cloud_num[1]=='type2':
		return dev.send_multi_value(cloud_num[0],[color_num_list[0],color_num_list[1],color_num_list[2],int(strength),0, 0,0,0 ])

#send_single_color(255,color_14,cloud_1)
#send_single_color(255,color_14,cloud_2)

def send_colors(strength,color_num_list,cloud_num_list):
	for cloud_num in cloud_num_list:
		send_single_color(strength,color_num_list,cloud_num)

'''
send_colors(255,color_5,[cloud_1,cloud_2])
time.sleep(2)
send_colors(255,color_15,[cloud_1,cloud_2])
'''

#def light_delta_step(color_num_start,color_num_end,step_time,total_time):
#	steps=int(1.00*total_time/step_time)
#	delta_step1 = 1.00*(color_num_end-color_num_start)*step/steps
#	return [int(x) for x in delta_step1]



def fade(color_num_start,color_num_end,step_time,total_time,cloud_num_list):
	steps=int(1.00*total_time/step_time+1)
	for step in range(1,steps):
		color_delta = 1.00*(color_num_end-color_num_start)*step/steps
		color_to_send = [int(x+y) for x,y in zip(color_num_start,color_delta)]
		time.sleep(step_time)
		send_colors(255,color_to_send,cloud_num_list)



#fade(color_14,color_13,1,5,[cloud_1,cloud_2])
#fade(color_4,color_5,1,5,[cloud_1,cloud_2])
#fade(color_4,color_15,0.04,3,[cloud_1,cloud_2])


def send_colors_by_strength(current_level,total_levels, color_num,cloud_num_list):
	send_colors(int(255*current_level/total_levels),color_num,cloud_num_list)


'''
!!!blinking!!!
send_colors_by_strength(14,20,color_10,cloud_list) 
send_colors(int(255*14/20),color_10,cloud_list)

for i in range(10):
	time.sleep(1)
	send_colors_by_strength(i+1,10,color_6,cloud_list)
send_colors_by_strength(4,10,color_6,cloud_list)
'''

def send_colors_by_strength_color_shift(current_level,total_levels, color_num_low,color_num_high, cutoff,cloud_num_list):
	if current_level >= round(cutoff,2):
		send_colors_by_strength(current_level,total_levels, color_num_high,cloud_num_list)
	else:
		send_colors_by_strength(current_level,total_levels, color_num_low,cloud_num_list)



################################
##patterns
################################

#time based loop | fade between all colors 
for i in time_counter(20):
	current_color=color_list[-1]
	for color in color_list:
		fade(np.array(current_color),np.array(color),1,5,[cloud_1,cloud_2])
		time.sleep(0.5)


#color on off 
send_colors(255,color_5,[cloud_1,cloud_2])
time.sleep(2)
send_colors(255,color_15,[cloud_1,cloud_2])

