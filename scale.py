# WORKS https://github.com/robert-hh/hx711
# Printing anything to console however appears to break deep sleep
# https://ghubcoder.github.io/posts/pico-w-deep-sleep-with-micropython/
from machine import Pin, ADC
from hx711_gpio import HX711
import time
from credentials import secrets

DEBUG = secrets['DEBUG']

pin_OUT = Pin(4, Pin.IN, pull=Pin.PULL_DOWN) # data_pin
pin_SCK = Pin(5, Pin.OUT) # clock_pin
# pin_OUT.on
# pin_SCK.on

hx = HX711(pin_SCK, pin_OUT)


# hx.tare()


# hx711.read()
# Returns the actual raw value of the load cell. Raw means: not scaled, no offset compensation.

# hx711.read_lowpass()
# Returns the actual value of the load cell fed through an one stage IIR lowpass filter.
# The properties of the filter can be set with set_time_constant().

# hx711.set_time_constant(value=None)
# Set the time constant used by hx711.read_lowpass(). The range is 0-1.0. Smaller values means longer times to settle and better smoothing.
# If value is None, the actual value of the time constant is returned.

# hx711.get_value()
# Returns the difference of the filtered load cell value and the offset, as set by hx711.set_offset() or hx711.tare()

# hx711.get_units()
# Returns the value delivered by hx711.get_value() divided by the scale set by hx711.set_scale().

# hx711.tare(times=15)
# Determine the tare value of the load cell by averaging times raw readings.

# hx711.power_down()
# Set the load cell to sleep mode.

# Για calibration βαζουμε να διαβάσει αυτό χωρίς καθόλου βάρος
def calibration():
    # ΠΑΝΩ ΚΑΠΑΚΙ 	=  2160
    # ΚΟΥΤΑΚΙ PICO  =  360
    # ΚΑΤΩ ΚΑΠΑΚΙ 	=  2930
    # ΜΠΑΤΑΡΙΑ 		=  2040
    # ΟΛΑ ΜΑΖΙ 		=  7490
    # ΚΑΤΩ ΚΑΠΑΚΙ 	+ ΚΟΥΤΑΚΙ PICO =  3290
    # w = 3290
    
    hx.power_up()
    hx.set_gain(64)
    time.sleep_ms(50)
    offset = hx.read_average(100) # επιστρέφει 6 ψηφία πριν την τελεία
    # Αφου πάντα θα έχει βάρος εβαλα μερικές τιμές που εβγαλε χωρίς βάρος
    # offset = (247144.6 + 247177.0 + 248031.8 + 247330.9 + 247626.2 ) / 5   # 27/7/2023
    print(f"offset {offset}")
    # αυτές ειναι οι τιμές που παίρνει με το βάρος που ξέρουμε
    # apply the weight
    # Δοκιμή να κάνω tare πριν πάρω τιμές με βάρος -- αποτέλεσμα δεν ειδα διαφορά 
    # hx.tare()
    # read = hx.read() # Returns the actual raw value of the load cell. Raw means: not scaled, no offset compensation.
    # print(f"read {read}")
    w = float(input("Γράψε πόσα γραμμάρια έβαλες και enter: "))
    r_load = hx.read_average(100)  # επιστρέφει 6 ψηφία πριν την τελεία
    print("r_load", r_load)
    # Δεν το χρειαζόμαστε να το ορίσουμε γιατί πέρνουμε απαυθείας το scaling και το οριζουμε ποιο κάτω με σταθερές τιμές 

    scaling = (r_load - offset) / w  # επιστρέφει 2 ψηφία πριν την τελεία
    # scaling = ( 21.99008 + 21.12412 + 21.43893 + 22.72987 + 22.86604 ) / 5   # 27/7/2023 
    print("scaling", scaling)

    # hx.set_offset(offset)
    # hx.set_scale(scaling)
    # units = hx.get_units()
    # print("units", units)
    weight = (hx.read_average(100) - offset) / scaling / 1000 # /1000 για να γίνουν κιλά kg ανάγνωση_μέσος όρος
    print("weight", weight)
    
    while True:
        # hx.tare()
        time.sleep(2)
        
        if hx.is_ready():
            weight1 = (hx.read_average(100) - offset) / scaling / 1000 # /1000 για να γίνουν κιλά kg ανάγνωση_μέσος όρος
            print(f"weight1 {weight1} kg  Διαφορά απο αυτό που έβαλα w {w} είναι: {((weight1 * 1000) - w) / 1000} kg")
            # weight2 = (hx.read_average(100) - offset) / scaling / 1000 # /1000 για να γίνουν κιλά kg ανάγνωση_μέσος όρος
            # print(f"weight2 {weight2} kg Διαφορά απο αυτό που έβαλα w {w} είναι: {((weight2 * 1000) - w) / 1000} kg")
        
        else:
            time.sleep(0.5)

# Gain 64 7/9/2023 SparkFun red HX711 ΤΙΣ ΠΙΟ ΣΤΑΘΕΡΕΣ ΤΙΜΕΣ
offset =  (  116012.1 + 115738.4 + 116054.8 ) / 3
scaling = (  10.23411 + 10.22676 + 11.07288 ) / 3

# Gain 128 6/9/2023 Vbus -> green Hx711 --> E+ E- A+ A-
#offset =  (  230269.8 + 229977.4 ) / 2
#scaling = (  19.97207 + 19.81562  ) / 2

# Gain 64 03/9/2023 POWER VBUS --> E+  PICO W GND --> E-
#offset =  (  142366.4 )
#scaling = (  12.77151 )

# Gain 64 29/8/2023 POWER VSYS E+     ασταθές ~1.7kg
#offset =  (  121991.3 +  108328.7) / 2
#scaling = (  9.600487 +  11.36467) / 2

# 9/8/2023
# offset = (225976.9 + 226632.8 + 226931.8 + 227085.7 + 227164.1 + 227684.6 + 227507.4) / 7
# scaling = ( 21.66586 + 21.79234 + 21.61346 + 21.3706 + 21.58702 + 21.48988 + 21.44592) / 7 

# 26/8/23
# offset = (200529.7 + 199972.2 + 199194.0 + 208173.5 + 204909.9 + 221279.8 + 222112.2) / 7 
# scaling = (21.42539 + 25.23673 + 24.37118 + 21.84423 + 26.46416 + 20.18019 + 23.72991 ) / 7

# Gain 128 29/8/2023 POWER VSYS E+ 
# offset = (223940.0  + 231542.2 + 232502.2 + 238473.0 + 241107.0) / 5
# scaling = (20.51777 + 23.30654 + 21.79071 + 19.26788) / 4


# Gain 128 29/8/2023 POWER VSYS --> A+ 
# offset =  (-22349.53) 
# scaling = (-0.05804284) 

# Gain 128 29/8/2023 POWER VSYS --> HX711  --> E+ KAI VSYS --> E+  πολύ ασταθές -3kg 
# offset =  (225128.6 + 225428.2 + 224636.9 + 225328.3) / 4
# scaling = (21.28717 + 20.35855 + 20.66859 + 19.90348) / 4

#gain 64 26/8/2023
# offset = (114889.5 + 112394.6 + 112343.9 + 112324.9 + 112508.6 + 112563.8 + 112545.2 + 112522.7 + 112522.3 + 113311.7 + 116294.0) / 11
# scaling = (10.09476 + 11.8163 + 10.49575 + 11.50566 + 11.53026 + 11.53999 + 11.54562 + 11.56497 + 11.56892 + 11.53587 + 11.53695) / 11
 
# Gain 64 direct 5v to E+ Gnd to E-
# offset = (138696.7   )
# scaling = (13.09548 )

# Gain 128 direct 5v to E+ Gnd to E-
# offset = (274743.3  + 275244.6 )
# scaling = (26.52515 + 25.61722 )

# Gain 128 direct 3v to E+ Gnd to E-
# offset = (183708.3  )
# scaling = (17.44316  )

# Gain 64 direct 3v to E+ Gnd to E-
# offset = (93266.46  )
# scaling = (8.803121  )

# Gain 64 direct Vbus to E+ Gnd to E-  ΕΧΕΙ ΤΙΣ ΜΙΚΡΟΤΕΡΕΣ ΑΠΟΚΛΗΣΕΙΣ -- ΣΕ ΜΑΓΑΛΑ ΒΑΡΟΙ ΧΑΝΕΙ ΠΑΝΩ ΑΠΟ 1400gr
# offset = (145897.3  + 146293.0 + 146733.1) / 3
# scaling = (13.73555 + 13.80091 + 13.62284) / 3

# Gain 64 direct Vbus to HX711  
# offset = (113162.6  )
# scaling = (10.4156  )

def get_weight():
    try:
        pin_OUT.on()
        pin_SCK.on()
        hx.power_up()
        hx.set_gain(64)
        time.sleep(2)
        if hx.is_ready():
            hx.tare()
            if DEBUG:
                print("hx is ready read_average(100)")
            # hx.set_offset(114889.5) # 26/8/2023
            # hx.set_scale(10.09476)  # 26/8/2023
            # Διαπίστωσα οτι αν ξαναδιαβάσουμε το δευτερο νούμερο είναι ποιο κοντά στην πραγματικότητα
            # 9/8/23 Το ιδιο νούμερο βγάζει και την δευτερη φορά
            weight = (hx.read_average(100) - offset) / scaling / 1000 # / 1000 για να γίνουν κιλά
            if DEBUG:
                print("weight1", float(weight))
            hx.power_down()
            pin_OUT.low()
            pin_SCK.low()
            return float(weight)
        else:
            if DEBUG:
                print("hx is not ready sleep(2)")
            time.sleep(2)
            get_weight()
    except Exception as e:
        hx.power_down()
        pin_OUT.low()
        pin_SCK.low()
        filename = "log.txt"
        file = open(filename, "a")
        file.write(f"\nscale.py get_weight() Exception: {e}")
        file.close()
        if DEBUG:
            print(f"\nscale.py get_weight() Exception: {e}")
        return 


# calibration()

# Get Weight loop
#while True:
#    weight = get_weight()
   # print("weight...", weight)
#    time.sleep(1)


# Read offset amd scaling
#while True:
#    # offset = hx.read_average(200)
#    print("offset", offset)
#    w = float(input("Γράψε πόσα γραμμάρια έβαλες και enter: "))
#    r_load = hx.read_average(200)  # επιστρέφει 6 ψηφία πριν την τελεία
#    print("r_load", r_load)

#    scaling = (r_load - offset) / w  # επιστρέφει 2 ψηφία πριν την τελεία
#    print("scaling", scaling)
#    weight = (r_load  - offset) / scaling / 1000
#    print("weight", weight)
    