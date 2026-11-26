from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    contents = util.get_entry(title)
    if contents:
        return render(request, "encyclopedia/article.html", {
            "title": title,
            "contents": util.parse_article(contents)
        })
    else:
        return render(request, "encyclopedia/page_not_found.html", {
            "title": title
        })

def search(request):
    return render(request, "encyclopedia/search.html")