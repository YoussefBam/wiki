from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    page_name="index"
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),"page_name":page_name
    })

#generate content page 
def generate(request,title):
    page_name="content_page"
    try:
        #get contents of md file and convert it to html
        content=markdown(util.get_entry(title))
    except:
        #case where title's content page is not found
        content=None
    finally:
        return render(request,"encyclopedia/index.html",{
            "content":content,"title":title, "page_name":page_name
        })





    

