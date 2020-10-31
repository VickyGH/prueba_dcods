from rest_framework import filters
from functools import reduce
from django.db.models import Q
from operator import or_
from core.helpers.methods import get_model
from .models import *
from django.http import JsonResponse


class UserFilter(filters.BaseFilterBackend):
    """
    Filter user Instance For models
    """

    def filter_queryset(self, request, queryset, view):
        user = request.user
        user_id = request.user.id
        result = queryset
        model_query = get_model(queryset.model.objects)
        print('model_query: ' + str(model_query))
        try:
            pk = view.kwargs['pk']
        except:
            pk = None

        if user.is_superuser != True:
            print('si! ' +str(user_id))
            result = queryset.filter(user_id=user_id)

            if model_query == 'Lesson':
                result = result.filter(lesson_id=pk)

        # if model_query == 'Matter':
        #     result = queryset.filter(degree_id=view.kwargs['pk'])
        # if model_query == 'Score':
        #     result = queryset.filter(additional_id=view.kwargs['pk'], content_id=view.kwargs['pk1'])
        # if model_query == 'Module':
        #     print(view.kwargs['pk'])
        #     result = queryset.filter(matter_id=view.kwargs['pk'])
        # if model_query == 'Content':
        #     result = queryset.filter(module_id=view.kwargs['pk'])

        return result


