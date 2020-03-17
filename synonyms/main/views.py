from django.shortcuts import render
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

# Create your views here.
def search_view(request):
	msg =""
	context = {}
	synonyms = []
	if request.method=='POST':
		
		word_search = request.POST['q']
		for syn in wordnet.synsets(word_search):
			for l in syn.lemmas():
				synonyms.append(l.name())
	print(synonyms)
	s = set(synonyms)
	lst = ','.join(synonyms)
	print(lst)
	if request.method=='POST':
		if lst:
			lst = lst
		
		else:
			msg = 'No synonyms available'

		
	context['lst'] = lst
	context['msg'] = msg




	return render(request, 'home.html', context)