from flet import *
import time
import test as t

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.title = ""
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.update()

    bar_cont = Container()

    def result_handler(e):
        r_val = 0
        bar_cont.content = ProgressBar(width=400, color="amber", bgcolor="#eeeeee", value=None)
        page.update()

        while r_val < 1:
            time.sleep(0.2)
            r_val += 0.1
            print(r_val)

        bar_cont.content = None
        page.update()


        lv = ListView(expand=0, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(Text(""))
        page.add(lv)

    def handle_change(e):
        if e.control.selected_index == 0:
            page.controls.clear()
            page.controls.append(home_screen)
        elif e.control.selected_index == 1:
            page.controls.clear()
            page.controls.append(settings_screen)
        elif e.control.selected_index == 2:
            print("to be implemented")
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()

    def placeholder(e):
        print("L")

    drawer = NavigationDrawer(
        on_change=handle_change,
        controls=[
            Container(height=12),
            NavigationDrawerDestination(
                label="Home",
                icon=Icons.HOME_ROUNDED,
                selected_icon=Icon(Icons.HOME_ROUNDED),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                icon=Icon(Icons.SEARCH_ROUNDED),
                label="Search",
                selected_icon=Icons.SEARCH_ROUNDED,
            ),
                NavigationDrawerDestination(
                icon=Icon(Icons.CALENDAR_MONTH_ROUNDED),
                label="Item 3",
                selected_icon=Icons.CALENDAR_MONTH_ROUNDED,
            ),
        ],
    )

    c_val = TextField(label="Enter company name", hint_text="Please enter text here")

    app = Container()

    home_screen = Column(
        [
            Container(
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    content=IconButton(Icons.MENU, on_click=lambda e: page.open(drawer))
                                ),
                                Row(
                                    controls=[
                                        IconButton(Icons.LIGHT_MODE_OUTLINED, on_click=toggle_theme),
                                        IconButton(Icons.CONTACT_SUPPORT, on_click=lambda _: print("L"))
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
            app
        ]
    )

    settings_screen = Column(
        [
            Container(
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    content=IconButton(Icons.MENU, on_click=lambda e: page.open(drawer))
                                ),
                                Row(
                                    controls=[
                                        IconButton(Icons.LIGHT_MODE_OUTLINED, on_click=toggle_theme),
                                        IconButton(Icons.CONTACT_SUPPORT, on_click=lambda _: print("L"))
                                    ]
                                )
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                c_val,
                                ElevatedButton(text="Submit", on_click=result_handler),
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                bar_cont,
                            ]
                        )
                    ]
                )
            )
        ]
    )

    page.add(settings_screen)


app(main)
