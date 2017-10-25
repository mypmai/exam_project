# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from ..login_app.models import User

# Create your views here.
def main(request):
	if 'first_name' not in request.session:
		return redirect('/')
		
	context={
		"user": User.objects.get(id=request.session['id']),
		"otheruser": User.objects.exclude(id=request.session['id']),
	}
	return render(request,'exam_app/main.html',context)

def show(request,id):
	context={
		'user':User.objects.get(id=id),
	}
	return render(request,'exam_app/show.html',context)

def addfriend(request,id):
	user= User.objects.get(id=request.session['id'])
	newfriend=User.objects.get(id=id)
	newfriend.friend.add(user)
	return redirect('/main')
def remove(request,id):
	remove=User.objects.get(id=id)
	remove.friend.clear()
	return redirect('/main')