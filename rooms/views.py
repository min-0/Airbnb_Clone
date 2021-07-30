#from django.http import HttpResponse
#from datetime import datetime
from math import ceil
from django.shortcuts import render
from . import models

def all_rooms(request):
    # return HttpResponse(content="<h1>hello</h1>")
    # return HttpResponse(content=f"<h1>{now}</h1>")

    # now = datetime.now()
    # hungry = True
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})

    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit] #offset and limit
    page_count = models.Room.objects.count()/page_size
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )


""" html 파일에서 변수를 보여주고 싶을 땐 {{변수명}}
장고 템플릿을 쓸 땐 {{% if %}} {{% else %}} {{% endif %}} / {{% for in %}} {{% endfor %}}
endif, endfor을 써주어야 함 """

"""
Html에 있는 template 이름과 view에 있는 extension 이름은 같아야 함
View에 있는 함수 이름과 urls.py에 있는 이름은 같아야 함
"""