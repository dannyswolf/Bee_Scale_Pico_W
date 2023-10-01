from django.urls import path, include
from .views import (add_weight, HomeView, ChartData, JanuaryView, FebruaryView, MarchView, AprilView, MayView,
                    JuneView, JulyView, AugustView, SeptemberView, OctoberView, NovemberView)

app_name = 'scale'
urlpatterns = [
    # path('', OpelCallsListView.as_view(), name="calls_list_view"),
    path('add/', add_weight, name='add_weight'),
    path('', HomeView.as_view()),
    path('January/', JanuaryView.as_view()),
    path('February/', FebruaryView.as_view()),
    path('March/', MarchView.as_view()),
    path('April/', AprilView.as_view()),
    path('May/', MayView.as_view()),
    path('June/', JuneView.as_view()),
    path('July/', JulyView.as_view()),
    path('August/', AugustView.as_view()),
    path('September/', SeptemberView.as_view()),
    path('October/', OctoberView.as_view()),
    path('November/', NovemberView.as_view()),
    path('December/', JanuaryView.as_view()),
    # path('test-api', views.get_data),
    path('api', ChartData.as_view()),
    # path('add_spare_part/<int:service_id>/<int:calendar_id>', add_spare_part_to_call, name='add_spare_part'),
    # path('add_spare_part/<int:service_id>/<int:calendar_id>/<str:app_label>/<int:part_id>', add_spare_part_post, name='add_spare_part_form'),
    # path('closed_calls/', ClosedCallsListView.as_view(), name="closed_calls"),
    # path('edit/<int:calendar_id>', EditCall.as_view(), name='edit_call'),
    # path('edit/<int:calendar_id>/delete/', DeleteCall.as_view(), name='delete_call'),
    # path('edit/delete_file/<int:service_id>/<str:file_name>', delete_files, name='delete_file'),
    # path('create/<int:machine_id>', CreateCall.as_view(), name='create_call'),
    # path('search', search_calendar_dte, name='search_dte'),
    
    
]

