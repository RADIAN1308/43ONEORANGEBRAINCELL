from collections.abc import Container

import flet as ft
from flet.core.icons import Icons


def main(page: ft.Page):
    page.title = ""
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    #Main app view

    search_page = ft.Container(
        border_radius=20,
        padding=40,
        bgcolor="#0F0F0F",

        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(bgcolor="#232D3F",
                                     padding=0,
                                     content=ft.Row(

                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    content=ft.Icon(Icons.MENU_ROUNDED)
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(Icons.NOTIFICATIONS_ROUNDED),
                                            ft.Icon(Icons.PERSON_2_ROUNDED)
                                        ]
                                    )
                                )

                            ]

                        ),
                            ),
                        ft.Container(height=40)
                        ]
                )

                ,ft.Row(
                            controls=[ft.TextField(hint_text="What query must be processed?", expand=True),

                          ]
                    )
                , ft.Row(
                    controls=[
                              ft.ElevatedButton(icon=Icons.SEARCH_ROUNDED,)
                              ]
                )
            ]
        )
    )








    page.add(search_page)




ft.app(main)