from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.SurveyListView.as_view(), name='survey_list'),
    path('survey/<int:survey_id>/', views.survey_detail, name='survey_detail'),
    path('thank-you/<int:response_id>/', views.thank_you, name='survey_thank_you'),
]