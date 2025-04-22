from django.contrib import admin
from .models import Member, Friend

#admin.site.register(Member) = models.py의 Member 클래스를 불러와 admin사이트에 등록
#admin.site.register(Friend) = models.py의 Friend 클래스를 불러와 admin사이트에 등록
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin): #이는 더 가시성이 좋게 테이블의 데이터값도 표현해줌
    list_display = ('name', 'student_id', 'hobby')  # 관리자 페이지에 표시할 필드

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'relation', 'member')  # 관리자 페이지에 표시할 필드
