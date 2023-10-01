from django.contrib import admin
from .models import January, February, March, April, May, June, July, August, September, October, November, December



# class CalendarAdminInLine(admin.StackedInline):
#     model = Calendar
#     extra = 0
#     # fields = ['Ημερομηνία', 'ΔΤΕ', "Customer_id__Επωνυμία_Επιχείρησης","Copier_ID__Εταιρεία"]

class JanuaryAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = January

class FebruaryAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = February

class MarchAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = March

class AprilAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = April

class MayAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = May

class JuneAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = June

class JulyAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = July

class AugustAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = August

class SeptemberAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = September

class OctoberAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = October

class NovemberAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = November

class DecemberAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Ημερομηνία', 'Ωρα', 'Βάρος', 'Pico_Θερμοκρασία', 'Volts', 'Temp', 'Humidity', 'Battery_Volts', 'Shunt_Voltage', 'Current', 'Power']
    search_fields = ['Ημερομηνία', 'Ωρα', "Βάρος"]
    class Meta:
        model = December


admin.site.register(January, JanuaryAdmin)
admin.site.register(February, FebruaryAdmin)
admin.site.register(March, MarchAdmin)
admin.site.register(April, AprilAdmin)
admin.site.register(May, MayAdmin)
admin.site.register(June, JuneAdmin)
admin.site.register(July, JulyAdmin)
admin.site.register(August, AugustAdmin)
admin.site.register(September, SeptemberAdmin)
admin.site.register(October, OctoberAdmin)
admin.site.register(November, NovemberAdmin)
admin.site.register(December, DecemberAdmin)


