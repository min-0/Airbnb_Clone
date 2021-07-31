#from django.http import HttpResponse
#from datetime import datetime, timezone
from django.core import paginator
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import ListView
from . import models

"""
def all_rooms(request):
    # return HttpResponse(content="<h1>hello</h1>")
    # now = datetime.now()
    # hungry = True
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
    
    page = request.GET.get("page", 1) #default 값 1
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    
    try:
        rooms = paginator.page(int(page))
        return render(request,"rooms/home.html",{"page": rooms})
    except EmptyPage:
        return redirect("/")
"""

""" html 파일에서 변수를 보여주고 싶을 땐 {{변수명}}
장고 템플릿을 쓸 땐 {{% if %}} {{% else %}} {{% endif %}} / {{% for in %}} {{% endfor %}}
endif, endfor을 써주어야 함 """

"""
Html에 있는 template 이름과 view에 있는 extension 이름은 같아야 함
View에 있는 함수 이름과 urls.py에 있는 이름은 같아야 함
"""

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        context["now"] = now
        return context"""
    
    def room_detail(request, pk):
        print(pk)
        return render(request, "rooms/detail.html")
