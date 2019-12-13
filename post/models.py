from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse as ApiReverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
    class Meta:
        verbose_name_plural = "My Api Posts"
    # def get_api_url(self, request=None):
    #     return ApiReverse("API:post-rud", kwargs={"pk":self.pk}, request=request)