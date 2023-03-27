from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from friendship.models import Friend, Follow, Block, FriendshipRequest
from django.conf import settings
from django.contrib.auth.decorators import login_required
from friendship.exceptions import AlreadyExistsError

try:
    from users.models import User
    
    user_model = User
except ImportError:
    from users.models import User
    
    user_model = User


def get_friendship_context_object_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_NAME", "user")


def get_friendship_context_object_list_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME", "users")


def view_friends(request, name, template_name="friendship/friend/user_list.html"):
    """View the friends of a user"""
    user = get_object_or_404(user_model, name=name)
    friends = Friend.objects.friends(user)
    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
            "friends": friends,
        },
    )


@login_required
def friendship_add_friend(
    request, to_name, template_name="friendship/friend/add.html"
):
    """Create a FriendshipRequest"""
    ctx = {"to_name": to_name}
    print("to_name", to_name)
    
    
    if request.method == "POST":
        to_user = user_model.objects.get(name=to_name)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            print("else")
            return redirect("friendship:friendship_request_list")

    return render(request, template_name, ctx)


@login_required
def friendship_accept(request, friendship_request_id):
    """Accept a friendship request"""
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id
        )
        f_request.accept()
        return redirect("friendship_view_friends", name=request.user.name)

    return redirect(
        "friendship_requests_detail", friendship_request_id=friendship_request_id
    )


@login_required
def friendship_reject(request, friendship_request_id):
    """Reject a friendship request"""
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id
        )
        f_request.reject()
        return redirect("friendship_request_list")

    return redirect(
        "friendship_requests_detail", friendship_request_id=friendship_request_id
    )


@login_required
def friendship_cancel(request,friend_id):
    """Cancel a previously created friendship_request_id : 친구요청 삭제"""
    
    print("삭제할 친구 아이디",friend_id) # User
    
    # friendship_request_id 모델 찾아오기
    if request.method == "POST":   
       
        # 
        drop_frined = get_object_or_404(Friend, from_user=friend_id)
        print("drop", drop_frined)
        
        drop_frined.cancel()
        
        return redirect("friendship:friendship_request_list")

    return redirect(
        "friendship_requests_detail", friendship_request_id=request.user
    )

@login_required
def friendship_request_list(
    request, template_name="friendship/friend/requests_list.html"
):
    """View unread and read friendship requests"""
    friendship_requests = Friend.objects.requests(request.user)
    # This shows all friendship requests in the database
    # friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True)

    return render(request, template_name, {"requests": friendship_requests})


@login_required
def friendship_request_list_rejected(
    request, template_name="friendship/friend/requests_list.html"
):
    """View rejected friendship requests"""
    # friendship_requests = Friend.objects.rejected_requests(request.user)
    friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=False)

    return render(request, template_name, {"requests": friendship_requests})


@login_required
def friendship_requests_detail(
    request, friendship_request_id, template_name="friendship/friend/request.html"
):
    """View a particular friendship request"""
    f_request = get_object_or_404(FriendshipRequest, id=friendship_request_id)

    return render(request, template_name, {"friendship_request": f_request})


def followers(request, name, template_name="friendship/follow/followers_list.html"):
    """List this user's followers"""
    user = get_object_or_404(user_model, name=name)
    followers = Follow.objects.followers(user)
    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
            "followers": followers,
        },
    )


def following(request, name, template_name="friendship/follow/following_list.html"):
    """List who this user follows"""
    user = get_object_or_404(user_model, name=name)
    following = Follow.objects.following(user)
    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
            "following": following,
        },
    )


@login_required
def follower_add(
    request, followee_name, template_name="friendship/follow/add.html"
):
    """Create a following relationship"""
    ctx = {"followee_name": followee_name}

    if request.method == "POST":
        followee = user_model.objects.get(name=followee_name)
        follower = request.user
        try:
            Follow.objects.add_follower(follower, followee)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect("friendship_following", name=follower.name)

    return render(request, template_name, ctx)


@login_required
def follower_remove(
    request, followee_name, template_name="friendship/follow/remove.html"
):
    """Remove a following relationship"""
    if request.method == "POST":
        followee = user_model.objects.get(name=followee_name)
        follower = request.user
        Follow.objects.remove_follower(follower, followee)
        return redirect("friendship_following", name=follower.name)

    return render(request, template_name, {"followee_name": followee_name})


def all_users(request, template_name="friendship/user_actions.html"):
    users = user_model.objects.all()

    return render(
        request, template_name, {get_friendship_context_object_list_name(): users}
    )


def blocking(request, name, template_name="friendship/block/blockers_list.html"):
    """List this user's followers"""
    user = get_object_or_404(user_model, name=name)
    Block.objects.blocked(user)

    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
        },
    )


def blockers(request, name, template_name="friendship/block/blocking_list.html"):
    """List who this user follows"""
    user = get_object_or_404(user_model, name=name)
    Block.objects.blocking(user)

    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
        },
    )


@login_required
def block_add(request, blocked_name, template_name="friendship/block/add.html"):
    """Create a following relationship"""
    ctx = {"blocked_name": blocked_name}

    if request.method == "POST":
        blocked = user_model.objects.get(name=blocked_name)
        blocker = request.user
        try:
            Block.objects.add_block(blocker, blocked)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect("friendship_blocking", name=blocker.name)

    return render(request, template_name, ctx)


@login_required
def block_remove(
    request, blocked_name, template_name="friendship/block/remove.html"
):
    """Remove a following relationship"""
    if request.method == "POST":
        blocked = user_model.objects.get(name=blocked_name)
        blocker = request.user
        Block.objects.remove_block(blocker, blocked)
        return redirect("friendship_blocking", name=blocker.name)

    return render(request, template_name, {"blocked_name": blocked_name})

#remove_friend
@login_required
def friendship_remove(
    request, friend_name, template_name="friendship/friend/user_list.html"
):
    """Remove a friendship"""
    if request.method == "POST":
        friend = user_model.objects.get(name=friend_name)
        user = request.user
        Friend.objects.remove_friend(user, friend)
        return redirect("friendship_friend_list")

    return render(request, template_name, {"friend_name": friend_name}
)