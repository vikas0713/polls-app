from django.urls import path

from polls.views import polls, rate, create_poll, poll_details

urlpatterns = [
    path('poll-list/', polls),
    path('poll-create/', create_poll, name='create_poll'),
    path('poll-details/<int:poll_id>/', poll_details, name='poll_details'),
    path('rate/<int:poll_id>/', rate, name='rate'),
]
