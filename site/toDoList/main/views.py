from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from .models import users, task
from .serializers import usersSerializer, taskSerializer
from .forms import taskForm, pointsFilterForm
from .models import task, users, score

def index(request):
    tasks = task.objects.all()
    form = pointsFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_points']:
            tasks = tasks.filter(points__gte=form.cleaned_data['min_points'])

        if form.cleaned_data['max_points']:
            tasks = tasks.filter(points__lte=form.cleaned_data['max_points'])

    return render(request, 'main/index.html', {'tasks': tasks, 'form': form})


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
    
class taskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]
