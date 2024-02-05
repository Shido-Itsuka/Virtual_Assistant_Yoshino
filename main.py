import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Yoshino'


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets'
           )
