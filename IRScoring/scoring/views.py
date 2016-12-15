from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Result
from django.views import generic
from .forms import SubmitForm
import json

class Scoring(object):
	"""docstring for scoring"""
	def __init__(self, answerPath, stuAnswer, stuID):
		with open(answerPath, 'r') as f:
			self.answer = json.load(f)
		self.stuAnswer = stuAnswer
		self.score  = 0
		self.stuID = stuID

	def scoring(self):
		index = 0
		for i in self.answer:
			if self.stuAnswer[index] == i:
				self.score+=1
			index+=1
		self._record()

	def _record(self):
		res, created = Result.objects.update_or_create(StdID=self.stuID, defaults={"Score":self.score, "Json_Str":json.dumps(self.stuAnswer)})

	def getScore(self):
		return self.score
# for index page
def index(request):
	form = SubmitForm()

	# 如果是用POST的方式進來這個function
	if request.method == 'POST' and request.POST:
		# 如果是POST，就再產生一個變數接request.POST的東西，並將之與form.py裡面的格式結合
		data = request.POST 
		data=data.dict()
		stuAnswer = json.loads(data['answer'])
		stuID = data['studentID']

		scOB = Scoring('answer.json', stuAnswer, stuID)
		scOB.scoring()

		return redirect('scoring:table')

	return render(request, 'scoring/index.html', locals())


# for displaying the result table
class IndexView(generic.ListView):
	template_name = 'scoring/table.html'
	context_object_name = 'all_result'

	def get_queryset(self):
		return Result.objects.all()