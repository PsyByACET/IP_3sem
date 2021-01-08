from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import users, task
from .serializers import usersSerializer

def index(request):
    tasks = task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


def about(request):
    return HttpResponse("<h2>ABOUT</h2>")




class usersView(APIView):
    def get(self, request):
        userss = users.objects.all()
        # return Response({"tasks": tasks})
        serializer = usersSerializer(userss, many=True)

        return Response({"userss": serializer.data})
