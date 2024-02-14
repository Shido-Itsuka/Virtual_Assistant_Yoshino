import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Settings'
    page.theme_mode = 'dark'
    page.window_focused = True
    page.window_to_front()

    page.window_width = 900
    page.window_height = 600

    page.window_center()

    page.theme = ft.Theme(
        color_scheme_seed='#5a84ff'
    )

    def window_event(e):
        if e.data == 'close':
            page.window_destroy()

    # должен выводиться AlertDialog при выявленных несохраненных изменениях

    page.window_prevent_close = True
    page.on_window_event = window_event

    page.padding = 0

    # page.window_bgcolor = ft.colors.TRANSPARENT
    # page.bgcolor = ft.colors.TRANSPARENT

    main_container = Container(
        expand=True,
        content=Row(

        )

    )

    page.add(main_container)
    page.update()


if __name__ == '__main__':
    abc = ft.app(target=main,
                 assets_dir='assets'
                 )
