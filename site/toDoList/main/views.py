from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import users, task
from .serializers import usersSerializer
from .forms import taskForm

def index(request):
    tasks = task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


def about(request):
    return HttpResponse("<h2>ABOUT</h2>")

def create(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'форма не верна'

    form = taskForm()
    context = {'form':form}
    return render(request, 'main/create.html', context)




class usersView(APIView):
    def get(self, request):
        userss = users.objects.all()
        # return Response({"tasks": tasks})
        serializer = usersSerializer(userss, many=True)

        return Response({"userss": serializer.data})
