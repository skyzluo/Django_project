from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.views import generic


#def index(request):
#    return HttpResponse("Hello, world. You're at the site home page.")
#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'mysite/index.html')