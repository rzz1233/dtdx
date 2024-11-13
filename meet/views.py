from rest_framework.views import APIView
from rest_framework import viewsets,status,exceptions
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from meet.models import Login, Users, Dept, Meetinglist, Attendee
from meet.serializers import LoginSerializers, UserSerializers, MeetinglistSerializer, AttendeeSerializer, DeptSerializers,UsersSerializer
from meet.auth import LoginPagination
from django.contrib.auth.models import User
# 注册

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')  # 添加排序
    serializer_class = UsersSerializer
    pagination_class = LoginPagination  # 设置分页器

# 注册
@api_view(['POST'])   #@api_view 是一个装饰器，用于将一个视图函数转换为 DRF 的视图，并指定允许的 HTTP 请求方法。
def register(request):
    # 获取请求中的用户名和密码
    username = request.data.get('username')
    password = request.data.get('password')

    # 验证用户名和密码是否为空
    if not username or not password:
        return Response({'error': '用户名和密码不能为空'}, status=status.HTTP_400_BAD_REQUEST)

    # 检查用户名是否已经存在
    if User.objects.filter(username=username).exists():
        return Response({'error': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)

    # 创建用户并保存到数据库
    user = User.objects.create(
        username=username,
        password=make_password(password)  # 对密码进行加密
    )
    return Response({'message': '注册成功'}, status=status.HTTP_201_CREATED)

#登录
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': '用户名和密码不能为空'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is not None:
        # 创建访问令牌和刷新令牌
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        return Response({
            'access': str(access_token),
            'refresh': str(refresh_token),
            'is_superuser': user.is_superuser
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': '用户名或密码不正确'}, status=status.HTTP_400_BAD_REQUEST)

# 刷新token
from rest_framework_simplejwt.views import TokenRefreshView
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'error': '缺少刷新令牌'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(refresh)
            access_token = str(refresh_token.access_token)
            return Response({'access': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 用户视图
class UserView(viewsets.ModelViewSet):

    queryset = Users.objects.all().order_by('id')  # 添加排序
    serializer_class = UserSerializers
    pagination_class = LoginPagination  # 设置分页器

    def create(self, request, *args, **kwargs):
        username = request.data.get('user')

        # 检查用户名是否已存在
        if User.objects.filter(user=username).exists():
            return Response({'error': '用户名已存在！'}, status=status.HTTP_400_BAD_REQUEST)

        # 调用父类的 create 方法，处理正常的创建逻辑
        return super().create(request, *args, **kwargs)

class DeptView(viewsets.ModelViewSet):

    queryset = Dept.objects.all()
    serializer_class = DeptSerializers

    def create(self, request, *args, **kwargs):
        dept_name = request.data.get('name')

        # 检查部门名称是否已存在
        if Dept.objects.filter(name=dept_name).exists():
            return Response({'error': '部门名称已存在！'}, status=status.HTTP_400_BAD_REQUEST)

        # 调用父类的 create 方法，处理正常的创建逻辑
        return super().create(request, *args, **kwargs)

# 会议视图
class MeetinglistView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # 仅允许经过身份验证的用户访问
    queryset = Meetinglist.objects.all()
    serializer_class = MeetinglistSerializer

    # def get_queryset(self):
    #     today = date.today() # 获取当前日期
    #     return Meetinglist.objects.filter(date=today).order_by('date')  # 返回今天的会议并排序
    # 预约时间冲突
    @action(detail=False, methods=['get'])
    def check_time_conflict(self, request):
        date = request.query_params.get('date')
        starttime = request.query_params.get('starttime')
        endtime = request.query_params.get('endtime')

        # 查询是否有冲突的预约
        conflict = Meetinglist.objects.filter(
            date=date,
            starttime__lt=endtime,
            endtime__gt=starttime
        ).exists()

        return Response({'conflict': conflict})

#会议分页
class MeetinglistDetailView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # 仅允许经过身份验证的用户访问
    queryset = Meetinglist.objects.all().order_by('-date')  # 使用 '-' 表示降序 （根据date降序排序）
    pagination_class = LoginPagination  # 设置分页器
    serializer_class = MeetinglistSerializer



# 参会人员
class AttendeeView(viewsets.ModelViewSet):

    queryset = Attendee.objects.all().order_by('id')  # 添加排序
    serializer_class = AttendeeSerializer

    def destroy(self, request, *args, **kwargs):
        # 删除所有记录
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#签到分页
# class AttendeeDetailView(viewsets.ModelViewSet):
#     pagination_class = LoginPagination  # 设置分页器
#     queryset = Attendee.objects.all().order_by('-meetdate')  # 添加排序
#     serializer_class = AttendeeSerializer


