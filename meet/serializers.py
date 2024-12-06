from rest_framework import serializers
from meet.models import Login,Dept,Users,Meetinglist,Attendee,qiandao
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']  # 根据需要返回字段


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Login  # 指定模型
        fields = '__all__'  # 定义要序列化的字段

    def create(self, validated_data):
        # 在创建用户时，确保密码已经加密
        validated_data['pwd'] = make_password(validated_data['pwd'])
        return super(LoginSerializers, self).create(validated_data)

class DeptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dept  # 指定模型
        fields = '__all__' # 定义要序列化的字段


class UserSerializers(serializers.ModelSerializer):
    dept_info = serializers.SerializerMethodField(read_only=True)
    dept = serializers.PrimaryKeyRelatedField(queryset=Dept.objects.all())  # 允许通过主键写入 dept
    def get_dept_info(self, obj):
        dept_queryset = obj.dept
        return {"id": dept_queryset.id, "name": dept_queryset.name}
    class Meta:
        model = Users  # 指定模型
        fields = '__all__'
        # extra_kwargs = {
        #     'dept': {'write_only': True},
        #     # 只写的不显示，只显示只读的
        # }

class MeetinglistSerializer(serializers.ModelSerializer):
    dept = serializers.PrimaryKeyRelatedField(queryset=Dept.objects.all())  # 允许通过主键写入 dept
    dept_info = serializers.SerializerMethodField()  # 添加 dept_info 字段(只读)

    def get_dept_info(self, obj):
        if obj.dept:  # 确保 dept 存在
            return {"id": obj.dept.id, "name": obj.dept.name}
        return None  # 如果没有 dept，则返回 None
    class Meta:
        model = Meetinglist
        fields = '__all__'



class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class qiandaoSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(queryset=Meetinglist.objects.all())
    meeting_info = serializers.SerializerMethodField()

    def get_meeting_info(self, obj):
        if obj.meeting:
            return {"id": obj.meeting.id, "date":obj.meeting.date,"starttime": obj.meeting.starttime,
                    "dept": {
                    "id": obj.meeting.dept.id,        # 返回 dept 的 id
                    "name": obj.meeting.dept.name     # 返回 dept 的 name
                }}
        return None
    class Meta:
        model = qiandao
        fields = '__all__'


