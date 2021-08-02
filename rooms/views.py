# from django.http import HttpResponse
# from datetime import datetime, timezone
# from django.core.paginator import EmptyPage, Paginator
# from django.core import exceptions, paginator
# from django.http import Http404
# from django.urls import 
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django_countries import countries
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
    
    
#FBV 방식
""" def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room":room})
    except models.Room.DoesNotExist:
        raise Http404()
        #return redirect(reverse("core:home"))
"""

#CBV 방식
class RoomDetail(DetailView):

    """ RoomDetail Definition """
    
    model = models.Room
    #pk_url_kwarg = "pk"

def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR ")
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    room_types = models.RoomType.objects.all()

    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(request, "rooms/search.html", {**form, **choices})