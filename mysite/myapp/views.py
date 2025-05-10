from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    template = loader.get_template('second.html')
    template = loader.get_template('third.html')
    return HttpResponse(template.render())