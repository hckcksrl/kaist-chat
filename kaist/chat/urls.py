from kaist.chat.views import FCLT
from django.urls import path


urlpatterns = [
     path('menu', FCLT.as_view())
]