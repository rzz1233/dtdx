# views.py  
from rest_framework import viewsets
from .models import beijin, guangzhou, shenzhen, shanghai, taiyuan, average_prices
from .serializers import (BeijingSerializer, GuangzhouSerializer, AveragePricesSerializer,
                          ShenzhenSerializer, ShanghaiSerializer, TaiyuanSerializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
import pandas as pd
import plotly.graph_objects as go
import plotly.express.colors as px_colors
from django.http import FileResponse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
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


from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken

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
            'user_id': user.id
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': '用户名或密码不正确'}, status=status.HTTP_400_BAD_REQUEST)



#刷新token
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


@api_view(['GET'])
def price_data(request):
    # 读取数据
    df = pd.read_csv(r'D:\program\ajk\data\processed_year1.csv')

    df = df.sort_values(by=['Year', 'Region'])

    try:
        # 获取2024年每个地区的价格
        top_2024_prices = df[df['Year'] == 2024].set_index('Region')['Price']
    except KeyError:
        top_2024_prices = pd.Series(dtype=float)  # 创建一个空的Series

    # 创建一个颜色字典，为每个年份分配一个颜色
    unique_years = df['Year'].unique()
    year_colors = {year: px_colors.qualitative.Plotly[i % len(px_colors.qualitative.Plotly)]
                   for i, year in enumerate(sorted(unique_years))}

    fig = go.Figure()

    for year, group in df.groupby('Year'):
        color = year_colors.get(year, 'gray')
        try:
            # 获取当前年份的价格最高的前十个地区（基于2024年的价格排序）
            top_regions_this_year = group['Region'].isin(top_2024_prices.nlargest(10).index)
            # 然后我们需要基于这些地区重新筛选当前年份的数据
            filtered_group = group[top_regions_this_year].sort_values(by='Price', ascending=False)

            # 检查是否真的有至少10个地区
            if len(filtered_group) < 10:
                print(f"Skipping year {year} because it has less than 10 regions in top 10 of 2024.")
                continue

                # 创建trace并添加到图形中
            trace = go.Bar(
                x=filtered_group['Region'],
                y=filtered_group['Price'],
                name=f'Year {year}',
                legendgroup=f'Year {year}',
                marker_color=color,
                showlegend=True
            )
            fig.add_trace(trace)

        except Exception as e:
            print(f"Error processing year {year}: {e}")
            continue

        # 更新布局以包含图例和标题等
    fig.update_layout(
        xaxis_title='Region',
        yaxis_title='Price',
        title='房价变化柱状图',
        barmode='group',
        legend_title='Year'
    )

    # 显示图形
    fig.show()
    return HttpResponse("你好，请返回")
class BeijingViewSet(viewsets.ModelViewSet):
    queryset = beijin.objects.all().order_by('-average_price')
    serializer_class = BeijingSerializer
    permission_classes = [IsAuthenticated]  # 仅允许经过身份验证的用户访问


class GuangzhouViewSet(viewsets.ModelViewSet):
    queryset = guangzhou.objects.all().order_by('-average_price')
    serializer_class = GuangzhouSerializer


class ShenzhenViewSet(viewsets.ModelViewSet):
    queryset = shenzhen.objects.all().order_by('-average_price')
    serializer_class = ShenzhenSerializer


class ShanghaiViewSet(viewsets.ModelViewSet):
    queryset = shanghai.objects.all().order_by('-average_price')
    serializer_class = ShanghaiSerializer


class TaiyuanViewSet(viewsets.ModelViewSet):
    queryset = taiyuan.objects.all().order_by('-average_price')
    serializer_class = TaiyuanSerializer


class AveragePricesViewSet(viewsets.ModelViewSet):
    queryset = average_prices.objects.all().order_by('-Average_Price')
    serializer_class = AveragePricesSerializer


def download_excel(request):
    file_path = r'D:\program\ajk\data\processed_year1.csv'  # 替换为实际文件路径
    response = FileResponse(open(file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="2019-2024房价.xlsx"'
    return response