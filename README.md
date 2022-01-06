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

## Note
Because I use also an rtc-head ds1307 with default-address 0x68 on bus-1 There would be a address-collision because one imu9250 also has the same address.
I cant change the address of both devices (imu allows ox69 but I used it already). Therefore I need to unload the kernel-module of the rtc-ds1307 after the raspberry gets the correct time update and before reading the imu250-sensors by using this in mpu_reader.py:

```python
subprocess.run(["sudo", "rmmod", "rtc-ds1307"]) 
```
