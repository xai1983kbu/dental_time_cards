from rest_framework import generics
from rest_framework import mixins

from salary.models import DaysAtWork
from salary.api.serializers import DaysAtWorkSerializer


class DaysAtWorkDetailView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.RetrieveAPIView):
    serializer_class   = DaysAtWorkSerializer
    queryset           = DaysAtWork.objects.all()
    lookup_field       = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DaysAtWorkAPIView(mixins.CreateModelMixin,
                        generics.ListAPIView):
    serializer_class     = DaysAtWorkSerializer
    queryset             = DaysAtWork.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)