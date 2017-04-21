# -*- coding:utf-8 -*-  
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from ht.models import Todo
from ht.serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

#if request.user.is_authenticated():

class HomeView(APIView):
	def get(self,request,format=None):
		return render(request,'newTodolist.html')	
	def post(request):
		return Response(template_name='newTodolist.html')

class RegisterView(APIView):#注册模块
	renderer_classes = [TemplateHTMLRenderer]
	def get(self,request,fomat=None):
		
		return Response(template_name='register.html')
	def post(self,request,fomat=None):
		username = request.data['account']
		password = request.data['password']
		password2 = request.data['password2']
		if password2 != password: 
			return Response({'errors':"Confirm your password"},template_name='register.html')
		filterResult=User.objects.filter(username=username) 
		if len(filterResult)>0:
			return Response({'errors':"The username is existed"},template_name='register.html')
		user = User.objects.create_user(username=username,password=password)
		user.save()
		return HttpResponseRedirect('/home')
		#非空判断
		
class LoginView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	def get(self, request, format=None):
		return HttpResponseRedirect('/home')											

	def post(self, request, format=None):
		if request.user.is_authenticated():
			return HttpResponseRedirect('/home')
		errors=[]
		username = request.data['account']  
		password = request.data['password']  
		user = authenticate(username=username, password=password)

		if user is not None: 
			if user.is_active:  
				login(request, user)
				return Response({"username":username},template_name='newTodolist.html')
			else:  
				return Response({'errors':'Username is inactive!'},template_name='newTodolist.html')
		else:
			return Response({'errors':'Username or password is incorrect!'},template_name='newTodolist.html')

def Logout(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect('/home')

class ReturnTodoView(APIView):
	def get(self, request, format=None):
		if request.user.is_authenticated():
			username = request.user.username
			Thing = Todo.objects.filter(username=username)
			serializer = TodoSerializer(Thing,many=True)
			return Response(serializer.data)
	def post(self, request, format=None):
		if request.user.is_authenticated():
			username = request.user.username
			Thing = Todo.objects.filter(username=username)
			serializer = TodoSerializer(Thing,many=True)
			return Response(serializer.data)
		return HttpResponseRedirect('/home')

class ChangeView(APIView):
	def get(self,request,fomat=None):
		return HttpResponseRedirect('/home')
	def post(self,request,fomat=None):
		obj = Todo.objects.get(id=request.data['id'])
		obj.status = request.data['status']
		obj.save()
		return Response(status=200)

class PostView(APIView):
	def get(self,request,fomat=None):
		return HttpResponseRedirect('/home')
	def post(self,request,fomat=None):
		title=request.data['title']
		description=request.data['description']
		username = request.user.username
		#curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
		Thing = Todo.objects.create(title=title,description=description,username=username,status=0)
		print request.data['description']
		Thing.save()
		#return render(request,'newTodolist.html')
		return HttpResponseRedirect('/home')
		#deadline 属性

class DeleteView(APIView):
	def get(self,request,fomat):
		return HttpResponseRedirect('/home')
	def post(self,request,fomat=None):
		Todo.objects.filter(id=request.data['id']).delete()
		#return render(request,'newTodolist.html')
		return Response(status=200)

"""  
	if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""