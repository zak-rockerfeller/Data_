from projectData.settings import MEDIA_URL, STATIC_URL
from django.shortcuts import render
import browserhistory as bh



# Create your views here.
def loading_page(request,*args, **kwargs):
    return render(request, "index.html", {})


def cypher(request):
    bh.write_browserhistory_csv()
    history = bh.get_browserhistory()

    file = open("browserHistory.txt", "wt", encoding='utf-8')

    for browser_name, history_list in history.items():
        for tuple in history_list:
            file.write(f"""Address: {tuple[0]} Name: {tuple[1]} Date: {tuple[2]}\n""")

    return render(request, "download.html", {})


