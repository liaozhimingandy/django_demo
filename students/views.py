from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from rest_framework import mixins, viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework import permissions

# Create your views here.
class StudentViewSet(mixins.ListModelMixin,# 表示可以在Postman类似的软件中只能查找所有数据
         viewsets.GenericViewSet,
         mixins.RetrieveModelMixin, # 表示可以在Postman类似的软件中只能查找单一数据
         mixins.UpdateModelMixin,  # 表示可以在Postman类似的软件中更新数据
         mixins.DestroyModelMixin,  # 表示可以在Postman类似的软件中删除数据
         mixins.CreateModelMixin):  # 表示可以在Postman类似的软件中创建数据):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentView(View):

    def get(self, request):
        # 获取数据
        student_list = Student.objects.all()

        # 转换数据[序列化过程]
        # 如果转换多个模型对象数据，则需要加上many=True
        serializer = StudentSerializer(instance=student_list,many=True)
        print( serializer.data ) # 序列化器转换后的数据

        # 响应数据给客户端
        # 返回的json数据，如果是列表，则需要声明safe=False
        return JsonResponse(serializer.data,safe=False)

