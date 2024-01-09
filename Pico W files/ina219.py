# https://github.com/DFRobot/DFRobot_INA219/blob/master/Python/RespberryPi/DFRobot_INA219.py
# CONVERTED TO MICROPYTHON FROM CHATGPT
from credentials import secrets
import machine
import time

DEBUG = secrets['DEBUG']

class INA219:

    _INA219_READ = 0x01

    INA219_I2C_ADDRESS1 = 0x40  # I2C ADDRESS 1
    INA219_I2C_ADDRESS2 = 0x41  # I2C ADDRESS 2
    INA219_I2C_ADDRESS3 = 0x44  # I2C ADDRESS 3
    INA219_I2C_ADDRESS4 = 0x45  # I2C ADDRESS 4 The I2C address defaults to 0x45, https://wiki.dfrobot.com/Gravity%3A%20I2C%20Digital%20Wattmeter%20SKU%3A%20SEN0291

    INA219_CONFIG_RESET = 0x8000  # Config reset register
    _INA219_REG_CONFIG = 0x00  # Config register

    bus_vol_range_16V = 0  # Voltage range ±16V
    bus_vol_range_32V = 1  # Voltage range ±32V
    # GAIN and range for PGA (Shunt Voltage Only)
    PGA_bits_1 = 0  # GAIN:1, Range ±40 mV
    PGA_bits_2 = 1  # GAIN:/2, Range ±80 mV
    PGA_bits_4 = 2  # GAIN:/4, Range ±160 mV
    PGA_bits_8 = 3  # GAIN:/8, Range ±320 mV

    adc_bits_9 = 0  # Resolution is 9bit
    adc_bits_10 = 1  # Resolution is 10bit
    adc_bits_11 = 2  # Resolution is 11bit
    adc_bits_12 = 3  # Resolution is 12bit
    # Size of the sample collected by adc every time
    adc_sample_1 = 0
    adc_sample_2 = 1
    adc_sample_4 = 2
    adc_sample_8 = 3
    adc_sample_16 = 4
    adc_sample_32 = 5
    adc_sample_64 = 6
    adc_sample_128 = 7

    power_down = 0  # Power-down
    shunt_vol_trig = 1  # Shunt voltage, triggered
    bus_vol_trig = 2  # Bus voltage, triggered
    shunt_and_bus_vol_trig = 3  # Shunt and bus, triggered
    adc_off = 4  # ADC off (disabled)
    shunt_vol_con = 5  # Shunt voltage, continuous
    bus_vol_con = 6  # Bus voltage, continuous
    shunt_and_bus_vol_con = 7  # Shunt and bus, continuous

    _INA219_REG_SHUNTVOLTAGE = 0x01  # Shunt Voltage Register
    _INA219_REG_BUSVOLTAGE = 0x02  # Bus Voltage Register
    _INA219_REG_POWER = 0x03  # Power Register
    _INA219_REG_CURRENT = 0x04  # Current Register
    _INA219_REG_CALIBRATION = 0x05  # Register Calibration

    def __init__(self, i2c_bus, i2c_addr):
        self.i2c_bus = i2c_bus
        self.i2c_addr = i2c_addr
        
    def begin(self):
        '''
          @fn begin
          @brief Initialize I2C bus and configure INA219 config register before reading data
          @return True (succeeded)/False (failed)
        '''
        if not self.scan():
            return False
        else:
            self.cal_value = 4096
            self.set_bus_RNG(self.bus_vol_range_16V)
            self.set_PGA(self.PGA_bits_1) # GAIN:1, Range ±40 mV
            self.set_bus_ADC(self.adc_bits_12, self.adc_sample_8)
            self.set_shunt_ADC(self.adc_bits_12, self.adc_sample_8)
            self.set_mode(self.shunt_and_bus_vol_con)
            return True
    
    def linear_cal(self, ina219_reading_mA, ext_meter_reading_mA):
        '''!
        @fn linear_cal
        @brief Linear calibration
        @param ina219_reading_mA    The current measured by INA219 (before calibration)
        @param ext_meter_reading_mA  Actual measured current
        '''
        ina219_reading_mA = float(ina219_reading_mA)
        ext_meter_reading_mA = float(ext_meter_reading_mA)
        self.cal_value = int((ext_meter_reading_mA / ina219_reading_mA) * self.cal_value) & 0xFFFE
        self._write_register(self._INA219_REG_CALIBRATION, self.cal_value)

    def reset(self):
        '''!
        @fn reset
        @brief Reset config register
        '''
        self._write_register(self._INA219_REG_CONFIG, self._INA219_CONFIG_RESET)

    def _write_register(self, register, value):
        self.i2c_bus.writeto(self.i2c_addr, bytearray([register, (value >> 8) & 0xFF, value & 0xFF]))

    def _read_register(self, register):
        data = bytearray(2)
        self.i2c_bus.writeto(self.i2c_addr, bytearray([register]))
        self.i2c_bus.readfrom_into(self.i2c_addr, data)
        return (data[0] << 8) | data[1]

    def get_bus_voltage_V(self):
        '''!
        @fn get_bus_voltage_V
        @brief  get the BusVoltage (Voltage of IN- to GND)
        @return Voltage unit:V
        '''
        return float(self._read_register(self._INA219_REG_BUSVOLTAGE) >> 1) * 0.001

    def get_shunt_voltage_mV(self):
        '''
        @fn get_shunt_voltage_mV
        @brief  get the ShuntVoltage (Voltage of the sampling resistor, IN+ to NI-)
        @return Voltage unit:V
        '''
        return float(self._read_register(self._INA219_REG_SHUNTVOLTAGE)) * 0.001

    def get_current_mA(self):
        '''
        @fn get_current_mA
        @brief get the Current (Current flows across IN+ and IN-.
        @n If the current flows from IN+ to IN-, the reading is positive.
        @n If the current flows from IN- to IN+, the reading is negative)
        @return Current unit:mA
        '''
        return float(self._read_register(self._INA219_REG_CURRENT))
    
    def get_power_mW(self):
        '''
        @fn get_power_mW
        @brief  get the Power (in milliwatts)
        @return Power unit: mW
        '''
        return float(self._read_register(self._INA219_REG_POWER)) * 20

    def set_bus_RNG(self, value):
        '''
        @fn set_bus_RNG
        @brief  Set BRNG (Bus Voltage Range)
        @param value     bus_vol_range_16V < 16V >
        @n               bus_vol_range_32V < 32V >
        '''
        conf = self._read_register(self._INA219_REG_CONFIG)
        conf &= ~(0x01 << 13)
        conf |= value << 13
        self._write_register(self._INA219_REG_CONFIG, conf)

    def set_PGA(self, bits):
        '''
        @fn set_PGA
        @brief  Set PGA parameter (Shunt Voltage Only)
        @param bits          PGA_bits_1 <GAIN:1,Range ±40 mV>
        @n                   PGA_bits_2 <GAIN:/2,Range ±80 mV>
        @n                   PGA_bits_4 <GAIN:/4,Range ±160 mV> 
        @n                   PGA_bits_8 <GAIN:/8,Range ±320 mV> 
        '''
        conf = self._read_register(self._INA219_REG_CONFIG)
        conf &= ~(0x03 << 11)
        conf |= bits << 11
        self._write_register(self._INA219_REG_CONFIG, conf)
        
    def set_bus_ADC(self, bits, sample):
        '''!
        @fn set_bus_ADC
        @brief  Set BADC parameter (Bus ADC Resolution/Averaging)
        @param bits           Resolution
        @n                    adc_bits_9,
        @n                    adc_bits_10,
        @n                    adc_bits_11,
        @n                    adc_bits_12
        @param sample         Sample size
        @n                    adc_sample_1,
        @n                    adc_sample_2,
        @n                    adc_sample_4,
        @n                    adc_sample_8,
        @n                    adc_sample_16,
        @n                    adc_sample_32,
        @n                    adc_sample_64,
        @n                    adc_sample_128
        '''
        conf = self._read_register(self._INA219_REG_CONFIG)
        value = 0

        if bits < self.adc_bits_12 and sample > self.adc_sample_1:
            return
        if bits < self.adc_bits_12:
            value = bits
        else:
            value = 0x80 | sample

        conf &= ~(0x0F << 7)
        conf |= value << 7
        self._write_register(self._INA219_REG_CONFIG, conf)

    def set_shunt_ADC(self, bits, sample):
        '''!
        @fn set_shunt_ADC
        @brief  Set SADC parameter (Shunt ADC Resolution/Averaging)
        @param bits           Resolution
        @n                    adc_bits_9,
        @n                    adc_bits_10,
        @n                    adc_bits_11,
        @n                    adc_bits_12
        @param sample         Sample size
        @n                    adc_sample_1,
        @n                    adc_sample_2,
        @n                    adc_sample_4,
        @n                    adc_sample_8,
        @n                    adc_sample_16,
        @n                    adc_sample_32,
        @n                    adc_sample_64,
        @n                    adc_sample_128
        '''
        conf = self._read_register(self._INA219_REG_CONFIG)
        value = 0

        if bits < self.adc_bits_12 and sample > self.adc_sample_1:
            return
        if bits < self.adc_bits_12:
            value = bits
        else:
            value = 0x80 | sample

        conf &= ~(0x0F << 3)
        conf |= value << 3
        self._write_register(self._INA219_REG_CONFIG, conf)
        
    def set_mode(self, mode):
        '''
        @fn set_mode
        @brief  Set operation Mode
        @param mode  
        @n                power_down,   <Power-down> 
        @n                shunt_vol_trig,    <Shunt voltage, triggered> 
        @n                bus_vol_trig,    <Bus voltage, triggered>  
        @n                shunt_and_bus_vol_trig,<Shunt and bus, triggered>  
        @n                adc_off,      <ADC off (disabled)> 
        @n                shunt_vol_con,     <Shunt voltage, continuous>  
        @n                bus_vol_con,     <Bus voltage, continuous>  
        @n                shunt_and_bus_vol_con   <Shunt and bus, continuous> 
        '''
        conf = self._read_register(self._INA219_REG_CONFIG)
        conf &= ~0x07
        conf |= mode
        self._write_register(self._INA219_REG_CONFIG, conf)

    def read_ina_reg(self, reg):
        buf = bytearray(2)
        self.i2c_bus.writeto(self.i2c_addr, bytearray([reg]))
        self.i2c_bus.readfrom_into(self.i2c_addr, buf)

        value = (buf[0] << 8) | buf[1]
        if (value & 0x8000):
            return -((value ^ 0xFFFF) + 1)
        else:
            return value

    def scan(self):
        try:
            self.i2c_bus.readfrom(self.i2c_addr, 1)
            return True
        except Exception as e:
            print("I2C init fail:", e)
            return False
        



def get_battery_volts():
    i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))  # Replace with your I2C configuration
    i2c.scan() 
    ina219 = INA219(i2c, INA219.INA219_I2C_ADDRESS4)  # Replace with your I2C address
    if DEBUG:
        if ina219.begin():
            print("INA219 initialization succeeded.")
        else:
            print("INA219 initialization failed.")
    #time.sleep(1)
    bus_voltage = ina219.get_bus_voltage_V() # Voltage of IN- to GND
    shunt_voltage = ina219.get_shunt_voltage_mV() # Voltage of the sampling resistor, IN+ to NI-
    current = ina219.get_current_mA() # Current flows across IN+ and IN-
    power = ina219.get_power_mW()
    ina219.set_mode(ina219.power_down)    # = 0 Power-down
    if DEBUG:
        print(f"Bus Voltage: {bus_voltage} V --- Shunt Voltage: {shunt_voltage} V --- Current: {current} mA  ---- Power: {power} mW")
    return  [bus_voltage,shunt_voltage,current,power]

#while True:
#    get_battery_volts()
#    time.sleep(2)
    
