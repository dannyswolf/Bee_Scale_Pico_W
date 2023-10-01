from datetime import datetime
from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import January, February, March, April, May, June, July, August, September, October, November, December
import struct

lists_of_months = [January, February, March, April, May, June, July, August, September, October, November, December]

"""
print("dir(request)", dir(request))
['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', 
 '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', 
 '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', 
 '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 
 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 
 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 
 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
 
print("request.headers", request.headers)
 {'Content-Length': '12', 'Content-Type': 'text/plain', 'Client': '192.168.1.230:8080', 'Connection': 'keep-alive,close', 
 'User-Agent': 'Pico W', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
 'Accept-Encoding': 'gzip, deflate', 'Dnt': '1', 'Accept-Language': 'el,en-US;q=0.7,en;q=0.3'}
"""


def add_weight(request, *args, **kwargs):
    """
    Αυτό είναι για απευθείας εισαγωγή δεδομένων απο το pico W με urequest μέθοδο
    πλέων το κάνω με το mqtt_client αρχείο
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    print("request", request)
    print("request.headers", request.headers)
    # print("request.read()", request.read())
    if request.method == 'GET':
        # το request.headers['Client'] το στέλνω εγώ απο το pico δεν υπάρχει κανονικά
        # request.headers {'Host': '192.168.1.232', 'User-Agent': 'Pico W', 'Connection': 'keep-alive, close', 'Client': '192.168.1.234', 'Content-Length': '26'}
        if request.headers['User-Agent'] == 'Pico W' and request.headers['Client'] == '192.168.1.234':
            # binary_string = request.read().decode().split(",")
            client_ip = request.headers['Client']
            print("client_ip", client_ip)
            data = request.read()
            print("data", data)
            decoded_data = data.decode().split(" ")
            print("decoded_data", decoded_data)
            # print("binary_string", binary_string)
            weight = decoded_data[0]  # Είναι το μήνυμα που στέλνει το pico w Σε κιλά
            pico_temp = decoded_data[1]  # Είναι το μήνυμα που στέλνει το pico w Σε κιλά
            volts = decoded_data[2]
            temp = decoded_data[3]
            humidity = decoded_data[4]
            Battery_Volts = decoded_data[5]
            Shunt_Voltage = decoded_data[6]
            Current = decoded_data[7]
            Power = decoded_data[8]
            today_month_number = datetime.today().month  # Επιστέφει μόνο τον αριθμό του μήνα, 12 αν είναι Δεκέμβρης
            # - 1 γιατί η λίστα ξεκινάει απο 0
            # Κάνω new_obj apo το mqtt_client.py
            new_obj = lists_of_months[today_month_number - 1].objects.create(Βάρος=weight, Pico_Θερμοκρασία=pico_temp,
                                                                            Volts=volts, Temp=temp, Humidity=humidity,
                                                                             Battery_Volts=Battery_Volts,
                                                                             Shunt_Voltage=Shunt_Voltage,
                                                                             Current=Current, Power=Power)

            response_data = {'client_ip': client_ip, "weight": weight, "temp": temp,
                             'User-Agent': request.headers['User-Agent']}
            return JsonResponse(response_data, status=200)
        return HttpResponse(status=200)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Current Month
        month_now = datetime.today().month
        # -1 γιατί ι λίστα ξεκινάει απο 0 ενω month_now ξεκινάει απο 1
        month_obj = lists_of_months[month_now - 1]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = f"{month_obj.__name__}"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class JanuaryView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[0]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Ιανουάριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class FebruaryView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[1]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Φεβρουάριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class MarchView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[2]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Μάρτιος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class AprilView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[3]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Μάρτιος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class MayView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[4]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Μάιος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class JuneView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[5]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Ιούνιος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class JulyView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[6]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Ιούλιος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class AugustView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[7]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Αύγουστος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class SeptemberView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[8]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Σεπτέμβριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class OctoberView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[9]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Οκτώβριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class NovemberView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[10]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Νοέμβριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


class DecemberView(View):

    def get(self, request, *args, **kwargs):
        month_obj = lists_of_months[11]
        month_qs = month_obj.objects.all()
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        chartLabel = "Δεκέμβριος"
        context = {
            "labels": labels,
            "chartLabel": chartLabel,
            "data_context": month_qs,
        }
        return render(request, 'scale/index.html', context)


## using rest_framework classes

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    lists_of_months = [January, February, March, April, May, June, July, August, September, October, November, December]

    def get(self, request, format=None):
        context = {}
        for month in lists_of_months:
            serialized_data = serialize("json", month.objects.all())
            serialized_data = json.loads(serialized_data)
            context[f'{month.__name__}'] = serialized_data
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July'
            'August',
            'September',
            'October',
            'November',
            'December',
        ]
        chartLabel = "my data"
        # chartdata = [jan_objs, feb_objs, mar_objs, apr_objs, may_objs, jun_objs, jul_objs, aug_objs, sep_objs, okt_objs, nov_objs, dec_objs]
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": context,
        }
        return Response(data)
