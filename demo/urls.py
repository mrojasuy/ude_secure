from django.urls.conf import path
from demo.views import Index

app_name = 'demo'
urlpatterns = [
    path("", Index.as_view(), name="index"),
]