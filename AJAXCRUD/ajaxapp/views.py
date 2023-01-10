from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import UserForm
from .models import Userinfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    uform = UserForm()
    user_data = Userinfo.objects.all()
    return render(request, 'index.html', {'user_data': user_data, 'uform': uform})


@csrf_exempt
def insert_data(request):
    if request.method == "POST":
        # input form data in student registration model
        uform = UserForm(request.POST, request.FILES)
        # check form validation
        if uform.is_valid():
            # upload file
            handle_uploaded_file(request.FILES['image'])
            # save form data
            uform.save()
            # fetch all student data
            user_data = get_all_users(request)
            # send student data in response
            return JsonResponse({'status': 'Save', 'user_data': user_data})
        else:
            # send invalid data error
            return JsonResponse({'status': 0})


'''def insertdata(request):
    if request.method == 'POST':
       form = UserForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = UserForm()
        return render(request, 'index.html', {'form': form})
'''


def update_user(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        print(id)
        user = Userinfo.objects.get(pk=id)
        # convert data to json data and send JsonResponse ajax file (data) as a json data
        user_data = {"id": user.id, "fname": user.fname, "lname": user.lname,
                     "gender": user.gender, "hobbies": user.hobbies, "occupation": user.occupation}
        return JsonResponse(user_data)


def delete_user(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        print(id)
        delete_rec = Userinfo.objects.get(pk=id)
        print(delete_rec)
        delete_rec.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def updatedata(request):
    id = int(request.POST.get('uid'))
    user = Userinfo.objects.get(pk=id)
    if request.method == "POST" and user:
        form = Userinfo(request.POST, request.FILES, instance=id)

        if (form.is_valid()):
            handle_uploaded_file(request.FILES['image'])
            form.save()
            user_data= get_all_users(request)
            return JsonResponse({'status':'Save',' user_data': user_data}) 


def handle_uploaded_file(f):
    with open('image/image/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def get_all_users(request):
    user = Userinfo.objects.all()
    Userlist = []
    for user in user:
        Userlist.append({"id": user.id, "fname": user.fname, "lname": user.lname, "gender": user.gender,
        "hobbies": user.hobbies, "occupation": user.occupation, "image": request.build_absolute_uri(user.image.url)})
    return Userlist
