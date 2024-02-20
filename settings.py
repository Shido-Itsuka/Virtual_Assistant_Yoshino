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
        label_type=ft.NavigationRailLabelType.SELECTED,
        height=500,
        width=130,
        min_width=130,
        min_extended_width=150,
        bgcolor=ft.colors.TRANSPARENT,
        leading=Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.alignment.center,
            controls=[
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    text='Create',
                ),

            ]
        ),
        group_alignment=-0.9,
        indicator_shape=ft.RoundedRectangleBorder(
            radius=10,

        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.EDIT_OUTLINED,
                selected_icon=ft.icons.EDIT,
                label='Edit',
                padding=40,

            ),

            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label='Settings',
                padding=40
            ),

            ft.NavigationRailDestination(
                icon=ft.icons.INFO_OUTLINED,
                selected_icon=ft.icons.INFO,
                label='Info',
                padding=40
            )

        ]
    )

    rail_container = Container(
        width=130,
        height=page.window_height,
        padding=0,
        bgcolor=ft.colors.BLACK12,
        content=Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                rail,
                Container(
                    content=Row(
                        controls=[
                            ft.Icon(
                                name=ft.icons.PERSON
                            ),
                            ft.Text('Nickname'),
                        ],

                    ),
                    bgcolor=ft.colors.BLACK26,
                    height=60,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(left=10)
                )
            ]
        )
    )

    main_container = Container(
        expand=True,
        content=Row(
            controls=[
                Row(
                    controls=[
                        rail_container,
                        ft.VerticalDivider(width=0)
                    ],
                    spacing=0
                )
                ,

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
