from django.urls import path
from .views import answer_views, base_views, comment_views, question_views, vote_views

urlpatterns = [

    ## question
    path('',  base_views.index, name="index"),
    path('<int:question_id>/',  base_views.detail, name="detail"),

    # http://127.0.0.1:8000/board/question/create/
    path('question/create/', question_views.question_create, name="question_create"),

    # http://127.0.0.1:8000/board/question/update/1/
    path('question/update/<int:question_id>/', question_views.question_update, name="question_update"),

    # http://127.0.0.1:8000/board/question/delete/1/
    path('question/delete/<int:question_id>/', question_views.question_delete, name="question_delete"),
    

    ### answer
    # http://127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', answer_views.answer_create, name="answer_create"),
    
    # http://127.0.0.1:8000/board/answer/update/1/
    path('answer/update/<int:answer_id>/', answer_views.answer_update, name="answer_update"),
    
    # http://127.0.0.1:8000/board/answer/delete/1/
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name="answer_delete"),


    #### comment
    # http://127.0.0.1:8000/board/comment/create/question/question_id/  comment_question_create
    path('comment/create/question/<int:question_id>/', comment_views.comment_question_create, name="comment_question_create"),

    # http://127.0.0.1:8000/board/comment/update/question/comment_id/  comment_question_update
    path('comment/update/question/<int:comment_id>/', comment_views.comment_question_update, name="comment_question_update"),

    # http://127.0.0.1:8000/board/comment/delete/question/comment_id/  comment_question_delete
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_question_delete, name="comment_question_delete"),    
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_answer_create, name="comment_answer_create"),
    path('comment/update/answer/<int:comment_id>/', comment_views.comment_answer_update, name="comment_answer_update"),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_answer_delete, name="comment_answer_delete"),


    ### vote
    # http://127.0.0.1:8000/board/question/vote/question_id/
    path('question/vote/<int:question_id>/', vote_views.vote_question, name="vote_question"),

    # http://127.0.0.1:8000/board/answer/vote/answer_id/
    path('answer/vote/<int:answer_id>/', vote_views.vote_answer, name="vote_answer"),
]
