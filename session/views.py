from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class HomeView(APIView):
    def get(self, request):
        return render(request, 'home.html')
    

def testsession(request):
    if request.session.get('test', False):
        print(request.session['test'])
    # request.session.set_expiry(10000000)
    request.session['test'] = "testing"
    request.session['test2'] = "testing2"
    return render(request, 'sessiontest.html')