from ctypes import *
import os
import sys
import tempfile
import re
import datetime,time
   
if sys.version_info >= (3,0):
    import urllib.parse

print ("import all")

#import pypixet
#import datetime,time

# print pixet version
#print("Pixet version:", pixet.pixetVersion())

    
cur_dir = os.path.abspath(os.path.dirname(__file__))
ximc_dir = os.path.join(cur_dir, "..", "..", "ximc")
ximc_package_dir = os.path.join(r'D:\soft\STANDA\ximc-2.9.14\ximc', "crossplatform", "wrappers", "python")
sys.path.append(ximc_package_dir)  # add ximc.py wrapper to python path

if sys.platform in ("win32", "win64"):
    libdir = os.path.join(r'D:\soft\STANDA\ximc-2.9.14\ximc\win64')
    os.environ["Path"] = libdir + ";" + os.environ["Path"]  # add dll

try: 
    from pyximc import *
except ImportError as err:
    print ("Can't import pyximc module. The most probable reason is that you changed the relative location of the testpython.py and pyximc.py files. See developers' documentation for details.")
    exit()
except OSError as err:
    print ("Can't load libximc library. Please add all shared libraries to the appropriate places. It is decribed in detail in developers' documentation. On Linux make sure you installed libximc-dev package.\nmake sure that the architecture of the system and the interpreter is the same")
    exit()

def test_info(lib, device_id):
    print("\nGet device info")
    x_device_information = device_information_t()
    result = lib.get_device_information(device_id, byref(x_device_information))
    print("Result: " + repr(result))
    if result == Result.Ok:
        print("Device information:")
        print(" Manufacturer: " +
                repr(string_at(x_device_information.Manufacturer).decode()))
        print(" ManufacturerId: " +
                repr(string_at(x_device_information.ManufacturerId).decode()))
        print(" ProductDescription: " +
                repr(string_at(x_device_information.ProductDescription).decode()))
        print(" Major: " + repr(x_device_information.Major))
        print(" Minor: " + repr(x_device_information.Minor))
        print(" Release: " + repr(x_device_information.Release))

def test_status(lib, device_id):
    print("\nGet status")
    x_status = status_t()
    result = lib.get_status(device_id, byref(x_status))
    print("Result: " + repr(result))
    if result == Result.Ok:
        print("Status.Ipwr: " + repr(x_status.Ipwr))
        print("Status.Upwr: " + repr(x_status.Upwr))
        print("Status.Iusb: " + repr(x_status.Iusb))
        print("Status.Flags: " + repr(hex(x_status.Flags)))

def test_get_position(lib, device_id):
    print("\nRead position")
    x_pos = get_position_t()
    result = lib.get_position(device_id, byref(x_pos))
    print("Result: " + repr(result))
    if result == Result.Ok:
        print("Position: {0} steps, {1} microsteps".format(x_pos.Position, x_pos.uPosition))
    return x_pos.Position, x_pos.uPosition

def test_left(lib, device_id):
    print("\nMoving left")
    result = lib.command_left(device_id)
    print("Result: " + repr(result))

def test_move(lib, device_id, distance, udistance):
    print("\nGoing to {0} steps, {1} microsteps".format(distance, udistance))
    result = lib.command_move(device_id, distance, udistance)
    print("Result: " + repr(result))

def test_wait_for_stop(lib, device_id, interval):
    print("\nWaiting for stop")
    result = lib.command_wait_for_stop(device_id, interval)
    print("Result: " + repr(result))

def test_serial(lib, device_id):
    print("\nReading serial")
    x_serial = c_uint()
    result = lib.get_serial_number(device_id, byref(x_serial))
    if result == Result.Ok:
        print("Serial: " + repr(x_serial.value))

def test_get_speed(lib, device_id)        :
    print("\nGet speed")
    # Create move settings structure
    mvst = move_settings_t()
    # Get current move settings from controller
    result = lib.get_move_settings(device_id, byref(mvst))
    # Print command return status. It will be 0 if all is OK
    print("Read command result: " + repr(result))    
    
    return mvst.Speed
        
def test_set_speed(lib, device_id, speed):
    print("\nSet speed")
    # Create move settings structure
    mvst = move_settings_t()
    # Get current move settings from controller
    result = lib.get_move_settings(device_id, byref(mvst))
    # Print command return status. It will be 0 if all is OK
    print("Read command result: " + repr(result))
    print("The speed was equal to {0}. We will change it to {1}".format(mvst.Speed, speed))
    # Change current speed
    mvst.Speed = int(speed)
    # Write new move settings to controller
    result = lib.set_move_settings(device_id, byref(mvst))
    # Print command return status. It will be 0 if all is OK
    print("Write command result: " + repr(result))    
    

def test_set_microstep_mode_256(lib, device_id):
    print("\nSet microstep mode to 256")
    # Create engine settings structure
    eng = engine_settings_t()
    # Get current engine settings from controller
    result = lib.get_engine_settings(device_id, byref(eng))
    # Print command return status. It will be 0 if all is OK
    print("Read command result: " + repr(result))
    # Change MicrostepMode parameter to MICROSTEP_MODE_FRAC_256
    # (use MICROSTEP_MODE_FRAC_128, MICROSTEP_MODE_FRAC_64 ... for other microstep modes)
    eng.MicrostepMode = MicrostepMode.MICROSTEP_MODE_FRAC_256
    # Write new engine settings to controller
    result = lib.set_engine_settings(device_id, byref(eng))
    # Print command return status. It will be 0 if all is OK
    print("Write command result: " + repr(result))

print ("imported pyximc")

dt = datetime.datetime.now()
value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
print(value.strftime('%Y-%m-%d %H:%M:%S'))

print("Library loaded")

sbuf = create_string_buffer(64)
lib.ximc_version(sbuf)
print("Library version: " + sbuf.raw.decode().rstrip("\0"))

# Set bindy (network) keyfile. Must be called before any call to "enumerate_devices" or "open_device" if you
# wish to use network-attached controllers. Accepts both absolute and relative paths, relative paths are resolved
# relative to the process working directory. If you do not need network devices then "set_bindy_key" is optional.
# In Python make sure to pass byte-array object to this function (b"string literal").
lib.set_bindy_key(r'D:\soft\STANDA\ximc-2.9.14\ximc\win64\keyfile.sqlite'.encode("utf-8"))

# This is device search and enumeration with probing. It gives more information about devices.
probe_flags = EnumerateFlags.ENUMERATE_PROBE + EnumerateFlags.ENUMERATE_NETWORK
enum_hints = b"addr=192.168.0.1,172.16.2.3"
# enum_hints = b"addr=" # Use this hint string for broadcast enumerate
devenum = lib.enumerate_devices(probe_flags, enum_hints)
print("Device enum handle: " + repr(devenum))
print("Device enum handle type: " + repr(type(devenum)))

dev_count = lib.get_device_count(devenum)
print("Device count: " + repr(dev_count))

controller_name = controller_name_t()
for dev_ind in range(0, dev_count):
    enum_name = lib.get_device_name(devenum, dev_ind)
    result = lib.get_enumerate_device_controller_name(devenum, dev_ind, byref(controller_name))
    if result == Result.Ok:
        print("Enumerated device #{} name (port name): ".format(dev_ind) + repr(enum_name) + ". Friendly name: " + repr(controller_name.ControllerName) + ".")

open_name = "xi-com:\\\\.\COM32"

if not open_name:
    exit(1)

if type(open_name) is str:
    open_name = open_name.encode()

print("\nOpen device " + repr(open_name))
device_id = lib.open_device(open_name)
print("Device id: " + repr(device_id))

test_info(lib, device_id)
test_status(lib, device_id)
test_set_microstep_mode_256(lib, device_id)
startpos, ustartpos = test_get_position(lib, device_id)

#go to origin
print('go to origin')
test_move(lib, device_id,100,100)
test_wait_for_stop(lib, device_id, 1000)
print('Succesfull: go to origin')

print('DEV_TYPE')
devices = pixet.devicesByType(pixet.PX_DEVTYPE_TPX3)
print('devices = ', devices)
dev = devices[0]
print('dev = ', dev)

print('def customAcq')
def customAcq(AngleNumber,acqCount,acqTime,waitTime):
    for i in range(AngleNumber+1): 
       # acqCount = 100
        outputFile = "D:/soft/STANDA/test/%i.clog" % (i)
        
        print('start to write output file')
        rc = dev.doSimpleAcquisition(acqCount, acqTime, 1, outputFile)
        #print "Acquition: %d" % rc    
        print ("Frame: %d" % i)
        time.sleep(waitTime) 

numberOfAnglePositions = 7
#exposeTime=180

for i in range(numberOfAnglePositions):
    print("GantryPosition:",i)
    startpos = i*5000
    ustartpos = 0
    test_move(lib, device_id, startpos, ustartpos)
    test_wait_for_stop(lib, device_id, 100)
    acqCount = 100
    acqTime = 0.001
    waitTime = 0.3
    #customAcq(i,acqCount,acqTime,waitTime)
    outputFile = "D:/soft/STANDA/test4/%i.clog" % (i)
        
    print('start to write output file')
    rc = dev.doSimpleAcquisition(acqCount, acqTime, 1, outputFile)
    #print "Acquition: %d" % rc    
    print ("Frame: %d" % i)
    time.sleep(waitTime) 


    # make data driven acquisition for N seconds and save to file:
    #res=dev.doAdvancedAcquisition(1, exposeTime, pixet.PX_ACQTYPE_DATADRIVEN, pixet.PX_ACQMODE_NORMAL, pixet.PX_FTYPE_AUTODETECT, 0, "/media/Data/Scans/ForFedja/17062021/Pattern_without_M3/" + "{:03d}".format(i) + ".pmf")

    dt = datetime.datetime.now()
    value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
    print(value.strftime('%Y-%m-%d %H:%M:%S'))


print("\nClosing")
lib.close_device(byref(cast(device_id, POINTER(c_int))))
print("Done")