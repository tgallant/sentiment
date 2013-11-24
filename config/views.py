from django.shortcuts import render
from forms import SentimentForm, SubmitRedirect
from django.http import HttpResponse 
from sentiment2 import sentiment

def form(request):
    form = SentimentForm()
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            txt = str(form.cleaned_data['text'])
            txt_analysis = str(sentiment(txt))
            return render(request, 'pages/home.html', {'txt': txt, 'txt_analysis': txt_analysis})
        if form == "":
            render(request, 'pages/home.html')
    return render(request, 'pages/home.html', {'form': form})

def analysis(request):
    form2 = SubmitRedirect()
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            txt = str(form.cleaned_data['text'])
            txt_analysis = str(sentiment(txt))
            return render(request, 'pages/analysis.html', {'txt': txt, 'txt_analysis': txt_analysis, 'form2': form2})
        if form == "":
            render(request, 'pages/home.html')
