from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import Form1, Form2
from .models import InfoModel
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import requests
from mailchimp3 import MailChimp


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)


def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


class Form1View(TemplateView):

    def get(self, request):
        form = Form1
        return render(request, 'form1_post.html', {
            'form': form,
        })

    @csrf_exempt
    def post(self, request):
        form = Form1(request.POST or None)
        if form.is_valid():
            info_model = InfoModel.objects.filter(email=form.instance.email)
            if info_model.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
            return redirect('form1_list')
        else:
            return HttpResponse('Error! Email is not valid!')


class Form1ListView(TemplateView):

    def get(self, request):
        emails = InfoModel.objects.all()
        return render(request, 'form1_list.html', {
            'emails': emails,
        })


class Form2View(TemplateView):

    def get(self, request):
        form = Form2
        return render(request, 'form2_post.html', {
            'form': form,
        })

    @csrf_exempt
    def post(self, request):
        form = Form2(request.POST or None)
        if form.is_valid():
            info_model = InfoModel.objects.filter(email=form.instance.email)
            if info_model.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
            return redirect('form2_list')
        else:
            return HttpResponse('Error! Email is not valid!')


class Form2ListView(TemplateView):

    def get(self, request):
        emails = InfoModel.objects.all()
        return render(request, 'form2_list.html', {
            'emails': emails,
        })


