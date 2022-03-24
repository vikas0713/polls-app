from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from polls.models import Poll


@login_required(login_url='/login')
def polls(request):
    return render(request, 'polls.html', {"polls_list": Poll.objects.all()})


def rate(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.rating += 1
    poll.save()
    return HttpResponseRedirect('/polls/poll-list/')


@login_required(login_url='/login')
def create_poll(request):
    if request.POST:
        title = request.POST.get("title")
        description = request.POST.get("description")
        Poll.objects.create(title=title,description=description)
        return HttpResponseRedirect('/polls/poll-list')
    return render(request, 'poll-form.html', {})


@login_required(login_url='/login')
def poll_details(request, poll_id):
    # if request.user.is_authenticated:
    return render(request, 'poll-details.html', {"poll": Poll.objects.get(id=poll_id)})
    # else:
    #     return HttpResponseRedirect('/login')


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
