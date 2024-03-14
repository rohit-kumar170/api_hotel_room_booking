from django.urls import path
from . import views
urlpatterns = [
    path('book/',views.book_room,name='book_room'),
    path('availability/<int:room_number>/',views.check_availability,name='check_availability'),
    path('test/',views.test_api,name='test'),
]
