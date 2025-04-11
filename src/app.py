from collections.abc import Container

import flet as ft
import time
from flet.core.icons import Icons




def main(page: ft.Page):
    page.title = ""
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    bar_cont = ft.Container()

    def result_handler(e):
        r_val = 0

        bar_cont.content = ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee", value=None)
        page.update()

        while r_val < 1:
            time.sleep(0.2)
            r_val += 0.1
            print(r_val)

        bar_cont.content = None
        page.update()

        lv = ft.ListView(expand=0, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(ft.Text(""))
        page.add(lv)

    #Main app view

    search_page = ft.Container(
        border_radius=20,
        padding=40,
        bgcolor="#0F0F0F",

        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(

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
                        ft.Container(height=40)
                        ]
                )

                ,ft.Row(
                            controls=[ft.TextField(hint_text="What query must be processed?", expand=True),ft.ElevatedButton("Search",icon=Icons.SEARCH_ROUNDED,on_click=result_handler)

                          ]
                    )
            ]
        ))

    page.add(search_page)
    )





ft.app(main)