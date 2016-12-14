from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Result
from django.views import generic
from .forms import SubmitForm
# from django.views.generic.edit import CreateView
# from django.template import loader


# for index page
def index(request):
    form = SubmitForm()
    return render(request, 'scoring/index.html', {'form': form})


# for displaying the result table
class IndexView(generic.ListView):
    template_name = 'scoring/table.html'
    context_object_name = 'all_result'

    def get_queryset(self):
        return Result.objects.all()


# for receiving the form, computing the score and redirecting to table.html
def table_create(request):
    # 如果是用POST的方式進來這個function
    if request.method == 'POST':
        # 如果是POST，就再產生一個變數接request.POST的東西，並將之與form.py裡面的格式結合
        form = SubmitForm(data=request.POST)

        if form.is_valid():
            std_id = form.cleaned_data.get('Std_ID')
            json_str = form.cleaned_data.get('Json_Str')
            print('Mayday==> ' + json_str + " <==END")
            print('try it out=> ' + std_id + " <=thanks")
            print(type(json_str))
            print('test test test test test test ')

            return HttpResponse('<h2> Hello World</h2>')
        else:
            return HttpResponse('<h2> Its not valid</h2>')

    # 如果是用GET的方式進來這個function
    else:
        form = SubmitForm()

    return render(request, 'scoring/index.html', {'form': form})


"""
def table_create(request):
    std_id = request.POST['ID']
    json_str = request.POST['content']

    std_id = str(std_id)
    json_str = str(json_str)

    return HttpResponse(std_id + "  " + json_str)
"""


