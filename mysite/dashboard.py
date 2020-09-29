from django.shortcuts import render
from pathlib import Path
from classes.application import Application
from django.core.paginator import Paginator

import csv
import os
import array


BASE_DIR = Path(__file__).resolve().parent.parent
csv_path =  os.path.join(BASE_DIR, '', 'home-credit-default-risk', 'application_train.csv')

def index(request):
    applications = getApplicationsList()
    page_number = request.GET.get('page', 1)
    p = Paginator(applications, 25)
    applications = p.page(page_number)
    context = {
        'applications': applications,
    }

    
    return render(request,'dashboard.html',context)


def detail(request, application_id):
    application = getApplication(application_id)
    context = {
        'application': application
    }
    return render(request, 'detail.html', context)


def getApplicationsList():
    applications = []
    with open(csv_path) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        for i,row in enumerate(reader):
            new_application = Application(
                SK_ID_CURR = row[0],
                TARGET = row[1],
                NAME_CONTRACT_TYPE = row[2],
                CODE_GENDER = row[3],
                FLAG_OWN_CAR = row[4],
                FLAG_OWN_REALTY = row[5]
            )
            applications.append(new_application)
            #if(i >= 600):
            #    break
    return applications

def getApplication(application_id):

    with open(csv_path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] == str(application_id):
                return Application(
                    SK_ID_CURR = row[0],
                    TARGET = row[1],
                    NAME_CONTRACT_TYPE = row[2],
                    CODE_GENDER = row[3],
                    FLAG_OWN_CAR = row[4],
                    FLAG_OWN_REALTY = row[5],
                    CNT_CHILDREN = row[6],
                    AMT_INCOME_TOTAL = row[7],
                    AMT_CREDIT = row[8],
                    AMT_ANNUITY = row[9],
                    AMT_GOODS_PRICE = row[10],
                    NAME_TYPE_SUITE = row[11],
                    NAME_INCOME_TYPE = row[12],
                    NAME_EDUCATION_TYPE = row[13],
                    NAME_FAMILY_STATUS = row[14],
                    NAME_HOUSING_TYPE = row[15],
                    REGION_POPULATION_RELATIVE = row[16]
                )
    return False

