import flet as ft
from flet import Column, Row, Container, TextField, Checkbox
from flet_core.control import Control
import settings

#
# from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
# import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
# import wave  # создание и чтение аудиофайлов формата wav
# import json  # работа с json-файлами и json-строками
# import os  # работа с файловой системой
#
#
# def record_and_recognize_audio(*args: tuple):
#     """
#     Запись и распознавание аудио
#     """
#     with microphone:
#         recognized_data = ""
#
#         # регулирование уровня окружающего шума
#         recognizer.adjust_for_ambient_noise(microphone, duration=2)
#
#         try:
#             print("Listening...")
#             audio = recognizer.listen(microphone, 5, 5)
#
#             with open("microphone-results.wav", "wb") as file:
#                 file.write(audio.get_wav_data())
#
#         except speech_recognition.WaitTimeoutError:
#             print("Can you check if your microphone is on, please?")
#             return
#
#         # использование online-распознавания через Google
#         try:
#             print("Started recognition...")
#             recognized_data = recognizer.recognize_google_cloud(audio, language="ru").lower()
#
#         except speech_recognition.UnknownValueError:
#             pass
#
#         # в случае проблем с доступом в Интернет происходит попытка
#         # использовать offline-распознавание через Vosk
#         except speech_recognition.RequestError:
#             print("Trying to use offline recognition...")
#             recognized_data = use_offline_recognition()
#
#         return recognized_data
#
#
# def use_offline_recognition():
#     """
#     Переключение на оффлайн-распознавание речи
#     :return: распознанная фраза
#     """
#     recognized_data = ""
#     try:
#         # проверка наличия модели на нужном языке в каталоге приложения
#         if not os.path.exists("models/vosk-model-small-ru-0.22"):
#             print("Please download the model from:\n"
#                   "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
#             exit(1)
#
#         # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
#         wave_audio_file = wave.open("microphone-results.wav", "rb")
#         model = Model("models/vosk-model-small-ru-0.4")
#         offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
#
#         data = wave_audio_file.readframes(wave_audio_file.getnframes())
#         if len(data) > 0:
#             if offline_recognizer.AcceptWaveform(data):
#                 recognized_data = offline_recognizer.Result()
#
#                 # получение данных распознанного текста из JSON-строки
#                 # (чтобы можно было выдать по ней ответ)
#                 recognized_data = json.loads(recognized_data)
#                 recognized_data = recognized_data["text"]
#     except:
#         print("Sorry, speech service is unavailable. Try again later")
#
#     return recognized_data

# def execute_command_with_name(command_name: str, *args: list):
#     """
#     Выполнение заданной пользователем команды с дополнительными аргументами
#     :param command_name: название команды
#     :param args: аргументы, которые будут переданы в функцию
#     :return:
#     """
#     for key in commands.keys():
#         if command_name in key:
#             commands[key](*args)
#         else:
#             pass  # print("Command not found")


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
        # settings_button.data = True
        settings_button.update()
        # page.visible = False
        __import__('subprocess').call('python settings.py')
        print('test')
        # if not settings_app:
        #     settings_button.data = False
        #     settings_button.update()
        #     print(f'settings window closed')
        # else:
        #     print(True)

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
    # recognizer = speech_recognition.Recognizer()
    # microphone = speech_recognition.Microphone()
    #
    # while True:
    #     # старт записи речи с последующим выводом распознанной речи
    #     # и удалением записанного в микрофон аудио
    #     voice_input = record_and_recognize_audio()
    #     os.remove("microphone-results.wav")
    #     print(voice_input)
    #
    #     # отделение команд от дополнительной информации (аргументов)
    #     voice_input = voice_input.split(" ")
    #     command = voice_input[0]
    #     command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
    #     # execute_command_with_name(command, command_options)
