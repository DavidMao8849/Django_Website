from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm, FriendForm

def home(request):
    members = Member.objects.all()
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # 새로 추가 후 목록 새로고침
    else:
        form = MemberForm()

    context={'members': members, 'form': form,}

    return render(request, 'pbl.html', context)

def member_detail(request, membered):
    member = get_object_or_404(Member, id=membered)
    return render(request, 'member.html', {'member': member})

def friend_list(request, membered):
    member = get_object_or_404(Member, id=membered)
    friends = member.friends.all()
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.member = member  # 연결된 팀원 지정
            friend.save()
            return redirect('friend_list', membered=member.id)  # 새로고침
    else:
        form = FriendForm()

    context={'member': member, 'friends': friends, 'form': form,}

    return render(request, 'friend.html', context)

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # 메인 페이지로 리다이렉트
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})