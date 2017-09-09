from django.contrib import messages  # flash the successful msg
# HttpResponseRedirect:it redirects to the detail page after updating or
# creating a post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import *
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
# login page#redirect = to redirect user to any specified page after login
from django.shortcuts import render, redirect
# login page#authenticate:to check the entered fields with existing ones in db
from django.contrib.auth import authenticate, login
from django.views.generic import View  # login page
import datetime


def event_create(request):
    if not request.user.is_staff or not request.user.is_superuser:  # imp
        raise Http404

    # request.FILES or None:for images
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success

        return HttpResponseRedirect('/')  # redirects to detail page
    context = {
        "form": form,
    }
    return render(request, "events/event_form.html", context)


def event_list(request):

	now =datetime.datetime.now() 
	ongoing = Event.objects.all().filter(start_date__lte= now , end_date__gte=now) 
	upcoming= Event.objects.all().filter(start_date__gte=now)
	past = Event.objects.all().filter(end_date__lte=now)
	full_list = []
	category_list = []
	for items in ongoing:
		items.category = "ongoing"
		full_list.append(items)
	for items in upcoming:
		items.category = "upcoming"
		full_list.append(items)
	for items in past:
		items.category = "past"
		full_list.append(items)


	#queryset_list = Event.objects.all().order_by("-timestamp") # order_by("-timestamp") : to order posts in increasing timestamp
	#if request.user.is_staff or request.user.is_superuser:
		#queryset_list = Event.objects.all().order_by("-timestamp")
	"""query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
			Q(event_name__icontains=query) |
			Q(content__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 1000) # Show 25 contacts per page
	page_request_var ="page"
	page = request.GET.get("page_request_var")


	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)"""

	context = {
	"queryset1": full_list,
	"queryset2": category_list
	}
	return render(request, "events/event_list.html",context)

def event_update(request,slug = None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Event, slug =slug)
	form =EventForm(request.POST or None,request.FILES or None,instance = instance )
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		# message success
		
		return HttpResponseRedirect('/') #redirects to detail page

	context = {
			"instance":instance,
			"title": instance.event_name,   
			 #inside context we declare variables which can be used in html files
			"form":form,
	}

	return render(request,"events/event_form.html",context)

    
   

def event_delete(request, slug=None):

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Succesfully deleted")
    return redirect("/events/event_list.html/")


# in url.py it is taking two arguments request and id hence here also we
# have to pass two
def event_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)

    context = {
        "instance": instance,
        # inside context we declare variables which can be used in html files
        "title": instance.event_name,

    }

    return render(request, "event_detail.html", context)


# def event_update(request, slug=None):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     instance = get_object_or_404(Post, slug=slug)
#     form = EventForm(
#         request.POST or None,
#         request.FILES or None,
#         instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         # message success

#         return HttpResponseRedirect(
#             instance.get_absolute_url())  # redirects to detail page

#     context = {
#         "instance": instance,
#         "title": instance.event_name,
#         # inside context we declare variables which can be used in html files
#         "form": form
#     }

#     return render(request, "event_form.html", context)
