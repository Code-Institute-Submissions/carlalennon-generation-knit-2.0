from django.shortcuts import render
from django.views import generic
from .models import Pattern
from django.views.generic import TemplateView
from .forms import PostPattern

# Create your views here.
class PatternView(generic.ListView):
    queryset = Pattern.objects.all()
    template_name = "pattern/index.html"
    paginate_by = 3


class UploadPatternView(CreateView):
    pass