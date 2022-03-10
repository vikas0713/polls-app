from django.urls import path

from polls.views import polls, rate, create_poll

urlpatterns = [
    path('poll-list/', polls),
    path('poll-create/', create_poll, name='create_poll'),
    path('rate/<int:poll_id>/', rate, name='rate'),
]
