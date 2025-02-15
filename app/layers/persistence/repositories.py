# capa DAO de acceso/persistencia de datos.

from sqlite3 import IntegrityError
from app.models import Favourite


def is_favourite(user, image):

    favourites = Favourite.objects.all()  # Traemos todos los registros de favoritos
    
    favourite_images = []
    
    for fav in favourites:
        if fav.user == user and fav.image == image:
            favourite_images.append(fav.image)
    
    # Ahora verificamos si la lista 'favourite_images' contiene la imagen que estamos buscando
    if image in favourite_images:
        return True
    else:
        return False
    
def save_favourite(fav):
    try:
        fav = Favourite.objects.create(
            name=fav.name,  # Nombre del personaje
            gender=fav.gender,  # Género
            house=fav.house,  # Casa
            actor=fav.actor,  # Actor
            image=fav.image,  # Imagen
            
            user=fav.user  # Usuario autenticado
        )
        return fav
    except IntegrityError as e:
        print(f"Error de integridad al guardar el favorito: {e}")
        return None
    except KeyError as e:
        print(f"Error de datos al guardar el favorito: Falta el campo {e}")
        return None


def get_all_favourites(user):
    return Favourite.objects.filter(user=user).values('id', 'name', 'gender', 'house', 'actor', 'image')


def delete_favourite(fav_id):
    try:
        favourite = Favourite.objects.get(id=fav_id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {fav_id} no existe o no pertenece al usuario.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False
