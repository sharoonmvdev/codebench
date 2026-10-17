from django.shortcuts import render

from django.contrib.auth.backends import ModelBackend

from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView

from rest_framework import permissions,authentication

from api.serializers import ProblemSerializer,AdminSerializer

from api.models import Problem

from api.permissions import OwnerOnly

class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer

class ProblemListCreateView(ListAPIView,CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProblemSerializer

    def get_queryset(self):

        return Problem.objects.filter(posted_by=self.request.user)

    def perform_create(self, serializer):

        return serializer.save(posted_by=self.request.user)

class ProblemUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    serializer_class = ProblemSerializer

    queryset = Problem.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [OwnerOnly]


class ProblemRetrieveView(RetrieveAPIView):

    queryset = Problem.objects.all()

    serializer_class = ProblemSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    








