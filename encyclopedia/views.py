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
    
#dirty fix that i'm not happy with 
def search(request):
    title=request.GET.get('title')
    page_name="searched_page"
    try:
        #get contents of md file and convert it to html
        content=markdown(util.get_entry(title))
    except:
        #case where title's content page is not found
        content=None
    finally:
        return render(request,"encyclopedia/index.html",{
            "content":content,"title":title, "page_name":page_name, "entries": util.list_entries()
        })

def view_create(request):
    return render(request,"encyclopedia/add.html")

def create(request):
    #get all titles in list
    title_list=util.list_entries()
    #get title of desired page to create
    title=request.POST.get('title')

    #case where the title exists (returning error)
    if title in title_list :
        error=True 
        return render(request,"encyclopedia/add.html", {"error":error, "title":title

        })
    #case where title doesn't exist
    else :
        #get content
        content=request.POST.get('content')
        #save content in markdown file.
        util.save_entry(title, content)
        #convert content to html
        content=markdown(util.get_entry(title))
        #validate page name so index conditonal will be true and will output the contents.
        page_name="content_page"
        return render(request,"encyclopedia/index.html",{
            "content":content,"title":title, "page_name":page_name
        })

    

 
    
    
    




    

