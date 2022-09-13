from rest_framework import status
from rest_framework.response import Response


def response(data=None, isBad=None):
    if isBad:
        return Response({"status": "error", "data": data}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
