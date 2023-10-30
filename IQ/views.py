from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
import requests
url = "http://notify.eskiz.uz/api/message/sms/send"

class Registration(APIView):
    def post(self, request):
        data = request.data
        number = data["mobile_number"]
        data["password"] = make_password(request.data['password'])
        serializer = UserSerializer(data)
        payload={'mobile_phone': number,
        'message': 'Eskiz Test',
        'from': '4546',
        'callback_url': 'http://0000.uz/test.php'}
        files=[]
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI0NTksInJvbGUiOm51bGwsImRhdGEiOnsiaWQiOjI0NTksIm5hbWUiOiJPXHUyMDE4emJla2lzdG9uLUZpbmxhbmRpeWEgcGVkYWdvZ2lrYSBpbnN0aXR1dGkiLCJlbWFpbCI6ImRvc3VtYmV0b3YxOTk4MzAxMEBnbWFpbC5jb20iLCJyb2xlIjpudWxsLCJhcGlfdG9rZW4iOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPakkwTlRrc0luSnZiR1VpT2lJaUxDSmtZWFJoSWpwN0ltbGtJam95TkRVNUxDSnVZVzFsSWpvaVJHOXpkVzFpWlhSdmRpQlBaeWRoWW1WcklFUmhkbXhoZENCdkoyY25iR2tpTENKbGJXRnBiQ0k2SW1SdmMzVnRZbVYwYjNZeE9UazRNekF4TUVCbmJXRnBiQzVqYjIwaUxDSnliMnhsSWpvaUlpd2lZWEJwWDNSdmEyVnVJam9pWlhsS01HVllRV2xQYVVwTFZqRlJhVXhEU20iLCJzdGF0dXMiOiJhY3RpdmUiLCJzbXNfYXBpX2xvZ2luIjoiZXNraXoyIiwic21zX2FwaV9wYXNzd29yZCI6ImUkJGsheiIsInV6X3ByaWNlIjo1MCwidWNlbGxfcHJpY2UiOjExNSwidGVzdF91Y2VsbF9wcmljZSI6MCwiYmFsYW5jZSI6OTgwNjUwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6IjIwMjMtMDItMDdUMTQ6Mzg6MjMuMDAwMDAwWiIsInVwZGF0ZWRfYXQiOiIyMDIzLTEwLTA5VDA1OjQzOjA3LjAwMDAwMFoiLCJ3aGl0ZWxpc3QiOm51bGwsImhhc19wZXJmZWN0dW0iOjAsImJlZWxpbmVfcHJpY2UiOjUwfSwiaWF0IjoxNjk2ODMwOTQ1LCJleHAiOjE2OTk0MjI5NDV9.JsPtMAFIPL9oHKkGYVbHlhTLJAz99RbsDmyY8KYxF94"
        headers = {'Authorization': "Bearer {}".format(token)}
        if serializer.is_valid():
            serializer.save()
            token = RefreshToken.for_user(serializer.instance)
            context = {
                "refresh":str(token),
                "access": str(token.access_token),
                "sms": requests.request("POST", url, headers=headers, data=payload, files=files)
            }
            return Response(context)
        return Response(serializer.errors)


