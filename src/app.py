from flet import *
import model as t

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.title = ""
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.update()

    bar_cont = Container()



    def result_handler(e):
        page.controls.clear()
        page.add(
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
        )
        page.update()

        bar_cont.content = None
        query = c_val.value.strip()
        results = t.search_funds(query, top_k=10)

        for result in results:
            print(f"Name: {result['name']}, Short Name: {result['shortName']}, Security Type: {result['securityType']}, Match Score: {result['match_score']}")

        lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        for company in results:
            c_comp = Container(
                content=Column(
                    controls=[
                        Text(f"Name: {company['name']}", weight=FontWeight.BOLD),
                        Text(f"Short Name: {company.get('shortName', 'N/A')}"),
                        Text(f"Type: {company.get('securityType', 'N/A')}"),
                        Text(f"Match Score: {company['match_score']:.2f}", color=Colors.GREEN),
                    ],
                    spacing=5,
                ),
                padding=10,
                border=border.all(1, Colors.GREY),
                border_radius=5,
            )
            lv.controls.append(c_comp)

        page.add(lv)

    def handle_change(e):
        if e.control.selected_index == 0:
            page.controls.clear()
            page.controls.append(home_screen)
        elif e.control.selected_index == 1:
            page.controls.clear()
            page.controls.append(search_screen)
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()


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
        ],
    )

    c_val = TextField(label="Enter company name", hint_text="Please enter text here", on_submit=result_handler)


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
            )
        ]
    )

    search_screen = Column(
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

    page.add(search_screen)


app(main)
