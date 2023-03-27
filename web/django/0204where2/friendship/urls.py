from django.urls import path
from friendship.views import (
    all_users,
    block_add,
    block_remove,
    blockers,
    blocking,
    follower_add,
    follower_remove,
    followers,
    following,
    friendship_accept,
    friendship_add_friend,
    friendship_cancel,
    friendship_reject,
    friendship_request_list,
    friendship_request_list_rejected,
    friendship_requests_detail,
    view_friends,
    friendship_remove
)

app_name = "friendship"

urlpatterns = [
    path("friends/", view=all_users, name="search_friends"),
    path(
        "friends/<slug:name>/",
        view=view_friends,
        name="friendship_view_friends",
    ),
    path(
        "friend/add/<slug:to_name>/",
        view=friendship_add_friend,
        name="friendship_add_friend",
    ),
    path(
        "friend/accept/<int:friendship_request_id>/",
        view=friendship_accept,
        name="friendship_accept",
    ),
    path(
        "friend/reject/<int:friendship_request_id>/",
        view=friendship_reject,
        name="friendship_reject",
    ),
    path(
        "friend/cancel/<int:friend_id>/",
        view=friendship_cancel,
        name="friendship_cancel",
    ),
    path(
        "friend/requests/",
        view=friendship_request_list,
        name="friendship_request_list",
    ),
    path(
        "friend/requests/rejected/",
        view=friendship_request_list_rejected,
        name="friendship_requests_rejected",
    ),
    path(
        "friend/request/<int:friendship_request_id>/",
        view=friendship_requests_detail,
        name="friendship_requests_detail",
    ),
    path(
        "followers/<slug:name>/",
        view=followers,
        name="friendship_followers",
    ),
    path(
        "following/<slug:name>/",
        view=following,
        name="friendship_following",
    ),
    path(
        "follower/add/<slug:followee_name>/",
        view=follower_add,
        name="follower_add",
    ),
    path(
        "follower/remove/<slug:followee_name>/",
        view=follower_remove,
        name="follower_remove",
    ),
    path(
        "blockers/<slug:name>/",
        view=blockers,
        name="friendship_blockers",
    ),
    path(
        "blocking/<slug:name>/",
        view=blocking,
        name="friendship_blocking",
    ),
    path(
        "block/add/<slug:blocked_name>/",
        view=block_add,
        name="block_add",
    ),
    path(
        "block/remove/<slug:blocked_name>/",
        view=block_remove,
        name="block_remove",
    ),
    path(
        "friend/remove/<int:friend_id>/",
        view=friendship_remove,
        name="friendship_remove",
    )
]