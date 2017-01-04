from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
# def index(request):
# #     return HttpResponse("hoge!")
# #     return HttpResponse(template.render({}, request))
#     return render(request, 'sample_app/index.html', {})

class IndexTemplateView(TemplateView):
#     template_name = 'index.html'
    template_name = 'sample_app/index.html'
