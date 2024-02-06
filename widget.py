import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Yoshino'
    page.window_focused = True
    page.theme_mode = 'dark'
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT

    page.window_maximizable = False
    page.window_minimizable = False
    page.window_resizable = False

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = False
    page.window_frameless = True

    page.window_height = 200
    page.window_width = 200

    page.window_center()

    page.window_always_on_top = True
    # page.window_to_front()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    chest = ft.Stack(
        controls=[
            ft.Image(
                src="assets/yoshino_chibi_2.png"
            ),
            ft.Container(
                width=page.window_width,
                height=page.window_height,
                opacity=100

            )
        ]

    )

    drag_area = ft.WindowDragArea(
        content=chest,
        maximizable=False
    )

    page.add(
        drag_area
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets'
           )
