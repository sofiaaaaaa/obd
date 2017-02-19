import obd
from obd import OBDStatus

# connecting ELM
connection = obd.OBD()

"""
# Check connection status
if connection.status() == OBDStatus.NOT_CONNECTED:
    print("ELM is not connected")

elif connection.status() == OBDStatus.ELM_CONNECTED:
    print("ELM is connected")

elif connection.status() == OBDStatus.CAR_CONNECTED:
    print("Car is connected")
"""

# Check if a response is empty
dataList = {}

speed = connection.query(obd.commands.SPEED)
if not speed.is_null():
    dataList["SPEED"] = str(speed.value)

intake_pressure = connection.query(obd.commands.INTAKE_PRESSURE)
if not intake_pressure.is_null():
    dataList["INTAKE_PRESSURE"] = str(intake_pressure.value)

intake_temp = connection.query(obd.commands.INTAKE_TEMP)
if not intake_temp.is_null():
    dataList["INTAKE_TEMP"] = str(intake_temp.value)

rpm = connection.query(obd.commands.RPM)
if not rpm.is_null():
    dataList["RPM"] = str(rpm.value)

maf = connection.query(obd.commands.MAF)
if not maf.is_null():
    dataList["MAF"] = str(maf.value)

coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
if not coolant_temp.is_null():
    dataList["COOLANT_TEMP"] = str(coolant_temp.value)

fuel_level = connection.query(obd.commands.FUEL_LEVEL)
if not fuel_level.is_null():
    dataList["FUEL_LEVEL"] = str(fuel_level.value)

ambiant_air_temp = connection.query(obd.commands.AMBIANT_AIR_TEMP)
if not ambiant_air_temp.is_null():
    dataList["AMBIANT_AIR_TEMP"] = str(ambiant_air_temp.value)

oil_temp = connection.query(obd.commands.OIL_TEMP)
if not oil_temp.is_null():
    dataList["OIL_TEMP"] = str(oil_temp.value)

control_module_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
if not control_module_voltage.is_null():
    dataList["CONTROL_MODULE_VOLTAGE"] = str(control_module_voltage.value)


print(dataList)