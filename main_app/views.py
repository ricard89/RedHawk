# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from main_app.models import Tag
from main_app.forms import TagForm


def index(request):
    return render(request, 'main_app/index.html')


@login_required
def add_tag(request):

    if request.method == "POST":
        form = TagForm(request.POST, user=request.user)

        if form.is_valid():
            tag_form = form.save(commit=False)
            tag_form.owner = request.user
            tag_form.save()
            return tags(request)
        else:
            print('ERROR: FORM INVALID')
    else:
        form = TagForm(user=request.user)

    context = {'form': form}
    return render(request, 'main_app/add_tag.html', context)


@login_required
def delete_tag(request, tag_id):
    query = Tag.objects.get(num_ID=tag_id, owner=request.user)
    query.delete()
    return tags(request)


@login_required
def update_tag_value(request, tag_id):
    if request.method == "POST":
        if request.POST.get('tag_value', False):
            try:
                value = int(request.POST['tag_value'])
            except ValueError:
                print("fail to update tag")
            query = Tag.objects.filter(num_ID=tag_id, owner=request.user).update(value=value)

        else:
            try:
                query = Tag.objects.filter(num_ID=tag_id, owner=request.user).values_list("value", flat=True)[0]
                query_int = int(query)
            except ValueError:
                query_int = 0

            if query_int == 1:
                Tag.objects.filter(num_ID=tag_id, owner=request.user).update(value=0)
            else:
                Tag.objects.filter(num_ID=tag_id, owner=request.user).update(value=1)

    return taglist(request)


@login_required
def taglist(request):
    tag_filter_list = Tag.objects.filter(owner=request.user)
    tag_list = tag_filter_list.order_by('num_ID')
    context = {'tag_list': tag_list}
    return render(request, 'main_app/taglist.html', context)
