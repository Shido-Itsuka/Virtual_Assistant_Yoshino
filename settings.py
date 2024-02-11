import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Settings'
    page.window_focused = True
    page.theme_mode = 'dark'

    page.window_width = 900
    page.window_height = 600

    page.window_center()

    page.theme = ft.Theme(
        color_scheme_seed='#5a84ff'
    )


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets'
           )
