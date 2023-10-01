# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

"""
I got a field with attribute unique, which was not unique [eg 2-time same value]
Error -->>  django.db.utils.IntegrityError: UNIQUE constraint failed:
python3 manage.py migrate --fake
then
python3 manage.py makemigrations
python3 manage.py migrate
"""

# Create your models here.
class January(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'January'
        verbose_name_plural = 'Ιανουάριος'
        verbose_name = 'Ιανουάριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage", help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class February(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'February'
        verbose_name_plural = 'Φεβρουάριος'
        verbose_name = 'Φεβρουάριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class March(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'March'
        verbose_name_plural = 'Μάρτιος'
        verbose_name = 'Μάρτιος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class April(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'April'
        verbose_name_plural = 'Απρίλιος'
        verbose_name = 'Απρίλιος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class May(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'May'
        verbose_name_plural = 'Μάιος'
        verbose_name = 'Μάιος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class June(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'June'
        verbose_name_plural = 'Ιούνιος'
        verbose_name = 'Ιούνιος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class July(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'July'
        verbose_name_plural = 'Ιούλιος'
        verbose_name = 'Ιούλιος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class August(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'August'
        verbose_name_plural = 'Αυγουστος'
        verbose_name = 'Αυγουστος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class September(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'September'
        verbose_name_plural = 'Σεπτέμβριος'
        verbose_name = 'Σεπτέμβριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class October(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'October'
        verbose_name_plural = 'Οκτώβριος'
        verbose_name = 'Οκτώβριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class November(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'November'
        verbose_name_plural = 'Νοέμβριος'
        verbose_name = 'Νοέμβριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)


class December(models.Model):
    class Meta:
        managed = True
        ordering = ['-pk']
        db_table = 'December'
        verbose_name_plural = 'Δεκέμβριος'
        verbose_name = 'Δεκέμβριος'

    ID = models.AutoField(db_column='ID', primary_key=True, blank=False, null=False)
    Ημερομηνία = models.DateField(db_column='Ημερομηνία', auto_now_add=True, help_text="Αυτόματη  εισαγωγή "
                                                                                       "Ημερομηνίας δεδομένων")
    Ωρα = models.TimeField(db_column="Ωρα", auto_now_add=True, help_text="Αυτόματη εισαγωγή ώρας δεδομένων")
    Βάρος = models.FloatField(db_column="Βάρος", help_text="βάρος σε KG")
    Pico_Θερμοκρασία = models.FloatField(db_column="Θερμοκρασία", help_text="Θερμοκρασία Pico W", default=0.0)
    Volts = models.FloatField(db_column="Volts", help_text="Volts που έχει το VSYS", default=0.0)
    Battery_Volts = models.FloatField(db_column="BatterY_Volts", help_text="Voltage of IN- to GND", default=0.0)
    Shunt_Voltage = models.FloatField(db_column="Shunt_Voltage",
                                      help_text="Voltage of the sampling resistor, IN+ to NI-", default=0.0)
    Current = models.FloatField(db_column="Current", help_text="Current flows across IN+ and IN-", default=0.0)
    Power = models.FloatField(db_column="Power", help_text="Watt σε mW", default=0.0)
    Temp = models.FloatField(db_column="Temp", help_text="Θερμοκρασία χώρου", default=0.0)
    Humidity = models.FloatField(db_column="Humidity", help_text="Υγρασία χώρου", default=0.0)
