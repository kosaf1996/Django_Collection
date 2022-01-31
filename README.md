# Django_Collection
1.uuid code 생성
- UUID란 네트워크 상에서 고유성이 보장되는 id를 만들기 위한 표준 규약
- sales/model.py
- sales/utils.py

2:55:01

2. m2m_changed, receiver -> Django Signal
- 모델 인스턴스에서 ManyToMantField 가 변경 될떄 전송
- 모델 변경 사항을 추적 할 때 pre_save / post_save 및 pre_delete / post_delete 를 보완
- sales/models.py
- sales/signals.py
- sales/apps.py
- sales/__init__.py


3. CSV
- sales/model.py

4.DetailView ,ListView
- ListView List로 표시 (예: 게시판 글 목록 전체)
- DetailView Detail 내용 표시 (예 : 게시판의 특정 글 상세 내용)
- sales/view.py
- sales/urls.py
- sales.models.py
- sales/templates/detail.html
- sales/templates/main.html


5. OneToOneField 1:1 관계를 의미합니다.
- profiles/models.py
- django 에 기본적으로 정의되어 있는 User 모델과 이를 커스튬하여 새로 만드는 Profile 모델을 연결해줄 때 자주 사용합니다.
- 반대로 ManyToManyField 는 다대다 관계이다.

6. URL Reverse
- Django 는 urls.py 변경을 통해 ‘각 뷰에 대한’ url이 변경되는 유연한 시스템을 갖고 있다
- url이 변경 되더라도 url reverse가 변경된 url을 추적한다.
- sales/urls.py
- sales/models.py
- sales/templates/main.html

7. Search Form
- sales/forms.py
- sales/view.py
- sales/templates/home.html

8. pandas 활용 데이터 프레임 & 데이터 프레임 치환 & 데이터 프레임 병합
- sales/view.py
- sales/templates/home.html

##
정리
Djnago Signal ★★★★★중요
- 어떤 특정한 일을 수행할 때마다 알려줄 것을 설정하고,
- 그 때에 지정한 동작을 수행할 수 있게 하는 신호 "signal"를 발생하는 기능

upload_to='path'
- model 생성시 이미지나 파일의 경로를 지정한다. 저장 경로 예제) media/path/test.jpg

LoginRequiredMixin
- 인증된 사용자만 접근할 수 있게 설정

csrf_token
- CSRF 공격을 방어하기 위한 다양한 방법이 있지만 Django에서는 기본적으로 csrf token을 이용

Django-crispy-forms
- 폼 레이아웃의 고급 기능들. 폼을 트위터의 부트스트랩 폼 엘리먼트와 스타일로 보여준다.
- django-floppyforms 와 함께 쓰기 좋아서 빈번하게 함께 쓰인다.

to_html | safe
- pandas 의 데이터프레임 형태를 html 로 변경
- html 에서 {{ sales_df|safe }} 와 같이 데이터를 출력하면 html 형태에 맞춰 출력한다.
