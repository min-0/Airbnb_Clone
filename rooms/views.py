#from django.http import HttpResponse
#from datetime import datetime
from django.shortcuts import render
from . import models

def all_rooms(request):
    # return HttpResponse(content="<h1>hello</h1>")
    # return HttpResponse(content=f"<h1>{now}</h1>")

    # now = datetime.now()
    # hungry = True
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})

    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms":all_rooms})


""" html 파일에서 변수를 보여주고 싶을 땐 {{변수명}}
장고 템플릿을 쓸 땐 {{% if %}} {{% else %}} {{% endif %}} / {{% for in %}} {{% endfor %}}
endif, endfor을 써주어야 함 """

"""
Html에 있는 template 이름과 view에 있는 extension 이름은 같아야 함
View에 있는 함수 이름과 urls.py에 있는 이름은 같아야 함
"""