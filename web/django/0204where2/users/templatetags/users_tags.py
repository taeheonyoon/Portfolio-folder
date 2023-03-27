from django import template

from board.models import Post
from review.models import Review
from ..models import User
from friendship.models import Friend, FriendshipManager, FriendshipRequest, Follow, Block

register = template.Library()


@register.simple_tag
def recent_post(count, uid):
    id = User.objects.get(id=uid)
    posts = Post.objects.filter(author=id).order_by('-create_date')[:count]
    return posts

@register.simple_tag
def count_post(uid):
    id = User.objects.get(id=uid)
    posts = Post.objects.filter(author=id).count()
    return posts

@register.simple_tag
def recent_review(count, uid):
    id = User.objects.get(id=uid)
    reviews = Review.objects.filter(user=id).order_by('-created_at')[:count]
    return reviews

@register.simple_tag
def count_review(uid):
    id = User.objects.get(id=uid)
    reviews = Review.objects.filter(user=id).count()
    return reviews

@register.simple_tag(takes_context=True)
def get_by_name(context, name):
    """Tag to lookup a variable in the current context."""
    return context[name]


@register.simple_tag
def friendlist(user):
    """
    Simple tag to grab all friends
    """
    id = User.objects.get(id=user)
    friendlist = Friend.objects.friends(id)
    return friendlist

@register.inclusion_tag("friendship/templatetags/followers.html")
def followers(user):
    """
    Simple tag to grab all followers
    """
    return {"followers": Follow.objects.followers(user)}


@register.inclusion_tag("friendship/templatetags/following.html")
def following(user):
    """
    Simple tag to grab all users who follow the given user
    """
    return {"following": Follow.objects.following(user)}


@register.inclusion_tag("friendship/templatetags/blockers.html")
def blockers(user):
    """
    Simple tag to grab all followers
    """
    return {"blockers": Block.objects.blocked(user)}


@register.inclusion_tag("friendship/templatetags/blocking.html")
def blocking(user):
    """
    Simple tag to grab all users who follow the given user
    """
    return {"blocking": Block.objects.blocking(user)}


@register.simple_tag
def friend_requests(user):
    """
    Inclusion tag to display friend requests
    """
    id = User.objects.get(id=user)
    friend_requests = Friend.objects.requests(id)
    
    return friend_requests

@register.inclusion_tag("friendship/templatetags/friend_request_count.html")
def friend_request_count(user):
    """
    Inclusion tag to display the count of unread friend requests
    """
    return {"friend_request_count": Friend.objects.unread_request_count(user)}


@register.inclusion_tag("friendship/templatetags/friend_count.html")
def friend_count(user):
    """
    Inclusion tag to display the total count of friends for the given user
    """
    return {"friend_count": len(Friend.objects.friends(user))}


@register.inclusion_tag("friendship/templatetags/friend_rejected_count.html")
def friend_rejected_count(user):
    """
    Inclusion tag to display the count of rejected friend requests
    """
    return {"friend_rejected_count": len(Friend.objects.rejected_requests(user))}