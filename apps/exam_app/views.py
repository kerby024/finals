from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Friend
from ..logreg_app.models import User

def display(request):
    me = Friend.objects.filter(poked_id = request.session['id'])
    check = Friend.objects.filter(poked_id=request.session['id']).annotate(num=Count('user'))
    print check
    context = {
        'users' :User.objects.exclude(id = request.session['id']),
        'me': me
    }
    return render(request, 'exam_app/display.html', context)


def counter(request, pokedid):
    Friend.objects.addpokes(request.session['id'], pokedid)
    return redirect ('/pokes')


def clear(request):
    request.session.flush()
    print 'clear'
    return redirect ('/')

