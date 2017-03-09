from rest_framework import serializers
from netaddr import *
from api.models import *


class Functiongroupserializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Functiongroup

class Hostserializers(serializers.HyperlinkedModelSerializer):
     function_group = serializers.SlugRelatedField(queryset=Functiongroup.objects.all(), slug_field='fun_groupname')
     class Meta:
         model = Host

class Roleserializers(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = Role
         fields = ('id', 'rolename', 'role_var','detail','stepnum','created_date','modified_date')
class Exe_groupserializers(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = Exe_group
         fields = ('id', 'exe_groupname', 'group_var','detail','created_date','modified_date')
class Host_exe_groupserializers(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = Host_exe_group

class Missionserializers(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = Mission

class Exeuserserializers(serializers.HyperlinkedModelSerializer):

     class Meta:
         model = Exeuser


