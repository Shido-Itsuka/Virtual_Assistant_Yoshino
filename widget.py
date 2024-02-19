import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control
import settings


def main(page: ft.Page) -> None:
    page.title = 'Yoshino'
    page.window_focused = True
    page.theme_mode = 'dark'

    page.window_minimizable = False
    page.window_maximizable = False
    page.window_resizable = False
    page.padding = 0

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = False
    page.window_frameless = True

    page.window_height = 230
    page.window_width = 200
    page.window_bgcolor = ft.colors.TRANSPARENT  # YELLOW_300
    page.bgcolor = ft.colors.TRANSPARENT

    page.window_center()

    page.window_always_on_top = True
    # page.window_to_front()

    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    pic_height = 182

    container_for_test = Container(
        width=page.window_width,
        height=pic_height,
        opacity=100,
        bgcolor=ft.colors.BLUE_300,
        alignment=ft.alignment.center,
    )

    nya_sound = ft.Audio(
        src='assets/nya.mp3',
        volume=0.7
    )
    page.overlay.append(nya_sound)

    def on_click_yoshino(e):
        nya_sound.play()

    chest = ft.Stack(
        controls=[
            # container_for_test,

            ft.Image(
                src="assets/yoshino_chibi_2_fixed.png",
            ),

            Container(
                width=page.window_width,
                height=pic_height,
                opacity=0,
                alignment=ft.alignment.center,
                on_click=on_click_yoshino

            )
        ]

    )

    drag_area = ft.WindowDragArea(
        content=chest,
        maximizable=False,
        width=page.window_width,
        height=pic_height,
    )

    def on_click_menu_button(e):
        e.control.selected = not e.control.selected
        if e.control.selected:
            e.control.tooltip = 'Unmute'
        else:
            e.control.tooltip = 'Mute'
        e.control.update()

    def on_click_pin_button(e):
        e.control.selected = not e.control.selected
        if e.control.selected:
            page.window_always_on_top = True
            page.window_minimizable = False
            page.window_maximizable = False
            e.control.tooltip = 'Unpin'
        else:
            page.window_always_on_top = False
            page.window_minimizable = True
            page.window_maximizable = True
            e.control.tooltip = 'Pin'
        e.control.update()
        page.update()

    def create_settings_window():
        settings_button.data = True
        settings_button.update()
        settings_app = ft.app(target=settings.main,
                              assets_dir='assets'
                              )
        if not settings_app:
            settings_button.data = False
            settings_button.update()
            print(f'settings window closed')
        else:
            print(True)

    def on_click_settings(e):
        print('settings button clicked!')
        print('-' * 15)
        if e.control.data == 0:
            e.data = True
            e.control.update()
            print(f'settings button data {e.data}')
            create_settings_window()
        else:
            print('Window already created')

    def window_event(e):
        if e.data == 'close':
            if settings_button.data:
                pass
            else:
                page.window_destroy()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def full_on_hover(e):
        menu.opacity = 100 if e.data == 'true' else 0
        menu.update()

    menu = Container(
        width=page.window_width,
        height=45,
        opacity=100,
        bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),
        border_radius=ft.border_radius.all(5),
        alignment=ft.alignment.center,

        content=ft.Row(
            [
                # Mute/unmute mic
                ft.IconButton(
                    icon=ft.icons.MIC_SHARP,
                    icon_color=ft.colors.WHITE,
                    selected_icon=ft.icons.MIC_OFF_SHARP,
                    selected_icon_color=ft.colors.RED_600,
                    selected=False,
                    tooltip='Mute',
                    on_click=on_click_menu_button
                ),
                # Main menu
                settings_button := ft.IconButton(
                    icon=ft.icons.DENSITY_MEDIUM,
                    icon_color=ft.colors.WHITE,
                    tooltip='Main menu',
                    on_click=on_click_settings,
                    data=False

                ),
                # Pin/unpin window
                pin_button := ft.IconButton(
                    icon=ft.icons.PUSH_PIN_OUTLINED,
                    icon_color=ft.colors.WHITE,
                    selected_icon=ft.icons.PUSH_PIN,
                    selected=True,
                    tooltip='Unpin',
                    on_click=on_click_pin_button
                ),
                # Close
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color=ft.colors.WHITE,
                    tooltip='Close',
                    on_click=lambda e: page.window_close()

                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )

    full = Container(
        ft.Column(
            [
                drag_area,
                menu
            ],
            spacing=3

        ),
        on_hover=full_on_hover

    )

    page.add(
        full
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets'
           )
