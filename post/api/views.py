from post.models import Post
from rest_framework import generics, permissions, filters
from .serializer import PostSerializer
# from  rest_framework.permissions import IsAdminUser
from django.db.models import Q


class PostListCreateView(generics.ListCreateAPIView):
    pass
    lookup_field = "pk"
    serializer_class = PostSerializer
    # permission_classes = [IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs
    def get_queryset(self):
        return Post.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def post(self, request, *args, **kwargs):
    #     return self.create(self,request,*args,**kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(self, request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.update(self, request, *args, **kwargs)
    # def get_serializer_context(self, *args,**kwargs):
    #     return {"request":self.request}


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = "pk"
    serializer_class = PostSerializer
    # queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Post.objects.all(pk=pk)
    # def get_serializer_context(self, *args,**kwargs):
    #     return {"request":self.request}

