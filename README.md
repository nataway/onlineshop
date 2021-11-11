# onlineshop
Các bước:
virtualenv myenv
myenv\scripts\activate
python manage.py runserver


Các bước:
<!-- cai moi truong ao -->
virtualenv myenv
myenv\scripts\activate
<!-- chay moi truong ao de run django -->
source myenv/bin/activate
<!-- run server -->
python3 manage.py runserver
<!-- tao tk admin -->
<!-- muon vao xem csdl vaof link : http://127.0.0.1:8000/admin/ -->
<!-- admin -->
tk: admin
pass: admin123
<!--  -->
python3 manage.py createsuperuser

<!-- sinh ra or cap nhap CSDL -->
python3 manage.py makemigrations
python3 manage.py migrate


<!-- pip install them cai nay -->
pip install social-auth-app-django

<!-- user -->
tk: chi123
pass: chi123456
