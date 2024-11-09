from meet.views import (UserView,MeetinglistView,AttendeeView,DeptView,
                    MeetinglistDetailView,AttendeeDetailView,register,login,CustomTokenRefreshView,UserListView)

from rest_framework.routers import DefaultRouter
from django.urls import path
# 创建一个默认的路由器
router = DefaultRouter()
# 注册视图集


router.register("user",UserView)
router.register("dept",DeptView)
router.register("users",UserListView)
router.register("meetinglist",MeetinglistView,basename='meetinglist')
router.register(r'meetinglist1', MeetinglistDetailView, basename='meetinglist1')
router.register("attendee",AttendeeView,basename='attendee')
router.register("attendeepro",AttendeeDetailView,basename='attendeepro')


urlpatterns = [
    # path('login/', LoginView.as_view({'post': 'login'}), name='login'),  # 登录认证
    path('login1/', login, name='login1'),  # 登录接口路径
    path('register1/', register, name='register1'),  # 注册接口路径
    # path('login/', LoginView.as_view(), name='login'),  # 登录认证

    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),



]
urlpatterns += router.urls