from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# Create your views here.
class mypagination(PageNumberPagination):
    page_size=10
    page_query_param='mypage'
    page_size_query_param='number'
    max_page_size=15
    last_page_strings=('endpage')
class mypagination2(LimitOffsetPagination):
    #default_limit=20
    offset_query_param='myoffset'
    limit_query_param='mylimit'
    max_limit=20

class mypagination3(CursorPagination):
    ordering='-esal' #descending
    #ordering='esal'
    page_size=30