from django.shortcuts import render
from forms.dataForm import DataForm

def index(request):
    return render(request, 'index.html')



def create(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            prediction = form.cleaned_data
            return HttpResponseRedirect('/prediction_post')
            pass  # does nothing, just trigger the validation
    else:
        form = DataForm()
    return render(request, 'dataForm.html', {'form': form})