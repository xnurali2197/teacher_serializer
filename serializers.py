class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'full_name', 'school', 'school_name']

    def get_full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"
