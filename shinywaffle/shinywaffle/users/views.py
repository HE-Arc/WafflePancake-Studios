# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.conf import settings
from django.http import HttpResponseRedirect

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

from friendship.models import Friend, Follow
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from friendship.views import view_friends
from friendship.models import Friend, Follow, FriendshipRequest



get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


@login_required
def user_friends(request, username, template_name='users/user_friends.html'):
    user = get_object_or_404(User, username=username)
    friends = Friend.objects.friends(user)
    followers = Follow.objects.followers(user)
    return render(request, template_name, {
        get_friendship_context_object_name(): user,
        'friendship_context_object_name': get_friendship_context_object_name()
    })

@login_required
def user_addfriend(request, to_username):

    if request.method == 'POST':
        to_user = get_object_or_404(User, username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            messages.add_message(request, messages.ERROR, "%s" % e)

        return redirect('users:detail', username=to_username)

@login_required
def user_removefriend(request, to_username):

    if request.method == 'POST':
        to_user = get_object_or_404(User, username=to_username)
        from_user = request.user
        try:
            Friend.objects.remove_friend(from_user, to_user)
        except AlreadyExistsError as e:
            messages.add_message(request, messages.ERROR, "%s" % e)

        return redirect('users:detail', username=to_username)

@login_required
def user_addfollow(request, to_username):

    if request.method == 'POST':
        followee = User.objects.get(username=to_username)
        follower = request.user
        try:
            Follow.objects.add_follower(follower, followee)
        except AlreadyExistsError as e:
            messages.add_message(request, messages.ERROR, "%s" % e)

        return redirect('users:detail', username=to_username)

@login_required
def user_removefollow(request, to_username):

    if request.method == 'POST':
        followee = User.objects.get(username=to_username)
        follower = request.user
        Follow.objects.remove_follower(follower, followee)

        return redirect('users:detail', username=to_username)

@login_required
def user_detail(request, username, template_name='users/user_detail.html'):
    model = User

    to_user = get_object_or_404(User, username=username)
    friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True,to_user=to_user.id)
    user = get_object_or_404(model, username=username)
    followers = Follow.objects.followers(user)
    friends = Friend.objects.friends(user)
    return render(request, template_name, {'requests': friendship_requests, 'to_user': user, 'followers': followers, 'friends': friends} )

@login_required
def search(request):
    if request.method == 'POST':
        return user_detail(request, request.POST.get("username"))


@login_required
def request_detail(request, friendship_request_id, template_name='users/user_request.html'):
    """ View a particular friendship request """
    f_request = get_object_or_404(FriendshipRequest, id=friendship_request_id)

    return render(request, template_name, {'friendship_request': f_request})

@login_required
def request_accept(request, friendship_request_id):
    if request.method == 'POST':
        f_request = get_object_or_404(
            FriendshipRequest,
            id=friendship_request_id)
        f_request.accept()

    return redirect('home')

@login_required
def request_reject(request, friendship_request_id):
    """ Reject a friendship request """
    if request.method == 'POST':
        f_request = get_object_or_404(
            FriendshipRequest,
            id=friendship_request_id)
        f_request.reject()

    return redirect('home')

@login_required
def request_cancel(request, friendship_request_id):
    """ Reject a friendship request """
    if request.method == 'POST':
        f_request = get_object_or_404(
            FriendshipRequest,
            pk=friendship_request_id)
        f_request.cancel()

    return redirect('home')
