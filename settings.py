import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control
from subprocess import call
import os
import commands_management as cm
import json


def main(page: ft.Page) -> None:
    page.title = 'Main menu'
    page.theme_mode = 'dark'
    page.window_focused = True
    page.window_to_front()

    page.window_width = 1000
    page.window_height = 700

    page.window_center()
    page.window_maximizable = False
    page.window_resizable = False

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

    # AlertDialog
    def open_create_dialog(e):
        page.dialog = creating_dialog
        creating_dialog.open = True
        page.title = 'Create - Yoshino'
        print('create dialog opened')
        page.update()

    # AlertDialog
    def close_create_dialog(e):
        type_select.value = None
        command_type_child.content = temp_text
        alert_dialog_con.content = None
        creating_dialog.open = False
        page.title = ['Edit - Yoshino', 'Settings - Yoshino', 'Info - Yoshino'][rail.selected_index]
        page.update()

    def create_command(e):
        if type_select.value:
            print(f'type selected ({type_select.value})')
            if True:
                print('command created!')
            match type_select.value:
                case 'exec':
                    print('exec')
                    if selected_file.value is not None and command_name.value != '' and voice_request.value != '':
                        print('exec')
                        print(selected_file.value)
                        print(command_name.value)
                        print(voice_request.value)
                        cm.create_record(
                            type_select.value,
                            command_name.value,
                            selected_file.value,
                            voice_request.value
                        )
                        print('command created!\n' + '-' * 20)
                        selected_file.value = None
                        command_name.value = ''
                        voice_request.value = ''
                case 'openweb':
                    print('openweb')
                    if link_input.value != '' and command_name.value != '' and voice_request.value != '':
                        print('openweb')
                        print(link_input.value)
                        print(command_name.value)
                        print(voice_request.value)
                        cm.create_record(
                            type_select.value,
                            command_name.value,
                            'www.' + link_input.value,
                            voice_request.value
                        )
                        print('command created!\n' + '-' * 20)
                        link_input.value = ''
                        command_name.value = ''
                        voice_request.value = ''
                case 'websearch':
                    print('websearch')
                    if search_input.value != '' and command_name.value != '' and voice_request.value != '':
                        print('websearch')
                        print(search_input.value)
                        print(command_name.value)
                        print(voice_request.value)
                        cm.create_record(
                            type_select.value,
                            command_name.value,
                            search_input.value,
                            voice_request.value
                        )
                        print('command created!\n' + '-' * 20)
                        search_input.value = ''
                        command_name.value = ''
                        voice_request.value = ''
            show_commands()

        close_create_dialog(1)

    commands = Column(
        controls=[

        ],
        scroll=ft.ScrollMode.HIDDEN,
        expand=True,
        spacing=5,
        width=999999
    )

    def show_commands(e=None):
        with open('commands.json', 'r') as f:
            data = json.load(f)
            commands.controls.clear()
            for record in data:
                print('\n', data[record], '\n')

                command = Command(
                    data[record]["id"],
                    data[record]['command_type'],
                    data[record]['command_name'],
                    data[record]['command_string'],
                    data[record]['voice_request']
                )
                commands.controls.append(command)
            f.seek(0)
        page.update()
        print(20 * '-')

    def change_page(e):
        match e.control.selected_index:
            case 0:
                main_body.content = edit_page
                show_commands()
            case 1:
                main_body.content = settings_page
            case 2:
                main_body.content = info_page
        page.title = ['Edit - Yoshino', 'Settings - Yoshino', 'Info - Yoshino'][rail.selected_index]
        page.update()

    def pick_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file.value = e.files[0].path
            selected_file_label.value = e.files[0].name
            selected_file_label.update()

        else:
            selected_file.value = None
            selected_file_label.value = 'Файл не выбран'
            selected_file_label.update()
        # selected_file.update()
        print(selected_file)

    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)

    selected_file = ft.Text(value=None)
    link_input = TextField(
        label='Введите ссылку',
        prefix_text='www.',
        width=500
    )
    search_input = TextField(
        label='Введите поисковой запрос',
        suffix_text='YA.RU',
        width=500
    )
    selected_file_label = ft.Text(
        value='Файл не выбран',
        size=20,
    )
    command_name = TextField(
        label='Название команды',
        width=500
    )
    voice_request = TextField(
        label='Запрос голосом',
        multiline=True,
        max_lines=4,
        width=500
    )

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
                                    ),
                                    selected_file_label,
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    command_name
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    voice_request
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
                                    link_input
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    command_name
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    voice_request
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
                                    search_input
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    command_name
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            Row(
                                controls=[
                                    voice_request
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
                try_run_com = ft.OutlinedButton(
                    'Выполнить в cmd',
                    icon=ft.icons.CHEVRON_RIGHT,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=10
                        )
                    ),
                    scale=1.1,
                    on_click=lambda _: os.system(command_input.value)
                    if command_input.value else print("Command is empty:", command_input.value),
                )
                command_type_child.content = try_run_com

                alert_dialog_con.content = Container(
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    command_input := TextField(
                                        label='Введите команду',
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    )

                )

                page.update()

            case 'python':
                print(e.control.value)
                page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,
        height=600,
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
                    ),
                    mouse_cursor=ft.MouseCursor.CLICK,
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

    def star_click(e):
        if e.control.icon == ft.icons.STAR_OUTLINE_ROUNDED:
            e.control.icon = ft.icons.STAR_RATE_ROUNDED
            e.control.icon_color = ft.colors.YELLOW
        else:
            e.control.icon = ft.icons.STAR_OUTLINE_ROUNDED
            e.control.icon_color = ft.colors.WHITE38
        page.update()

    def open_edit_dialog(e):
        print(e.id, e.type, e.name, e.string, e.voice)
        temp_var_command.data = [e.id, e.type, e.name, e.string, e.voice]
        edit_com_name.value = e.name
        edit_com_string.value = e.string
        edit_com_voice.value = e.voice

        page.dialog = edit_dialog
        edit_dialog.open = True
        page.title = 'Edit - Yoshino'
        print('edit dialog opened')
        page.update()

    # id, type, name, string, voice
    temp_var_command = ft.Text(data=['', '', '', '', ''])

    def close_edit_dialog(e):
        temp_var_command.data = ['', '', '', '', '']

        edit_dialog.open = False
        page.title = ['Edit - Yoshino', 'Settings - Yoshino', 'Info - Yoshino'][rail.selected_index]
        show_commands()
        page.update()

    def update_command(e):
        page.update()
        print(temp_var_command.data)
        cm.update_record(
            temp_var_command.data[0],
            temp_var_command.data[1],
            edit_com_name.value,
            edit_com_string.value,
            edit_com_voice.value)
        print('Successful')
        close_edit_dialog(e)

    def refresh_edit_field(e, i):  # строки не обновляются
        match i:
            case 0:
                edit_com_name.value = temp_var_command.data[2]
            case 1:
                edit_com_string.value = temp_var_command.data[3]
            case 2:
                edit_com_voice.value = temp_var_command.data[4]
        page.update()
        print('well')

    edit_dialog = ft.AlertDialog(
        title=Row(
            controls=[
                ft.Text('Edit a command'),
                ft.IconButton(ft.icons.CLOSE, on_click=close_edit_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        content=Container(
            width=600,
            height=400,
            # border=ft.border.all(1, ft.colors.BLUE_900),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            edit_com_name := TextField(
                                label='Название команды',
                                width=500,
                                value='',
                            ),
                            ft.IconButton(
                                icon=ft.icons.REFRESH,
                                on_click=lambda e: refresh_edit_field(0, 0)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    Row(
                        controls=[
                            edit_com_string := TextField(
                                label='Команда',
                                width=500,
                                value='',
                            ),
                            ft.IconButton(
                                icon=ft.icons.REFRESH,
                                on_click=lambda e: refresh_edit_field(0, 1)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    Row(
                        controls=[
                            edit_com_voice := TextField(
                                label='Голос',
                                width=500,
                                value=''
                            ),
                            ft.IconButton(
                                icon=ft.icons.REFRESH,
                                on_click=lambda e: refresh_edit_field(0, 2)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            )
        ),
        content_padding=ft.padding.only(15, 0, 15, 0),
        inset_padding=15,
        actions_padding=15,
        title_padding=15,
        actions=[
            ft.TextButton('Save',
                          on_click=update_command
                          ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=10),
        on_dismiss=close_edit_dialog
    )

    class Command(ft.Card):
        def __init__(self, id, ctype, name, string, voice):
            super().__init__(
                width=100,
                height=70,
                show_border_on_foreground=True,
                is_semantic_container=True,
                expand=True
            )
            self.id = id
            self.type = ctype
            self.name = name
            self.string = string
            self.voice = voice

        def build(self):
            self.container = Container(
                expand=True,
                padding=ft.padding.only(10, 0, 10),
                content=Row(
                    controls=[
                        Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.STAR_OUTLINE_ROUNDED,
                                    icon_color=ft.colors.WHITE38,
                                    on_click=star_click,
                                    icon_size=30
                                ),
                                ft.Text(self.name)
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.START
                        ),
                        Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.PLAY_ARROW_ROUNDED,
                                    icon_color=ft.colors.GREEN_500,
                                    icon_size=25,
                                    on_click=self.run,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.EDIT_ROUNDED,
                                    icon_color=ft.colors.AMBER_600,
                                    icon_size=20,
                                    on_click=self.edit,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_ROUNDED,
                                    icon_color=ft.colors.RED_600,
                                    icon_size=20,
                                    on_click=self.delete,
                                )
                            ],
                            width=150,
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END
                        )

                    ],
                    spacing=10,
                    expand=True,
                )
            )
            super().__init__(
                content=self.container,
                height=70,

            )
            return self.container

        async def run(self, e):
            if self.string != '':
                match self.type:
                    case 'exec':
                        call(self.string)
                    case 'openweb':
                        print(self.string)
                        page.launch_url(self.string)
                    case 'websearch':
                        print(self.string)
                        page.launch_url('https://yandex.ru/search/?text=' + '+'.join(self.string.split(' ')))
                    case 'cmd':
                        print('Doesnt work')
                    case 'python':
                        print('Doesnt work')
            else:
                print('self.string is empty')

        async def edit(self, e):
            print('edit')
            open_edit_dialog(self)

        async def delete(self, e):
            cm.delete_record(self.id)
            show_commands()

    def search_commands(e):
        for com in commands.controls:
            if com.name.lower().find(com_search.value.lower()) != -1:
                com.visible = True
            else:
                com.visible = False
        page.update()

    def search_clear(e):
        com_search.value = ''
        search_commands(0)
        page.update()

    edit_page = Container(
        padding=ft.padding.only(0, 10, 10),
        expand=True,
        content=Column(
            controls=[
                Row(
                    controls=[
                        ft.Text('Тут будут фильтры'),
                        Container(
                            content=Row(
                                expand=True,
                                controls=[
                                    com_search := ft.TextField(
                                        expand=True,
                                        border=ft.InputBorder.NONE,
                                        filled=False,
                                        content_padding=ft.padding.symmetric(0, 10),
                                        hint_text='Поиск',
                                        on_change=search_commands
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.CLEAR_ROUNDED,
                                        on_click=search_clear
                                    )
                                ],
                                spacing=0
                            ),
                            width=500,
                            bgcolor='#282f36',
                            border_radius=50,
                            padding=5
                        ),
                        ft.IconButton(
                            icon=ft.icons.REFRESH_ROUNDED,
                            icon_color=ft.colors.WHITE,
                            icon_size=30,
                            on_click=show_commands
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                Container(
                    expand=True,
                    margin=ft.margin.only(10, 10, 10),
                    padding=ft.padding.only(10, 10, 10),
                    border=ft.border.only(
                        ft.BorderSide(1, ft.colors.WHITE12),
                        ft.BorderSide(1, ft.colors.WHITE12),
                        ft.BorderSide(1, ft.colors.WHITE12),
                    ),
                    content=commands
                )
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

    page.title = ['Edit - Yoshino', 'Settings - Yoshino', 'Info - Yoshino'][rail.selected_index]
    show_commands()

    # ВАЖНО ПЕРЕДЕЛАТЬ ВСЁ, ЧТО РАНЬШЕ БЫЛО SETTINGS, В MAIN_MENU В settings.py & widget.py
    page.add(main_container)
    page.update()


if __name__ == '__main__':
    abc = ft.app(target=main,
                 assets_dir='assets',
                 name='Yoshino',
                 )
