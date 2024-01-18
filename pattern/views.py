from django.shortcuts import render
from django.views import generic
from .models import Pattern
from django.http import HttpResponse
from django.shortcuts import render
def upload_media(request):
    return render(request, 'media_app/upload_media.html')

# Create your views here.
class PatternView(generic.ListView):
    queryset = Pattern.objects.all()
    template_name = "pattern/index.html"
    paginate_by = 3

def patterns(request):
    myPatterns = Pattern.objects.all()
    template = loader.get_template('index.html')
    context = {
        'myPatterns' : myPatterns,
    }
    return HttpResponse(template.render(context, request))
    
def upload_media(request):
    return render(request, 'media_app/upload_media.html')