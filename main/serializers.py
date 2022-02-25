from portfolio_website import serializers
from .models import TechnicalSkill, Language, Experience, Education, Hobby, Course, Project

DEFAULT_MAX_LENGTH = 255


class TechnicalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkill
        fields = ('name',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('level', 'name')


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('name',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title',)


class EducationSerializer(serializers.Serializer):
    authority = serializers.CharField()
    title = serializers.CharField()
    major = serializers.CharField()
    gpa = serializers.FloatField()
    courses = CourseSerializer(read_only=True, many=True)
    projects = ProjectSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('authority', 'title', 'start_time', 'end_time', 'descriptions')


class CVSerializer(serializers.Serializer):
    user_picture_url = serializers.URLField(source='user_picture.url', read_only=True)
    user_picture_alt = serializers.URLField(source='user_picture.alt', read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    technical_skills = TechnicalSkillSerializer(read_only=True, many=True)
    languages = LanguageSerializer(read_only=True, many=True)
    hobbies = HobbySerializer(read_only=True, many=True)
    educations = EducationSerializer(read_only=True, many=True)
    experiences = ExperienceSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
