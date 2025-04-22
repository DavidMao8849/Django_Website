
# 📖 Django 기반 팀원 소개 웹 애플리케이션

**파이썬 프로그래밍 PBL 프로젝트 - 개인**  
> 프로젝트 기간: 2024년 5월 23일 ~ 2024년 6월 18일

---

## 📌 프로젝트 개요

이 프로젝트는 Django 웹 프레임워크를 활용하여 팀원 소개 및 팀원과 관련된 친구 정보를 보여주는 웹 애플리케이션입니다. <br /> 
사용자는 팀원 및 친구 정보를 **DB에 등록**하고, **UI를 통해 조회/추가**할 수 있으며, Django의 핵심 개념인 **MVT 구조**를 실습하며 이해할 수 있도록 구성되었습니다.

---

## 🛠️ 사용 기술

- Python 3
- tkinter

---

## 🧱 프로젝트 파일 구조

```bash
mysite/
├── pbl/                # 애플리케이션
│   ├── models.py       # Member, Friend 모델 정의
│   ├── views.py        # home, member_detail, friend_list 뷰 정의
│   ├── urls.py         # URL 패턴 정의
│   ├── forms.py        # form 기능 구현
│   ├── templates/
│   │   ├── pbl.html         # 메인 화면 (팀원 목록)
│   │   ├── member.html      # 팀원 상세 정보
│   │   └── friend.html      # 친구 목록
│   └── static/         # JS/CSS 정적 파일
└── manage.py
```

---

## 🧠 주요 기능
- **Main → List → Detail** 구조의 웹 페이지 구현
- **팀원 정보 등록/조회 기능 (form 기반)**
- **팀원의 친구 목록 등록/조회 기능**
- Django의 **admin 기능을 통한 DB 관리**
- **ORM 기반 모델링** (Member & Friend 모델)
- **템플릿 시스템**, **URLconf**, **View 함수**를 통한 화면 구성

---

## 💻 주요 코드 예시

https://github.com/DavidMao8849/Broken_Wall_Game/blob/ca27e4766017649b6c3a8a7911da780f21757c52/breakout%5Btest3%5D.py#L122-L240

---

## 🖼 결과 예시

![시작화면](https://github.com/user-attachments/assets/275f650c-f3e1-48a9-9272-49689506b687)
![결과 화면 승리](https://github.com/user-attachments/assets/4384942d-93ac-4f94-b2fc-fb1cb78494fa)


---

## 💡 활용 방안

- **파이썬 언어를 이용하여 앱을 만들고 UI 화면을 작성할 수 있는 코딩능력 향상**
- **풍부한 라이브러리를 이용해서 복잡한 기능들을 빠르고 쉽게 구현가능하여 인공지능의 구현 결과물을 쉽게 만들 수 있음**

---

## 📎 부록

- 📄 [PBL 결과보고서 PDF](docs/파이썬프로그래밍_1-13주차_PBL_결과보고서(이은우))
