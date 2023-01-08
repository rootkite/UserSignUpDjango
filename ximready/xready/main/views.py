from django.shortcuts import render
from main.froms import SiteUserForm
from main.models import SiteUser

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def signup(request):

    singupform = SiteUserForm()
    if request.method == 'POST':
        singupform = SiteUserForm(request.POST)
        if singupform.is_valid():
            singupform.save(commit=True)
            return render(request, 'main/index.html',{'checkforgreet':1})
        else:
            print('Error : Form invalid')
    return render(request, 'main/signup.html',{'signupform':singupform})



def userlist(request):
    userslist = SiteUser.objects.order_by('lname')
    usersdict = {'userdicthere':userslist}
    return render(request, "main/userlist.html",context=usersdict)

