from django.shortcuts import render

# Create your views here.
from book_app.models import Book
from django.views.generic import View
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name="dispatch")
class BookListCreateView(View):

    def get(self,request):

        qs=Book.objects.all().values()

        response_data=list(qs)

        return JsonResponse(response_data,safe=False)


    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        Book.objects.create(**form_data)

        response_data={"message":"created"}

        return JsonResponse(response_data,safe=False)

@method_decorator(csrf_exempt,name="dispatch")
class BookRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs=Book.objects.filter(id=pk).values()

        response_data=list(qs)

        return JsonResponse(response_data,safe=False)

    def put(self,request,pk=None):

        json_data=request.body

        form_data=loads(json_data)

        Book.objects.filter(id=pk).update(**form_data)

        response_data={"message":"updated"}

        return JsonResponse(response_data,safe=False)


    def delete(self,request,pk=None):

        Book.objects.filter(id=pk).delete()

        response_data={"message":"deleted"}

        return JsonResponse(response_data)
    