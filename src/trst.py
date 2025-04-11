from flet import *
import time
from flet.core.icons import Icons


def main(page: Page):
    page.title = "Flet Example"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    # Ensure the bar container is properly initialized
    bar_cont = Container()

    def result_handler(e):
        r_val = 0

        # Safely assign ProgressBar to the bar container
        bar_cont.content = ProgressBar(width=400, color="amber", bgcolor="#eeeeee", value=None)
        page.update()

        while r_val < 1:
            time.sleep(0.2)
            r_val += 0.1
            print(r_val)

        # Clear the ProgressBar after completion
        bar_cont.content = None
        page.update()

        # Create and display a ListView with sample items
        lv = ListView(expand=0, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(Text("Process complete!"))
        page.add(lv)

    def handle_change(e):
        # Safely manage screen switching
        page.controls.clear()
        if e.control.selected_index == 0:
            page.add(home_screen)
        elif e.control.selected_index == 1:
            page.add(settings_screen)
        elif e.control.selected_index == 2:
            print("Option 3 is to be implemented")
        page.update()

    def toggle_theme(e):
        # Toggle between Dark and Light Themes
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()

    def placeholder(e):
        print("Placeholder clicked")

    # Navigation Drawer
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
                icon=Icon(Icons.BOOK),
                label="Settings",
                selected_icon=Icons.BOOK,
            ),
            NavigationDrawerDestination(
                icon=Icon(Icons.CALENDAR_MONTH_ROUNDED),
                label="More",
                selected_icon=Icons.CALENDAR_MONTH_ROUNDED,
            ),
        ],
    )

    # Input Field for Company Name
    c_val = TextField(label="Enter company name", hint_text="Please enter text here")

    # Home Screen Layout
    home_screen = Column(
        [
            Container(
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                IconButton(Icons.MENU, on_click=lambda e: page.open(drawer)),
                                Row(
                                    controls=[
                                        IconButton(Icons.LIGHT_MODE_OUTLINED, on_click=toggle_theme),
                                        IconButton(Icons.CONTACT_SUPPORT, on_click=placeholder),
                                    ]
                                ),
                            ]
                        ),
                    ]
                )
            ),
        ]
    )

    # Settings Screen Layout
    settings_screen = Column(
        [
            Container(
                content=Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                IconButton(Icons.MENU, on_click=lambda e: page.open(drawer)),
                                Row(
                                    controls=[
                                        IconButton(Icons.LIGHT_MODE_OUTLINED, on_click=toggle_theme),
                                        IconButton(Icons.CONTACT_SUPPORT, on_click=placeholder),
                                    ],
                                ),
                            ],
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                c_val,
                                ElevatedButton(text="Submit", on_click=result_handler),
                            ],
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                bar_cont,  # Add bar container safely
                            ],
                        ),
                    ],
                ),
            ),
        ]
    )

    # Initialize page with the settings screen as default
    page.add(settings_screen)


app(main)
