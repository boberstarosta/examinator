from django.urls import path
from exams import views


urlpatterns = [
	path('', views.home_page_view, name='home')
]
