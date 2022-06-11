from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer
from ..basic.constants import OBJECT_CREATED, BAD_REQUEST
from ..basic.utils import get_return_rest_201, get_return_rest_400


class RegisterUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return get_return_rest_201(OBJECT_CREATED)

        return get_return_rest_400(BAD_REQUEST, serializer.errors)


class ListUserView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
