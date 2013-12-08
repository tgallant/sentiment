from django.shortcuts import render
from forms import SentimentForm, SubmitRedirect
from django.http import HttpResponse 
from TextAnalysis import Analysis

def form(request):
    form = SentimentForm()
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form == "":
            render(request, 'pages/home.html')
    return render(request, 'pages/home.html', {'form': form})

def analysis(request):
    form2 = SubmitRedirect()
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            txt = str(form.cleaned_data['text'])
            x = Analysis(txt)
            sent = x.sentiment()
            sc = x.spellcheck()[0]
            words = ', '.join(x.spellcheck()[1])
            y = x.syllablecount()
            totalsyll = y[0]
            totalwords = y[1]
            syll = y[2]
            return render(request, 'pages/analysis.html', {'totalsyll': totalsyll, 'totalwords': totalwords, 'words': words, 
                                                           'form2': form2, 'txt': txt, 'sent': sent, 'sc': sc, 'syll': syll})
        if form == "":
            render(request, 'pages/home.html')
