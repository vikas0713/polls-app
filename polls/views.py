from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from polls.forms import PollForm
from polls.models import Poll


@login_required(login_url='/login')
def polls(request):
    return render(request, 'polls.html', {"polls_list": Poll.objects.all()})


def rate(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.rating += 1
    poll.save()
    return JsonResponse(data={"rating": poll.rating, "title": poll.title})


@login_required(login_url='/login')
def create_poll(request):
    if request.POST:
        form = PollForm(request.POST, files=request.FILES)
        if form.is_valid():
            poll = form.save()
            return HttpResponseRedirect('/polls/poll-list')
    return render(request, 'poll-form.html', {"form": PollForm})


@login_required(login_url='/login')
def poll_details(request, poll_id):
    return render(request, 'poll-details.html', {"poll": Poll.objects.get(id=poll_id)})


def login_user(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/polls/poll-list/')
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'login.html', {})
