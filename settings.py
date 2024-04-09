import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control
from subprocess import call


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

    def change_page(e):
        match e.control.selected_index:
            case 0:
                main_body.content = edit_page
            case 1:
                main_body.content = settings_page
            case 2:
                main_body.content = info_page
        page.update()

    # AlertDialog
    def open_create_dialog(e):
        page.dialog = creating_dialog
        creating_dialog.open = True
        print('create dialog opened')
        page.update()

    # AlertDialog
    def close_create_dialog(e):
        type_select.value = None
        command_type_child.content = temp_text
        alert_dialog_con.content = None
        creating_dialog.open = False
        page.update()

    def create_command(e):
        if type_select.value:
            print(f'type selected ({type_select.value})')
            if True:
                print('command created!')
        close_create_dialog(1)

    def pick_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file.value = e.files[0].path

        else:
            selected_file.value = None
        # selected_file.update()
        print(selected_file)

    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    selected_file = ft.Text(value=None, )
    page.overlay.append(pick_file_dialog)

    def on_change_type_select(e):
        match e.control.value:
            case 'exec':
                print(e.control.value)
                try_exec_file = ft.OutlinedButton(
                    'Запустить .exe файл',
                    icon=ft.icons.CHEVRON_RIGHT,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=10
                        )
                    ),
                    scale=1.1,
                    on_click=lambda _: call(
                        str(selected_file.value)
                    ) if selected_file.value else print("Path isn't correct:", selected_file.value),
                )
                command_type_child.content = try_exec_file
                alert_dialog_con.content = Container(
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    pick_exe := ft.OutlinedButton(
                                        "Выбрать .exe файл",
                                        icon=ft.icons.UPLOAD_FILE,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=10
                                            )
                                        ),
                                        scale=1.1,
                                        on_click=lambda _: pick_file_dialog.pick_files(
                                            dialog_title='Выбор .exe файла',
                                            allow_multiple=False,
                                            file_type=ft.FilePickerFileType.CUSTOM,
                                            allowed_extensions=["exe"],
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    )
                )
                page.update()

            case 'openweb':
                print(e.control.value)
                try_open_link = ft.OutlinedButton(
                    'Открыть сайт в браузере',
                    icon=ft.icons.LINK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=10
                        )
                    ),
                    scale=1.1,
                    on_click=lambda _: page.launch_url(
                        url='www.' + link_input.value,
                    ) if link_input.value else print("Link is empty:", link_input.value),
                )
                command_type_child.content = try_open_link

                alert_dialog_con.content = Container(
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    link_input := TextField(
                                        label='Введите ссылку',
                                        prefix_text='www.',
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    )

                )

                page.update()

            case 'websearch':
                print(e.control.value)
                try_search = ft.OutlinedButton(
                    'Открыть поисковой запрос',
                    icon=ft.icons.SEARCH,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=10
                        )
                    ),
                    scale=1.1,
                    on_click=lambda _: page.launch_url(
                        url='https://yandex.ru/search/?text=' + '+'.join(search_input.value.split(' ')),
                    ) if search_input.value else print("Link is empty:", search_input.value),
                )
                command_type_child.content = try_search

                alert_dialog_con.content = Container(
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    search_input := TextField(
                                        label='Введите поисковой запрос',
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    )

                )

                page.update()

            case 'cmd':
                print(e.control.value)

            case 'python':
                print(e.control.value)

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,
        height=500,
        width=130,
        min_width=130,
        min_extended_width=200,
        bgcolor=ft.colors.TRANSPARENT,
        on_change=change_page,
        leading=Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.alignment.center,
            controls=[
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    text='Create',
                    on_click=open_create_dialog,
                    shape=ft.RoundedRectangleBorder(
                        radius=10
                    )
                ),

            ]
        ),
        group_alignment=-0.8,
        indicator_color=ft.colors.TRANSPARENT,
        indicator_shape=ft.RoundedRectangleBorder(
            radius=10,
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.EDIT_OUTLINED,
                    color=ft.colors.WHITE38,
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.EDIT,
                    color=ft.colors.WHITE
                ),
                label='Edit',
                padding=40,

            ),

            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.SETTINGS_OUTLINED,
                    color=ft.colors.WHITE38
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.SETTINGS,
                    color=ft.colors.WHITE
                ),
                label='Settings',
                padding=40
            ),

            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.INFO_OUTLINED,
                    color=ft.colors.WHITE38
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.INFO,
                    color=ft.colors.WHITE
                ),
                label='Info',
                padding=40
            )

        ],
    )

    temp_text = ft.Text(
        'Выберите тип команды',
        size=16
    )

    creating_dialog = ft.AlertDialog(
        title=Row(
            controls=[
                ft.Text('Create a new command!'),
                ft.IconButton(ft.icons.CLOSE, on_click=close_create_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        modal=True,
        content=Container(
            width=600,
            # border=ft.border.all(1, ft.colors.BLUE_900),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            type_select := ft.Dropdown(
                                label='Типы команд',
                                hint_text='Выберите тип команды',
                                options=[
                                    ft.dropdown.Option(key='exec', text='Запустить программу'),
                                    ft.dropdown.Option(key='openweb', text='Открыть сайт'),
                                    ft.dropdown.Option(key='websearch', text='Найти в браузере'),
                                    ft.dropdown.Option(key='cmd', text='Выполнить команду в терминале'),
                                    ft.dropdown.Option(key='python', text='Выполнить код на Python'),
                                ],
                                width=300,
                                border_radius=ft.border_radius.all(5),
                                on_change=on_change_type_select
                            ),
                            command_type_child := Container(
                                content=temp_text,
                                alignment=ft.alignment.center,
                                expand=True,
                                # margin=ft.margin.only(right=10),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN

                    ),
                    alert_dialog_con := Container(
                        expand=True,
                    )
                ]
            )
        ),
        content_padding=ft.padding.only(15, 0, 15, 0),
        inset_padding=15,
        actions_padding=15,
        title_padding=15,
        actions=[
            ft.TextButton('Create',
                          on_click=create_command
                          ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=10),

    )

    edit_page = Container(
        expand=True,
        content=Column(
            controls=[
                ft.Text('Edit page')
            ]
        )
    )

    settings_page = Container(
        expand=True,
        content=Column(
            controls=[
                ft.Text('Settings page')
            ]
        )
    )

    info_page = Container(
        expand=True,
        content=Column(
            controls=[
                ft.Text('Info page')
            ]
        )
    )

    main_body = Container(
        expand=True,
        padding=0,
        content=edit_page
    )

    rail_container = Container(
        width=130,
        height=page.window_height,
        padding=0,
        bgcolor=ft.colors.BLACK12,
        blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR),
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
                ),
                main_body
            ]
        ),
        blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR)

    )

    # ВАЖНО ПЕРЕДЕЛАТЬ ВСЁ, ЧТО РАНЬШЕ БЫЛО SETTINGS, В MAIN_MENU В settings.py & widget.py
    page.add(main_container)
    page.update()


if __name__ == '__main__':
    abc = ft.app(target=main,
                 assets_dir='assets'
                 )
