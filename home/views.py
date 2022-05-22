from django.shortcuts import render,HttpResponse, redirect
from home.logic import convert
from home.models import UploadImage
from home.forms import UserImage

# Create your views here.
def home(request):
    form = UserImage(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        img_object = form.instance
        cap = img_object.caption
        text = convert(img_object,cap)
        # print(img_object.image.url)
        return render(request, 'base.html', {'form': form, 'img_obj':img_object, 'text':text})
    else:
        form= UserImage()
        return render(request, 'base.html',{'form':form})
