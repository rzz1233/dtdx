from meet.models import Login
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions

# 自定义认证类
class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token", "")
        print(f"Received token: {token}")  # 打印接收到的 token

        if not token:
            raise exceptions.AuthenticationFailed("登录之后才能访问")

        user_obj = Login.objects.filter(token=token).first()
        print(f"Authenticated user: {user_obj}")  # 打印找到的用户对象

        if not user_obj:
            raise exceptions.AuthenticationFailed("token 不合法")

        return (user_obj, None)


from rest_framework.pagination import PageNumberPagination

# 自定义分页器
class LoginPagination(PageNumberPagination):
    page_size = 1000 # 每页显示的记录数量
    page_query_param = 'page'  # 页码参数名称
    page_size_query_param = 'page_size' # 每页大小的参数名称
    max_page_size = 1000



# class LoginView(APIView):
#     # permission_classes = [AllowAny]  # 允许未认证的用户访问此视图 jwt的
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#     def post(self, request):
#         # 获取请求中的用户名和密码
#         username = request.data.get("user")
#         password = request.data.get("pwd")
#
#         try:
#             # 仅通过用户名查找用户
#             login_user = Login.objects.get(user=username)
#         except Login.DoesNotExist:
#             return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 使用 check_password 验证密码
#         if check_password(password, login_user.pwd):
#             # 生成 token 并保存
#             login_user.token = str(uuid.uuid4())
#             login_user.save()
#             return Response({'token': login_user.token})
#         else:
#             return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
#
# class TestView(APIView):
#     # 指定使用自定义的认证类
#     authentication_classes = [MyAuth]
#     # permission_classes = [AllowAny]
#
#     def get(self,request):
#         # 返回测试认证成功的响应
#         return Response("我是测试认证的组件")
