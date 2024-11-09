# project/urls.py 或 myapp/urls.py，取决于您的项目结构
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ajkapp.views import (BeijingViewSet, GuangzhouViewSet, ShenzhenViewSet,
                         ShanghaiViewSet, TaiyuanViewSet, AveragePricesViewSet,price_data,download_excel,register,
                          CustomTokenRefreshView,login)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'beijin', BeijingViewSet)
router.register(r'guangzhou', GuangzhouViewSet)
router.register(r'shenzhen', ShenzhenViewSet)
router.register(r'shanghai', ShanghaiViewSet)
router.register(r'taiyuan', TaiyuanViewSet)
router.register(r'average-prices', AveragePricesViewSet)

# 将API的URLs添加到urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # 包含由路由器生成的URLs
    path('price-data/', price_data, name='price-data'),
    path('download-excel/', download_excel, name='download_excel'),
    path('register/', register, name='register'),  # 注册接口路径
    path('login/', login, name='login'),  # 登录接口路径
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),


]