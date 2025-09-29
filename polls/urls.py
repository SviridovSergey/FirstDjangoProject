from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.SurveyListView(), name='survey_list'),
    path('survey/<int:survey_id>/', views.views.survey_detail, name='survey_detail'),
    path('thank-you/<int:reponse_id>/', views.thank_you, name='survey_thank_you')
]