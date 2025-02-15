# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def getAllImagesAndFavouriteList(request):
    #obtenemos todas las imagenes de la API
    images = services.getAllImages()

    if request.user.is_authenticated:
        favourite_list = services.getAllFavourites(request.user)
    else:
        favourite_list = []

    return images, favourite_list

def home(request):
    # Llama a la funcion auxiliar getAllImagesFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario
    images, favourite_list = getAllImagesAndFavouriteList(request)

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })


# función utilizada en el buscador.
def search(request):

    name = request.GET.get('query', '')
    images, favourite_list = getAllImagesAndFavouriteList(request)

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    images_coin = []

    if name: 
        for img in images:
            if name.lower() in img.name.lower():
                images_coin.append(img) # Agregamos la imagen a la lista images = []
            
            favourite_list = []
        return render(request, 'home.html', { 'images': images_coin, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por casa Gryffindor o Slytherin.
def filter_by_house(request):

    house = request.POST.get('house', '')
    images, favourite_list = getAllImagesAndFavouriteList(request)

    images_coin = [] # debe traer un listado filtrado de imágenes, según la casa.

    if house:
        for img in images:
            if house == img.house:
                images_coin.append(img)
        favourite_list = []

        return render(request, 'home.html', { 'images': images_coin, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    pass

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')