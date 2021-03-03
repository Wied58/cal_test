#!/usr/bin/python3

from time import strftime
from time import gmtime
import subprocess


# shutter speed (exposure time) in microseconds
raspistill_ss = 1000000 

# Sensitivity (ISO)
ISO = 800

#Dynamic Range Compression (DRC) options :off,low,med,high
drc = 'off'

#White Balance: off,auto,sun,cloud,shade,tungsten,fluorescent,incandescent,flash,horizon
awb = 'off'

# Mannually set white balance gains
white_balance_gains = '1.03125, 1.8086'

#Brightness
br = 50

#interval between images in milliseconds
raspistill_tl = 0

# total time of the run in milliseconds (controls how many photos you take)
# Exposure time converted to milliseconds + interval between images X number of images + an extra interval
#raspistill_t = (((raspistill_ss/1000) + raspistill_tl) * (number_of_images +1)) 
#raspistill_t = (((raspistill_ss/1000) + raspistill_tl) * (number_of_images)) 
raspistill_t = 5000

image_file_name = "cal_test_" + (strftime("%y%m%d_%H%M%S", gmtime())) + "_%d"
command = ['/usr/bin/raspistill', '-v',
                         '-t', str(raspistill_t),
                         '-ss', str(raspistill_ss),
                         '-tl', str(raspistill_tl),
                         '-ISO', str(ISO),
                         '-drc', str(drc),
                         '-awb', awb,
                         '-awbg', white_balance_gains,
                         '-br', str(br),
                         '-r',
                         '-ts',
                         '-st',
                         '-o', image_file_name + '.jpg']
subprocess.call(command)


