import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250

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

# lowpassfreq: 5Hz, 10Hz, 20Hz, 41Hz, 92Hz, 184Hz
imu_1_master.setLowPassFilterFrequency("AccelLowPassFilter184")
imu_1_slave.setLowPassFilterFrequency("AccelLowPassFilter184")
imu_2_master.setLowPassFilterFrequency("AccelLowPassFilter184")
imu_2_slave.setLowPassFilterFrequency("AccelLowPassFilter184")


imu_1_master.begin()
imu_1_slave.begin()
imu_2_master.begin()
imu_2_slave.begin()

imu_1_master.caliberateAccelerometer()
imu_1_slave.caliberateAccelerometer()
imu_2_master.caliberateAccelerometer()
imu_2_slave.caliberateAccelerometer()
