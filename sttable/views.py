import logging
import base64
import sys
import datetime, json
from datetime import datetime, timedelta , time
from json import JSONEncoder
import json
from decimal import Decimal
from django.utils.dateparse import parse_date
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
from django.template import Context, Template
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import get_language
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render , redirect
from.models import Students, Teachers, Principal



class Index(View):
    template_name = "index.html"
    def get(self , request):
        print("HOMEEEE")

        stt_data = []

        stt = Students.objects.all()

        for ht in stt:
            data = {
                "id" : ht.id,
                "name" : ht.name,
                "email" : ht.email,
                "number" : ht.number,
            }

            stt_data.append(data)


        teach_data = []

        teach = Teachers.objects.all()

        for ar in teach:
            data = {
                "id" : ar.id,
                "name" : ar.name,
                "email" : ar.email,
                "number" : ar.number,
            }

            teach_data.append(data)

            
        prin_data = []

        prin = Principal.objects.all()

        for pr in prin:
            data = {
                "id" : pr.id,
                "name" : pr.name,
                "email" : pr.email,
                "number" : pr.number,
            }

            prin_data.append(data)


        context = {
            'stt' : stt_data,
            'all_stt' : json.dumps(list(stt_data)),
            'teach' : teach_data,
            'all_teach' : json.dumps(list(teach_data)),
            'prin' : prin_data,
            'all_prin': json.dumps(list(prin_data)),
        }


        return render(request , self.template_name , context)
    
    def post(self , request):

        print("INNNNSIDE POST")

        form_id = request.POST.get('stt_id')

        db_param = request.POST.dict()

        print("DB Param1 = ",db_param)   

        del db_param['csrfmiddlewaretoken']
        del db_param['stt_id']
        del db_param['role']

        print("DB Param222 = ",db_param)        

        if(form_id == '0'):
            db_param['created_time'] = datetime.now()
            if(request.POST.get('role') == '1'):
               Teachers.objects.create(**db_param)
            elif(request.POST.get('role') == '2'):
               Students.objects.create(**db_param)
            else:
               Principal.objects.create(**db_param)    
            return redirect('index')
        else:
            print("Update")
            db_param['updated_time'] = datetime.now()
            if(request.Post.get('role') == '2'):
                Students.objects.filter(id = int(form_id)).update(**db_param)

            return redirect('index')
        
     






        