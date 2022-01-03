import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250
import datetime

mode = 'accel' #accel: just accelometer #else: accel, gyro and magnetometer, 

filename = 'mpu.csv'

address_master = 0x68
address_slave = 0x69

bus_1 = smbus.SMBus(0)
bus_2 = smbus.SMBus(1)

imu_1_master = MPU9250.MPU9250(bus=bus_1, address=address_master)
imu_1_slave = MPU9250.MPU9250(bus=bus_1, address=address_slave)
imu_2_master = MPU9250.MPU9250(bus=bus_2, address=address_master)
imu_2_slave = MPU9250.MPU9250(bus=bus_2, address=address_slave)

# ranges: +-2G +-4G +-8G +-16G
imu_1_master.setAccelRange("AccelRangeSelect2G")
imu_1_slave.setAccelRange("AccelRangeSelect2G")
imu_2_master.setAccelRange("AccelRangeSelect2G")
imu_2_slave.setAccelRange("AccelRangeSelect2G")

if not 'accel' in mode:
#	DPS:dagrees per second : +-250 +-500 +-1000 +-2000
	imu_1_master.setGyroRange("GyroRangeSelect250DPS")
	imu_1_slave.setGyroRange("GyroRangeSelect250DPS")
	imu_2_master.setGyroRange("GyroRangeSelect250DPS")
	imu_2_slave.setGyroRange("GyroRangeSelect250DPS")

# lowpassfreq: 5Hz, 10Hz, 20Hz, 41Hz, 92Hz, 184Hz
#imu_1_master.setLowPassFilterFrequency("AccelLowPassFilter184")
#imu_1_slave.setLowPassFilterFrequency("AccelLowPassFilter184")
#imu_2_master.setLowPassFilterFrequency("AccelLowPassFilter184")
#imu_2_slave.setLowPassFilterFrequency("AccelLowPassFilter184")

imu_1_master.begin()
imu_1_slave.begin()
imu_2_master.begin()
imu_2_slave.begin()


logfile = open(filename, 'w')
if 'accel' in mode:
	print ("""timestamp,S1_master_accel_x,S1_master_accel_y,S1_master_accel_z,S1_slave_accel_x,S1_slave_accel_y,S1_slave_accel_z,S2_master_accel_x,S2_master_accel_y,S2_master_accel_z,S2_slave_accel_x,S2_slave_accel_y,S2_slave_accel_z
		""", file=logfile)
	# with gyro- and magnetometer
else:
	print ("""timestamp,S1_master_accel_x,S1_master_accel_y,S1_master_accel_z,S1_slave_accel_x,S1_slave_accel_y,S1_slave_accel_z,S2_master_accel_x,S2_master_accel_y,S2_master_accel_z,S2_slave_accel_x,S2_slave_accel_y,S2_slave_accel_z,
		S1_master_gyro_x,S1_master_gyro_y,S1_master_gyro_z,S1_slave_gyro_x,S1_slave_gyro_y,S1_slave_gyro_z,S2_master_gyro_x,S2_master_gyro_y,S2_master_gyro_z,S2_slave_gyro_x,S2_slave_gyro_y,S2_slave_gyro_z,
		S1_master_mag_x,S1_master_mag_y,S1_master_mag_z,S1_slave_mag_x,S1_slave_mag_y,S1_slave_mag_z,S2_master_mag_x,S2_master_mag_y,S2_master_mag_z,S2_slave_mag_x,S2_slave_mag_y,S2_slave_mag_z
		""", file=logfile)
logfile.close


while True:
	logfile = open(filename, 'a')

	imu_1_master.readSensor()
	imu_1_master.computeOrientation()
	imu_1_slave.readSensor()
	imu_1_slave.computeOrientation()
	imu_2_master.readSensor()
	imu_2_master.computeOrientation()
	imu_2_slave.readSensor()
	imu_2_slave.computeOrientation()
	if 'accel' in mode:
		print (f"""{datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')},{imu_1_master.AccelVals[0]},{imu_1_master.AccelVals[1]},{imu_1_master.AccelVals[2]},{imu_1_slave.AccelVals[0]},{imu_1_slave.AccelVals[1]},{imu_1_slave.AccelVals[2]},{imu_2_master.AccelVals[0]},{imu_2_master.AccelVals[1]},{imu_2_master.AccelVals[2]},{imu_2_slave.AccelVals[0]},{imu_2_slave.AccelVals[1]},{imu_2_slave.AccelVals[2]}
		""", file=logfile)
	else:
	# with gyro and magnetometer
		print (f"""{datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')},{imu_1_master.AccelVals[0]},{imu_1_master.AccelVals[1]},{imu_1_master.AccelVals[2]},{imu_1_slave.AccelVals[0]},{imu_1_slave.AccelVals[1]},{imu_1_slave.AccelVals[2]},{imu_2_master.AccelVals[0]},{imu_2_master.AccelVals[1]},{imu_2_master.AccelVals[2]},{imu_2_slave.AccelVals[0]},{imu_2_slave.AccelVals[1]},{imu_2_slave.AccelVals[2]},
		{imu_1_master.GyroVals[0]},{imu_1_master.GyroVals[1]},{imu_1_master.GyroVals[2]},{imu_1_slave.GyroVals[0]},{imu_1_slave.GyroVals[1]},{imu_1_slave.GyroVals[2]},{imu_2_master.GyroVals[0]},{imu_2_master.GyroVals[1]},{imu_2_master.GyroVals[2]},{imu_2_slave.GyroVals[0]},{imu_2_slave.GyroVals[1]},{imu_2_slave.GyroVals[2]},
		{imu_1_master.MagVals[0]},{imu_1_master.MagVals[1]},{imu_1_master.MagVals[2]},{imu_1_slave.MagVals[0]},{imu_1_slave.MagVals[1]},{imu_1_slave.MagVals[2]},{imu_2_master.MagVals[0]},{imu_2_master.MagVals[1]},{imu_2_master.MagVals[2]},{imu_2_slave.MagVals[0]},{imu_2_slave.MagVals[1]},{imu_2_slave.MagVals[2]}""", file=logfile)

	time.sleep(0.01)
	logfile.close
