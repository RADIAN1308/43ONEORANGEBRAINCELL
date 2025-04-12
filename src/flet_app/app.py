from flet import *
import urllib.request
import json

global url

url = ""

def call_api(input_string):
    headers = {"Content-Type": "application/json"}
    payload = {"input_data": input_string}

    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            return json.loads(response_data)
    except urllib.error.HTTPError as e:
        return {"error": f"Failed with status code {e.code}"}
    except Exception as e:
        return {"error": str(e)}

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.title = "SLM FindMyFunds"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    page.update()

    global url
    bar_cont = Container()

    def update_url(e):
        global url
        url = e.control.value.strip()
        print(f"URL: {url}")

    def result_handler(e):
        bar_cont.content = None
        input_string = c_val.value.strip()
        if not url:
            bar_cont.content = Text("Please provide a valid URL.", color=Colors.RED)
            page.update()
            return

        results = call_api(input_string)
        results = list({frozenset(item.items()): item for item in results}.values())

        if "error" in results:
            bar_cont.content = Text(results["error"], color=Colors.RED)
            page.update()
            return

        lv.controls.clear()
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

        page.update()

    def toggle_theme(e):
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
        else:
            page.theme_mode = ThemeMode.LIGHT
        page.update()

    drawer = NavigationDrawer(
        controls=[
            NavigationDrawerDestination(
                label="Home",
                icon=Icons.HOME_ROUNDED,
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                icon=Icons.SEARCH_ROUNDED,
                label="Search",
            ),
        ],
    )

    c_val = TextField(label="Enter company name", hint_text="Please enter text here", on_submit=result_handler)
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    header = Row(
        alignment=MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            IconButton(Icons.MENU, on_click=lambda e: page.open(drawer)),
            Row(
                controls=[
                    IconButton(Icons.LIGHT_MODE_OUTLINED, on_click=toggle_theme),
                    IconButton(Icons.CONTACT_SUPPORT, on_click=lambda e: page.launch_url(
                        "https://ishitasampat.github.io/QX25-PS2-T43-Website/"))
                ]
            )
        ]
    )

    home_screen = Column(
        controls=[
            header,
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Image(src="app_icon.png", width=150, height=150, fit=ImageFit.CONTAIN),
                ]
            ),
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text("SLM FindMyFunds", size=24, text_align=TextAlign.CENTER),
                ]
            ),
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                TextField(label="Enter Ngrok IP", hint_text="Please enter IP here", on_change=update_url),
                ElevatedButton("Start your Search", icon=Icons.SEARCH_OUTLINED, on_click=lambda e: switch_to_search(),
                           bgcolor="#DC3535", color="#ffffff", icon_color="#ffffff"),
                ]
            )
        ]
    )

    search_screen = Column(
        controls=[
            header,
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    c_val,
                    ElevatedButton(text="Submit", on_click=result_handler),
                ]
            ),
            bar_cont,
            lv,
        ]
    )

    def switch_to_search():
        page.controls.clear()
        page.add(search_screen)
        page.update()

    page.add(home_screen)

app(main)