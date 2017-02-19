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
    dataList["SPEED"] = speed.value

intake_pressure = connection.query(obd.commands.INTAKE_PRESSURE)
if not intake_pressure.is_null():
    dataList["INTAKE_PRESSURE"] = intake_pressure.value

intake_temp = connection.query(obd.commands.intake_temp)
if not intake_temp.is_null():
    dataList["INTAKE_TEMP"] = intake_temp.value

rpm = connection.query(obd.commands.rpm)
if not rpm.is_null():
    dataList["RPM"] = rpm.value

maf = connection.query(obd.commands.maf)
if not maf.is_null():
    dataList["MAF"] = maf.value

coolant_temp = connection.query(obd.commands.coolant_temp)
if not coolant_temp.is_null():
    dataList["COOLANT_TEMP"] = coolant_temp.value

fuel_level = connection.query(obd.commands.fuel_level)
if not fuel_level.is_null():
    dataList["FUEL_LEVEL"] = fuel_level.value

ambiant_air_temp = connection.query(obd.commands.ambiant_air_temp)
if not ambiant_air_temp.is_null():
    dataList["AMBIANT_AIR_TEMP"] = ambiant_air_temp.value

oil_temp = connection.query(obd.commands.oil_temp)
if not oil_temp.is_null():
    dataList["OIL_TEMP"] = oil_temp.value

control_module_voltage = connection.query(obd.commands.control_module_voltage)
if not control_module_voltage.is_null():
    dataList["CONTROL_MODULE_VOLTAGE"] = control_module_voltage.value


print(dataList)