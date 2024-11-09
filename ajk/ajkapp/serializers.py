from rest_framework import serializers
from .models import beijin, guangzhou, shenzhen, shanghai, taiyuan, average_prices


class BeijingSerializer(serializers.ModelSerializer):
    class Meta:
        model = beijin
        fields = '__all__'  # 或者指定具体的字段，如 ['region', 'average_price', ...]


class GuangzhouSerializer(serializers.ModelSerializer):
    class Meta:
        model = guangzhou
        fields = '__all__'

class ShenzhenSerializer(serializers.ModelSerializer):
    class Meta:
        model = shenzhen
        fields = '__all__'

class ShanghaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = shanghai
        fields = '__all__'

class TaiyuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = taiyuan
        fields = '__all__'

    # ... 为其他城市创建类似的序列化器 ...


class AveragePricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = average_prices
        fields = '__all__'