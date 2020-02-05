from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from kaist.chat.interactors import GetMenuInteracor


class FCLT(APIView):
    def post(self, request: Request) -> Response:
        menu = GetMenuInteracor().execute(request.data)
        print(menu)
        return Response(
            status=status.HTTP_200_OK,
            data=menu
        )


