import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Main menu'
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

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=150,
        min_extended_width=300,
        leading=ft.FloatingActionButton(
            icon=ft.icons.ADD,
            text='Create'
        ),
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.EDIT_OUTLINED,
                selected_icon=ft.icons.EDIT,
                label='Edit'
            ),

            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label='Settings'
            ),

            ft.NavigationRailDestination(
                icon=ft.icons.INFO_OUTLINED,
                selected_icon=ft.icons.INFO,
                label='Info'
            )

        ]
    )



    main_container = Container(
        expand=True,
        content=Row(
            controls=[
                rail,
                ft.VerticalDivider(width=1),

            ]
        )

    )

    # ВАЖНО ПЕРЕДЕЛАТЬ ВСЁ, ЧТО РАНЬШЕ БЫЛО SETTINGS, В MAIN_MENU В settings.py & widget.py
    page.add(main_container)
    page.update()


if __name__ == '__main__':
    abc = ft.app(target=main,
                 assets_dir='assets'
                 )
