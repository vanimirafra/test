from django.shortcuts import render
from .models import Tutorial


# Create your views here.
def home(request):
    return render(request, 'test2.html', context = {"tutorials":Tutorial.objects.all})

def home(request):

    if request.method == 'POST':
         print(request.POST)
         b=Tutorial(request.POST.get('tutorial_title'), request.POST.get('tutorial_content'))
         b.save()
         context =  {'Tutorial' :Tutorial.objects.all}
         return render(request, 'test2.html', context)
                    
 

    else :

        context = {"books": Tutorial.objects.all()}
        return render(request, 'test.html', context)