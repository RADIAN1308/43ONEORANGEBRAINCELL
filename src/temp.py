import flet as ft

def main(page: ft.Page):
    # Create a list of inner containers
    inner_containers = [
        ft.Container(
            content=ft.Text(f"Container {i}"),
            width=200,
            height=150,
            bgcolor=ft.colors.AMBER if i % 2 == 0 else ft.colors.BLUE,
            alignment=ft.alignment.center,
            border_radius=10,
            margin=10,
        )
        for i in range(10)  # Generate 10 containers
    ]

    # Create a parent container with scrolling
    scrollable_parent = ft.Container(
        content=ft.Column(
            controls=inner_containers,  # Add the list of child containers
            scroll="auto"               # Enable scrolling
        ),
        width=250,
        height=400,
        bgcolor=ft.colors.GREY_200,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )

    # Add the scrollable parent container to the page
    page.add(scrollable_parent)

ft.app(target=main)