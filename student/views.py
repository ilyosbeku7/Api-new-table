from django.shortcuts import render
from .models import User
from django.views import View

# Create your views here.
class ProfileView( View):
    
    def get(self, request):
        users=User.objects.all()
        return render(request, 'student/index.html', {'users':users})