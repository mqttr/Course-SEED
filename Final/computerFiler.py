import serial
import csv
import datetime

ser = serial.Serial('COM3', 9600) # change the serial port name as needed

ser.flushInput()



with open('VoltageLevel.csv', 'a',newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['Day','Time', 'Voltage'])

    print("Intialized")
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline().decode().rstrip()
            voltage = int(data)
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            writer.writerow([date,timestamp, voltage])
            print([date,timestamp, voltage])
            csvfile.flush()
