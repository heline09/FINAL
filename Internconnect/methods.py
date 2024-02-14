from django.core.paginator import Paginator


def handle_pagination(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page=per_page)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return page_obj

