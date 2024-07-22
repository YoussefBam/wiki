from django.shortcuts import render
from markdown2 import markdown
from . import util
from random import choice


def index(request):
    page_name="index"
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),"page_name":page_name
    })

#rendering desired page 
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
    

def search(request):
    title=request.GET.get('title')
    if title in util.list_entries() :
        return generate(request, title)
    else :
        page_name="search_error"
        return render(request,"encyclopedia/index.html",{
            "title":title, "entries": util.list_entries(),"page_name":page_name
        })

def view_create(request):
    return render(request,"encyclopedia/add.html")

def create(request):
    #get all titles in list
    title_list=util.list_entries()
    #get title of desired page to create
    title=request.POST.get('title')

    #case where the title already exists (returning error)
    if title in title_list :
        error=True 
        return render(request,"encyclopedia/add.html", {"error":error, "title":title

        })
    #case where title doesn't exist
    else :
        #get content
        content=request.POST.get('content')
        #save content with its title in a markdown file.
        util.save_entry(title, content)
        #rendering created page
        return generate(request,title)

    
def edit(request,title):
        #get contents of md file and convert it to html
        content=util.get_entry(title)
        return render(request,"encyclopedia/edit.html", {"content":content,"title":title
} )


def save(request,title):
    content=request.POST.get('content')
    util.save_entry(title, content)
    #rendering created page
    return generate(request,title)
    
    
def random(request):
    title_list=util.list_entries()
    title = choice(title_list)
    #rendering random page
    return generate(request,title)




    

