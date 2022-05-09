from django.urls import path
from basic import views

# TEMPLATE TAGGING
app_name = 'basic'
urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('others/', views.other, name = 'other'),
]
