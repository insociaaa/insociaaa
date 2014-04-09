from django.shortcuts import render

# Create your views here.
def expedia(request):
  return render(request, 'expedia.html')
