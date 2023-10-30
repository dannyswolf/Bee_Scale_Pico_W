from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView, LogoutView
from admin_material.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from datetime import datetime
from scale.models import January, February, March, April, May, June, July, August, September, October, November, December

lists_of_months = [January, February, March, April, May, June, July, August, September, October, November, December]





def login_view(request):
    if request.user.is_authenticated and request.method == "GET":
        return render(request, 'logout.html')

    if request.method == 'GET' and  not request.user.is_authenticated:
        return render(request, "login.html")

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'base.html')

    else:
        context = {"error": "Το όνομα χρήστη ή ο κωδικός πρόσβασης σας δεν ταιριάζουν!"}
        # Return an 'invalid login' error message.
        return render(request, "login.html", context=context)


def home_view(request):
    return render(request, "index.html")


# Create your views here.


# Pages Είναι η πρώτη σελίδα που εμφανίζεται http://bee-scale:8080/
def index(request):
    month_now = datetime.today().month
    # -1 γιατί η λίστα ξεκινάει απο 0 ενω month_now ξεκινάει απο 1
    month_obj = lists_of_months[month_now - 1]
    # Latest values of every month
    max_values_list = []
    min_values_list = []
    not_empty_max_values_list = []
    not_empty_min_values_list = []
    # βάζω το πρώτο γιατί η κάθε class επιστέφει ordering = ['-pk'] ανάποδα
    for month in lists_of_months:
        obj = month.objects.order_by('-Βάρος').first()
        obj1 = month.objects.order_by('Βάρος').first()
        max_values_list.append(obj)
        min_values_list.append(obj1)
        if obj is not None:
            not_empty_max_values_list.append(obj)
        if obj1 is not None:
            not_empty_min_values_list.append(obj1)

    first_max_value_obj = not_empty_max_values_list[0]
    latest_max_value_obj = not_empty_max_values_list[-1]

    first_min_value_obj = not_empty_min_values_list[0]
    latest_min_value_obj = not_empty_min_values_list[-1]

    max_temp = month_obj.objects.order_by('-Temp').first()
    max_weight = month_obj.objects.order_by('-Βάρος').first()
    min_weight = month_obj.objects.order_by('Βάρος').first()
    max_Pico_temp = month_obj.objects.order_by('-Pico_Θερμοκρασία').first()
    max_Humidity = month_obj.objects.order_by('-Humidity').first()

    # Για να πάρω τελευταία τάση του Battery_Volts
    latest_obj = month_obj.objects.first()
    # max 14v 100%
    #min 10v 0% # μετά δε θα δουλεύει το router που θέλει 9V
    # αρα η διαφορά τους είναι 4
    # (x-10) * 100 / 4 το αποτέλεσμα είναι το ποσοστό που θέλουμε
    battery_percent = round(((latest_obj.Battery_Volts - 10)  * 100) / 4)
    # print("battery_percent", battery_percent)

    # Επιστέφει τα τελευταία 24 δεδομένα
    month_qs = month_obj.objects.all().order_by('-ID')[:24][::-1]
    # Το πρώτο obj απο τα τελευταία 24
    first_obj = month_qs[0]
    # 24 ωρη διαφορά με τρία δεκαδικά πίσω απο το κόμμα
    difference = round(float(latest_obj.Βάρος - first_obj.Βάρος), 3)

    labels = [
        'Ιανουάριος',
        'Φεβρουάριος',
        'Μάρτιος',
        'Απρίλιος',
        'Μάιος',
        'Ιούνιος',
        'Ιούλιος',
        'Αύγουστος',
        'Σεπτέμβριος',
        'Οκτώβριος',
        'Νοέμβριος',
        'Δεκέμβριος'
    ]
    chartLabel = f"{month_obj.__name__}"
    context = {
        "labels": labels,
        "chartLabel": chartLabel,
        "data_context": month_qs,
        "max_temp": max_temp.Temp,
        "max_temp_date": max_temp.Ημερομηνία,
        "max_temp_time": max_temp.Ωρα,
        "max_Βάρος": max_weight.Βάρος,
        "max_Βάρος_date": max_weight.Ημερομηνία,
        "max_Βάρος_time": max_weight.Ωρα,
        "min_weight": min_weight.Βάρος,
        "min_weight_date": min_weight.Ημερομηνία,
        "min_weight_time": min_weight.Ωρα,
        "max_Pico_temp": max_Pico_temp.Pico_Θερμοκρασία,
        "max_Pico_date": max_Pico_temp.Ημερομηνία,
        "max_Pico_time": max_Pico_temp.Ωρα,
        "max_Humidity": max_Humidity.Humidity,
        "max_Humidity_date": max_Humidity.Ημερομηνία,
        "battery_percent": battery_percent,
        "max_Humidity_time": max_Humidity.Ωρα,
        "latest_obj": latest_obj,
        "max_values_list": max_values_list,
        "first_max_value_obj": first_max_value_obj,
        "latest_max_value_obj": latest_max_value_obj,
        "min_values_list": min_values_list,
        "first_min_value_obj": first_min_value_obj,
        "latest_min_value_obj": latest_min_value_obj,
        'first_obj': first_obj,
        'difference': difference,

    }
    return render(request, 'pages/index.html', context)


# Authentication
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def logout_view(request):
    logout(request)
    return redirect('/')



