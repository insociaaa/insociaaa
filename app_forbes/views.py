from django.shortcuts import render

# Create your views here.
def forbes(request):
  return render(request, 'forbes.html')
