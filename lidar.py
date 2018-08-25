#!/usr/bin/env python
from numpy import interp
import RPi.GPIO as IO
import time
import VL53L0X
import rospy
from sensor_msgs.msg import LaserScan
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19,IO.OUT)
p = IO.PWM(19,50)
p.start(7.5)


rospy.init_node('laser_scan_publisher')

scan_pub = rospy.Publisher('scan', LaserScan, queue_s$
tof = VL53L0X.VL53L0X()
num_readings = 180
laser_frequency = 100
tof.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)
flag=1
count = 0
r = rospy.Rate(1.0)
while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        scan = LaserScan()
        scan.header.stamp = current_time
        scan.header.frame_id = 'laser'
        scan.angle_min = -3.14
        scan.angle_max = 3.14
        scan.angle_increment = 3.14 / num_readings
        scan.time_increment = (1.0 / laser_frequency)$
        scan.range_min = 0.0
        scan.range_max = 30.0

        scan.ranges = [0]*180
        scan.intensities = []
        if(flag==1):
                for i in xrange(0, num_readings):
#                       print(i)
                        p.ChangeDutyCycle(interp(i,[0$
                        distance =float(tof.get_dista$
                        scan.ranges[i]=distance/100
#                       scan.ranges.append(distance/1$
#                       scan.intensities.append(1)
#                       scan_pub.publish(scan)
                        print(len(scan.ranges))
		scan_pub.publish(scan)
 		continue

        if(flag==0):
                for i in xrange(num_readings-1,-1,-1):
                        print(i)
                        p.ChangeDutyCycle(interp(i,[0$
                        distance =float(tof.get_dista$
                        scan.ranges[i]=distance/100
#                       scan.ranges.insert(i,distance$
#                       scan_pub.publish(scan)
                        flag=1
#                       print(len(scan.ranges))
                scan_pub.publish(scan)
                continue








