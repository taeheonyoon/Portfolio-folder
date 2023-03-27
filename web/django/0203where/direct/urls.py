from django.urls import path
from direct.views import Inbox, UserSearch, Directs, NewConversation, SendDirect
urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('directs/<name>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<name>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),

]