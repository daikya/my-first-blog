from django.urls import path
from . import views
# urlパターンの追加。
urlpatterns = [
        path('', views.post_list, name='post_list'),
]
