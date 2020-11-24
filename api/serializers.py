from rest_framework import serializers
from .models import Category
from .utils import get_edges, validate_tree


class StrictCharField(serializers.CharField):
    def to_internal_value(self, value):
        if isinstance(value, str):
            return value
        else:
            self.fail('invalid', input=value)


class NestedCategorySerializer(serializers.ModelSerializer):
    name = StrictCharField(required=True)

    class Meta:
        model = Category
        fields = ('name', 'children')

    def get_fields(self):
        fields = super(NestedCategorySerializer, self).get_fields()
        fields['children'] = NestedCategorySerializer(many=True, required=False)
        return fields

    def validate(self, data):
        unique_set = set()
        validate_tree(data,  unique_set)
        return data

    def create(self, validated_data):
        get_edges(validated_data)
        return validated_data


class CategoryPartialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryReportSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('_get_children')
    parents = serializers.SerializerMethodField('_get_parents')
    siblings = serializers.SerializerMethodField('_get_siblings')

    def _get_children(self, obj):
        serializer = CategoryPartialSerializer(obj.child_list(), many=True)
        return serializer.data

    def _get_parents(self, obj):
        serializer = CategoryPartialSerializer(obj.parents_list(), many=True)
        return serializer.data

    def _get_siblings(self, obj):
        serializer = CategoryPartialSerializer(obj.siblings_list(), many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'parents', 'children', 'siblings')