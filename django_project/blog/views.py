import os


from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesAdmin



# Create your views here.
def home(request):
    context = {'file': FilesAdmin.objects.all()}
    return render(request, 'blog/home.html', context)
    return HttpResponse


def showResult(request):
    nm1 = request.POST['fname']
    nm2 = request.POST['lname']
    nm = nm1 + ' ' + nm2
    return render(request, 'blog/showResult.html', {'name': nm})



def download(request, path):
    file_path: os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

        raise Http404


def result():
    return None
