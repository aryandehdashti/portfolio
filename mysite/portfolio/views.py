from .models import MyInfo, About, Project, Skill
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyInfoSerializer, AboutSerializer, ProjectSerializer, SkillSerializer

# Create your views here.

# class MyInfoViewSet(viewsets.ModelViewSet):
#     queryset = MyInfo.objects.all()
#     serializer_class = MyInfoSerializer

# class AboutViewSet(viewsets.ModelViewSet):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class SkillViewSet(viewsets.ModelViewSet):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer


# class GetPortfolioPage(APIView):

#     def get(self, request, format=None):
#         myInfo = MyInfo.objects.all()
#         about = About.objects.all()
#         project = Project.objects.all()
#         skill = Skill.objects.all()

#         myInfoSerializer = MyInfoSerializer(myInfo, many=True)
#         aboutSerializer = AboutSerializer(about, many=True)
#         projectSerializer = ProjectSerializer(project, many=True)
#         skillSerializer = SkillSerializer(skill, many=True)

#         data = {
#             'myInfo':myInfoSerializer.data,
#             'about':aboutSerializer.data,
#             'project':projectSerializer.data,
#             'skill':skillSerializer.data
#         }
#         return Response(data)

# class GetPortfolioPage(APIView):
#     def get(self, request, format=None):
#         myInfo = MyInfo.objects.all()
#         myInfoSerializer = MyInfoSerializer(myInfo)
#         return Response(myInfoSerializer.data)

class GetMyInfo(APIView):

    def get(self, request, format=None):
        myInfo = MyInfo.objects.all()
        myInfoSerializer = MyInfoSerializer(myInfo, many=True)
        return Response(myInfoSerializer.data)
    

class GetAbout(APIView):
    
    def get(self, request, format=None):
        about = About.objects.all()
        aboutSerializer = AboutSerializer(about, many=True)
        return Response(aboutSerializer.data)
    

class GetProject(APIView):
    
    def get(self, request, format=None):
        project = Project.objects.all()
        projectSerializer = ProjectSerializer(project, many=True)
        return Response(projectSerializer.data)
    

class GetSkill(APIView):
    
    def get(self, request, format=None):
        skill = Skill.objects.all()
        skillSerializer = SkillSerializer(skill, many=True)
        return Response(skillSerializer.data)
    


