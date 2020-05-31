from django.shortcuts import get_object_or_404, render
from .forms import HomeForm

def calculation(request):
    form = HomeForm()
    text1 = 0
    text2 = 0
    act = ''
    result = 0
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            text1 = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            act = form.cleaned_data['action']
            if act == '+':
                result = text1 + text2
            elif act == '-':
                result = text1 - text2
            elif act == '*':
                result = text1 * text2
            elif act == '/':
                result = text1 / text2


    args = {'form': form,
            'num1': text1,
            'num2': text2,
            'act':act,
            'result': result
            }

    return args

def index(request):
    args = calculation(request)
    return render(request, 'calculator/index.html', args)

def result(request):
    args = calculation(request)
    return render(request, 'calculator/result.html', args)





