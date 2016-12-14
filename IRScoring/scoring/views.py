from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Result
from django.views.generic.edit import CreateView
from django.views import generic


# index
def index(request):

    return render(request, 'scoring/index.html')


class IndexView(generic.ListView):
    template_name = 'scoring/table.html'
    context_object_name = 'all_result'

    def get_queryset(self):
        return Result.objects.all()


def table_create(request):
    std_id = request.POST.get('ID', False)
    json_str = request.POST.get('content', False)

    return HttpResponse(std_id + "  " + json_str)


