# search/views.py
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page


def search(request):
    search_query = request.GET.get("query", "").strip()
    page = request.GET.get("page", 1)

    if search_query:
        search_qs = (
            Page.objects.live()
            .public()
            .search(search_query)
        )
    else:
        search_qs = Page.objects.none()

    paginator = Paginator(search_qs, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
