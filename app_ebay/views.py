from django.shortcuts import render

# Create your views here.
def ebay(request):
  return render(request, 'ebay.html')
