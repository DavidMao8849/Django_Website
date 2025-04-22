
# 📖 Django 기반 팀원 소개 웹 애플리케이션

**파이썬 프로그래밍 PBL 프로젝트 - 개인**  
> 프로젝트 기간: 2024년 11월 23일 ~ 2024년 12월 1일

---

## 📌 프로젝트 개요

이 프로젝트는 Django 웹 프레임워크를 활용하여 팀원 소개 및 팀원과 관련된 친구 정보를 보여주는 웹 애플리케이션입니다. <br /> 
사용자는 팀원 및 친구 정보를 **DB에 등록**하고, **UI를 통해 조회/추가**할 수 있으며, Django의 핵심 개념인 **MVT 구조**를 실습하며 이해할 수 있도록 구성되었습니다.

---

## ⚙ 주요 기능
- **Main → List → Detail** 구조의 웹 페이지 구현
- **팀원 정보 등록/조회 기능 (form 기반)**
- **팀원의 친구 목록 등록/조회 기능**
- Django의 **admin 기능을 통한 DB 관리**
- **ORM 기반 모델링** (Member & Friend 모델)
- **템플릿 시스템**, **URLconf**, **View 함수**를 통한 화면 구성

---

## 🛠️ 사용 기술

- Python 3
- Django
- HTML/CSS, JavaScript
- SQLite (Django ORM 기반)
- Django 핵심 개념
  └── MVT 패턴
  └── ORM 활용
  └── Form 처리 및 validation
  └── Static 파일 관리
  └── URL dispatcher
  └── 관리자(admin) 기능

---

## 🧱 프로젝트 파일 구조

```bash
Team_Member/
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


## 💻 주요 코드 예시



---

## 🖼 결과 화면
![image](https://github.com/user-attachments/assets/8a3192cc-67ca-4c60-81a9-3e6c44095c0d)
- pbl.html - 팀원 리스트 및 팀원 추가 폼
https://github.com/DavidMao8849/Django_Website/blob/4eb599c18984b3645bbfddd3f362bc53b2da22a8/pbl/templates/pbl.html#L1-L27
---
![image](https://github.com/user-attachments/assets/3c4f5986-83b5-4fb9-bcf6-2b392f3245b8)
- member.html - 팀원 상세 정보 및 친구 목록으로 이동 링크
https://github.com/DavidMao8849/Django_Website/blob/4eb599c18984b3645bbfddd3f362bc53b2da22a8/pbl/templates/member.html#L1-L9
---
![image](https://github.com/user-attachments/assets/e857a96a-af42-4ec0-8dc9-fb6ef03a0753)
- friend.html - 친구 리스트 및 친구 추가 폼
https://github.com/DavidMao8849/Django_Website/blob/4eb599c18984b3645bbfddd3f362bc53b2da22a8/pbl/templates/member.html#L1-L9

![image](https://github.com/user-attachments/assets/1269ae6d-d10d-4448-a2a4-f994cebf5e85)

![image](https://github.com/user-attachments/assets/cacc9a50-9caa-4b6f-b7c1-8cd962d3f706)

---

## 💡 활용 방안

- **Django 웹 개발의 핵심 개념인 MVT 아키텍처, DB 모델링, 폼 처리, 템플릿 시스템 등을 실습하고 습득**
- **이를 기반으로 향후 AI 기능이 연동된 웹 서비스로 확장할 수 있는 가능성**

---

## 📎 부록

- 📄 [PBL 결과보고서 PDF](docs/파이썬프로그래밍_1-13주차_PBL_결과보고서(이은우))
