# import json
# import requests
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from .models import AirbnbData
# from myapp.service.scraper import Scraper
# from myapp.service.csvDataToList import CsvToList
# from myapp.cron import MyCronJob
# from airbnbscrap.myapp.seralizers import AirbnbSeralizer


# newObject = MyCronJob()
# airbnbdata = newObject.getData()


# class AirbnbApiView(generics.ListCreateAPIView):
    
#     serializer = AirbnbSeralizer(data= airbnbdata)
#     existing_data = AirbnbData.objects.get(
#         airbnbdata['URL']
#     )
#     olddata = existing_data.__dict__
#     breakpoint()
#     if serializer.is_valid():
#         breakpoint()
#         serializer.save()
#     else:
#         serializer = AirbnbSeralizer(olddata , data= airbnbdata)
#         if serializer.is_valid():
#             serializer.save()
    





    

#     # def post(self, request):
#     #     serializer = AirbnbSeralizer(data=request.data)
#     #     print(serializer)

#     #     if serializer.is_valid():
#     #         serializer.save(user=request.user, status=AirbnbData.SENT)
#     #     return Response(status=status.HTTP_201_CREATED)

#     # try:
#     #     serializer_class.instance = AirbnbData.objects.get(...)
#     # except AirbnbData.DoesNotExist:
#     #     pass

    