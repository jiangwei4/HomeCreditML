from django.shortcuts import render
from forms.dataForm import DataForm
from django.http import HttpResponse
from datetime import datetime, timedelta, date
import joblib
import pandas as pd


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


def prediction_post(request):
    organisation_type = request.POST.get("ORGANIZATION_TYPE", "")
    code_gender = request.POST.get("CODE_GENDER", "")
    days_birth = request.POST.get("DAYS_BIRTH", "")
    region_rating = request.POST.get("REGION_RATING_CLIENT_W_CITY", "")
    ext_source_1 = request.POST.get("EXT_SOURCE_1", "")
    ext_source_2 = request.POST.get("EXT_SOURCE_2", "")
    ext_source_3 = request.POST.get("EXT_SOURCE_3", "")

    today = date.today()
    d = datetime.strptime(days_birth, "%m/%d/%Y").date()
    days_birth = d-today

    loaded_model = joblib.load('F:\\wamp64\\www\\api_home_credit\\api_home_credit\\media\\modelRandomForestClassifier')
    val = {'ORGANIZATION_TYPE':[organisation_type],
        'CODE_GENDER':[code_gender],
        'DAYS_BIRTH':[days_birth.days],
        'REGION_RATING_CLIENT_W_CITY':[region_rating],
        'EXT_SOURCE_1':[float(ext_source_1)],
        'EXT_SOURCE_2':[float(ext_source_2)],
        'EXT_SOURCE_3':[float(ext_source_3)]}
    val = pd.DataFrame(data=val)

    loaded_pipeline = joblib.load('F:\\wamp64\\www\\api_home_credit\\api_home_credit\\media\\sklearn_pipeline.pkl')
    val = loaded_pipeline.transform(val)
    prediction = loaded_model.predict_proba(val)

    return HttpResponse(prediction)