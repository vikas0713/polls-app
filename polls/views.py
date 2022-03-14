from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from polls.models import Poll


def polls(request):
    return render(request, 'polls.html', {"polls_list": Poll.objects.all()})


def rate(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.rating += 1
    poll.save()
    return HttpResponseRedirect('/polls/poll-list/')


def create_poll(request):
    if request.POST:
        title = request.POST.get("title")
        description = request.POST.get("description")
        Poll.objects.create(title=title,description=description)
        return HttpResponseRedirect('/polls/poll-list')
    return render(request, 'poll-form.html', {})


def poll_details(request, poll_id):
    return render(request, 'poll-details.html', {"poll": Poll.objects.get(id=poll_id)})

