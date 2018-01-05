from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Result
from django.views import generic
from .forms import SubmitForm
import json
import traceback


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
				self.score += 5
			index += 1
		self._record()

	def _record(self):
		res, created = Result.objects.update_or_create(StdID=self.stuID, defaults={"Score":self.score, "Json_Str":json.dumps(self.stuAnswer)})

	def getScore(self):
		return self.score

# for index page
def index(request):
	form = SubmitForm()

	# 如果是用POST的方式進來這邊
	if request.method == 'POST' and request.POST:
		data = request.POST 
		data=data.dict()
		# 如果輸入的格式JSON無法處理，則render show_error頁面
		try:
			stuAnswer = json.loads(data['answer'])
			if len(stuAnswer) != 20:
				error_type = '輸入答案長度不符規定'
				error_message = '目前輸入長度為' + str(len(stuAnswer))
				return render(request, 'scoring/show_error.html', locals())
			stuID = data['studentID']
			scOB = Scoring('QandA/Answer_for_examples.json', stuAnswer, stuID)
			scOB.scoring()
		except Exception as e:
			error_type = str(type(e))
			error_message = str(e)
			return render(request, 'scoring/show_error.html', locals())

		return redirect('scoring:table')

	return render(request, 'scoring/index.html', locals())


# for displaying the result table
class IndexView(generic.ListView):
	template_name = 'scoring/table.html'
	context_object_name = 'all_result'

	def get_queryset(self):
		return Result.objects.all()
