import flet as ft
from flet import *

from mongo import connect

def main(page: ft.Page):

    #connect

    tf_user = TextField(hint_text="Nombre de usuario", label="Nombre de usuario")
    tf_password = TextField(hint_text="Contraseña", label="Contraseña", can_reveal_password=True, password=True)
    submit = ElevatedButton(text="Save")

    page.add(tf_user, tf_password, submit)
    page.update()
    connect()

ft.app(main)