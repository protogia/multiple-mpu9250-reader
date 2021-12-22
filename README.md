# multiple-mpu9250-reader
Reading up to 4 mpu9250 with Raspberry 3B+ using i2c

## Wiring 
To use the Raspi3B+ and upt four MPU9250 you need to use two i2c-busses like described in this [HowTo](https://github.com/GiancarloRizzo/HowToSummeries/blob/master/HowTo-Raspberry/how-to-connect-multiple-MPU9250-with-raspi.md).

## Pre: Environment and dependencies
```bash
virtualenv -p python3 
```

## Code
In your code you need to reference the two busses and the two devices by their address for each bus:
```
#bus  address name
bus_0 0x68    imu11
bus_0 0x69    imu12 
bus_1 0x68    imu21
bus_1 0x69    imu22
```

## Start example
```
python3 ./src/imu_reader.py
# calibrates imus and creates imu.log 
```
