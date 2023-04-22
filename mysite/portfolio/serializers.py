from .models import MyInfo, About, Project, Skill
from rest_framework import serializers

class MyInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyInfo
        fields = ['fullName', 'miniDescribe', 'avatar', 'phone', 'email', 'cv', 'github', 'linkedin']


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'describe1', 'describe2', 'aboutAvatar']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'image']


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['title', 'grade']