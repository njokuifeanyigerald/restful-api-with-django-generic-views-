# from rest_framework.test import APITestCase
# from django.contrib.auth import get_user_model
# # Create your tests here.
# from post.models import Post

# class PostAPITestCase(APITestCase):
#     def setUp(self):
#         user_obj  = User(username="geraldd", email="b@gmsil.com")
#         user_obj.set_password("asasas")
#         user_obj.save()
#         post = Post.objects.create(
#             user=user_obj,
#             title="dog",
#             content="some_random_content"
#         )
#     def test_single_user(self):
#         user_count = User.objects.count()
#         self.assertEqual(user_count,1)
