from django.shortcuts import render

def post_list(request):
    return render(request, 'projects/post_list.html', {})

# Create your views here.
