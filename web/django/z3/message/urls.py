#from django.urls import path, include
#from .views import inbox, Directs, SendDirect,message

#app_name = 'message'

#urlpatterns = [
#    path('inbox/', inbox, name='inbox'),
#    path('directs/<username>', Directs, name='directs'),
#    path('send/<username>', SendDirect, name='send_direct'),
#]


from django.urls import path
from .views import Inbox, UserSearch, Directs, NewConversation, SendDirect
#urlpatterns = [
#   	path('', Inbox, name='inbox'),
#   	path('directs/<name>', Directs, name='directs'),
#   	path('new/', UserSearch, name='usersearch'),
#   	path('new/<name>', NewConversation, name='newconversation'),
#   	path('send/', SendDirect, name='send_direct'),

#]

app_name = 'message'

urlpatterns = [
    path('', Inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/<username>', SendDirect, name='send_direct'),
]
