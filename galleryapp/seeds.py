from .models import Usuario


def generate_usuarios():
    usuarios = [
        { 'username': 'jose', 'password': '1ec4ed037766aa181d8840ad04b9fc6e195fd37dedc04c98a5767a67d3758ece'},
        { 'username': 'ana', 'password': '24d4b96f58da6d4a8512313bbd02a28ebf0ca95dec6e4c86ef78ce7f01e788ac'},
        { 'username': 'pedro', 'password': 'ee5cd7d5d96c8874117891b2c92a036f96918e66c102bc698ae77542c186f981'},
        { 'username': 'karla', 'password': '1cfcffbd0d0536e2b354a0bbe9a0df8f7c15b26293e99ce5bd468e1716154295'},
        { 'username': 'juan', 'password': 'ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca'},
    ]

    try:
        for u in usuarios:
            usuario = Usuario(username=u['username'], password=u['password'])
            usuario.save()
    except Exception as ex:
        pass

