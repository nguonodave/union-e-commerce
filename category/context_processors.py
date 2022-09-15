from . models import Category

# creating links for all the available category
# when we use context_processors we have to tell django at the setting file in templates under context_processors list
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)