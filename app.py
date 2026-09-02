from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DiceboundApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="THE DICEBOUND KINGDOM",
            font_size="28sp"
        )

        start = Button(
            text="⚔ NEW GAME",
            font_size="22sp",
            size_hint_y=None,
            height=80
        )

        continue_btn = Button(
            text="📂 CONTINUE",
            font_size="22sp",
            size_hint_y=None,
            height=80
        )

        layout.add_widget(title)
        layout.add_widget(start)
        layout.add_widget(continue_btn)

        return layout


if __name__ == "__main__":
    DiceboundApp().run()
