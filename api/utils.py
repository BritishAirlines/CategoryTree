from .models import Category
from django.db import IntegrityError
import logging
from rest_framework import serializers

logger = logging.getLogger(__name__)


def validate_tree(json_tree, unique_set, parent=None):
    try:
        name = json_tree.get('name', None)
        children = json_tree.get('children', None)
        if not isinstance(name, str):
            raise serializers.ValidationError(f'{name} is not str')
        else:
            if not len(name) > 0:
                raise serializers.ValidationError(f'name cannot be empty')
            else:
                if name not in unique_set:
                    unique_set.add(name)
                else:
                    raise serializers.ValidationError(f'{name} has duplicates')
        try:
            parent_obj = Category.objects.get(name__iexact=parent) if parent is not None else None
            obj = Category.objects.get(name=name)
            raise serializers.ValidationError(f'{obj.name} already exists - parent {parent_obj}')
        except Category.DoesNotExist:
            pass
        if children is not None:
            if isinstance(children, list):
                if len(children) > 0:
                    for item in children:
                        if isinstance(item, dict):
                            validate_tree(item, unique_set, parent=name)
                        else:
                            raise serializers.ValidationError(f'{children} is not dict')
                else:
                    raise serializers.ValidationError(f'{children} cannot be empty')
            else:
                raise serializers.ValidationError(f'{children} is not list')
    except Category.MultipleObjectsReturned:
        raise serializers.ValidationError('Multiple object were returned by get()')
    except serializers.ValidationError:
        raise


def get_edges(json_tree, parent=None):
    try:
        name = json_tree.get('name', None)
        children = json_tree.get('children', None)
        try:
            parent_obj = Category.objects.get(name__iexact=parent) if parent is not None else None
            obj, created = Category.objects.get_or_create(name=name, defaults={'parent': parent_obj})
            if created:
                logger.info(f'object successfully created: {obj} with parent - {parent_obj}')
            else:
                logger.info(f'object {obj} already exists')
        except IntegrityError:
            raise
        if children is not None and isinstance(children, list):
            for item in children:
                if isinstance(item, dict):
                    get_edges(item, parent=name)
    except IntegrityError:
        logger.exception('Integrity Error occured while trying to create an object')
    except Category.MultipleObjectsReturned:
        logger.exception('Multiple object were returned by get()')
