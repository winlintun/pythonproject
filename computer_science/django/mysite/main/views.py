from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.
# html & css and js code


def index(response, id):
	ls = ToDoList.objects.get(id=id)
	item = ls.item_set.get(id=1)
	return HttpResponse("<h1>%s</h1></br></br><p>%s</p>" % (ls.name, item.text))