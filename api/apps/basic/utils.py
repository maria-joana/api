from rest_framework import status
from rest_framework.response import Response


def get_return_rest(msg, data=None, status=200, native=True):
    if native:
        return Response({msg: data}, status=status)


def get_return_rest_201(msg, data=None):
    return Response({msg: data}, status=status.HTTP_201_CREATED)


def get_return_rest_500(msg, data=None):
    return Response({msg: data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_return_rest_404(msg, data=None):
    return Response({msg: data}, status=status.HTTP_404_NOT_FOUND)


def get_return_rest_400(msg, data=None):
    return Response({msg: data}, status=status.HTTP_400_BAD_REQUEST)
