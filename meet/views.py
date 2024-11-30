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
from django.utils import timezone
from datetime import datetime

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
    queryset = Meetinglist.objects.all()
    serializer_class = MeetinglistSerializer

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

    # 添加更新会议状态的方法
    @action(detail=False, methods=['get'])
    def update_meeting_status(self, request):
        # 使用本地时间
        current_datetime = timezone.localtime(timezone.now())
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        
        # print(f"当前时间: {current_time}")  # 调试信息
        
        # 更新已过期的会议状态
        expired_meetings = Meetinglist.objects.filter(
            date__lt=current_date,
            status__in=['未开始', '进行中']  # 同时更新未开始和进行中的过期会议
        )
        expired_meetings.update(status='已结束')

        # 更新当天的会议状态
        today_meetings = Meetinglist.objects.filter(
            date=current_date
        )
        
        for meeting in today_meetings:
            # print(f"会议: {meeting.title}")  # 调试信息
            # print(f"开始时间: {meeting.starttime}")  # 调试信息
            # print(f"结束时间: {meeting.endtime}")  # 调试信息
            # print(f"当前状态: {meeting.status}")  # 调试信息
            
            # 使用严格的时间比较
            if meeting.starttime <= current_time <= meeting.endtime:
                if meeting.status != '进行中':
                    meeting.status = '进行中'
                    meeting.save()
            elif current_time > meeting.endtime:
                if meeting.status != '已结束':
                    meeting.status = '已结束'
                    meeting.save()
            elif current_time < meeting.starttime:
                if meeting.status != '未开始':
                    meeting.status = '未开始'
                    meeting.save()

        return Response({
            'message': '会议状态更新成功',
            'current_time': str(current_time),
            'current_date': str(current_date)
        }, status=status.HTTP_200_OK)

#会议分页
class MeetinglistDetailView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # 仅允许经过身份验证的用户访问
    queryset = Meetinglist.objects.all()
    pagination_class = LoginPagination  # 设置分页器
    serializer_class = MeetinglistSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date') # 使用 '-' 表示降序 （根据date降序排序）
    def list(self, request, *args, **kwargs):
        # factor = self.request.query_params.get("factor", "f1")  根据请求中的参数来决定哪些数据需要返回
        quaryset = self.get_queryset()
        page = self.paginate_queryset(quaryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(quaryset, many=True)
        return Response(serializer.data)



# 参会人员
class AttendeeView(viewsets.ModelViewSet):

    queryset = Attendee.objects.all().order_by('id')  # 添加排序
    serializer_class = AttendeeSerializer

    def destroy(self, request, *args, **kwargs):
        # 删除所有记录
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#签到分页
class AttendeeDetailView(viewsets.ModelViewSet):
    pagination_class = LoginPagination  # 设置分页器
    queryset = Attendee.objects.all().order_by('-meetdate')  # 添加排序
    serializer_class = AttendeeSerializer


