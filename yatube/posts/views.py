from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request,):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'title': f'Записи сообщества {slug}',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
