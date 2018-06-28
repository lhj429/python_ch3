from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/index.html', context)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def delete(request):
    # if request.GET['password'] == :
    # guestbook_list =
    # Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()

    # return HttpResponseRedirect('/guestbook')