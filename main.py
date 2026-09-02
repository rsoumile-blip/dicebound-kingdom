import builtins
import threading
import queue

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp


class TouchIO:
    def __init__(self):
        self.inputs = queue.Queue()
        self.output = queue.Queue()

    def input(self, prompt=""):
        if prompt:
            self.output.put(prompt)
        return self.inputs.get()

    def print(self, *args, **kwargs):
        text = " ".join(str(x) for x in args)
        self.output.put(text)


class DiceboundApp(App):
    def build(self):
        self.io = TouchIO()

        self.root_layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )

        title = Label(
            text="⚔ THE DICEBOUND KINGDOM ⚔",
            font_size=dp(24),
            size_hint_y=None,
            height=dp(55)
        )
        self.root_layout.add_widget(title)

        scroll = ScrollView(size_hint_y=1)
        self.log = Label(
            text="Starting...",
            size_hint_y=None,
            text_size=(None, None),
            halign="left",
            valign="top"
        )
        self.log.bind(texture_size=self._resize_log)
        scroll.add_widget(self.log)
        self.root_layout.add_widget(scroll)

        self.entry = TextInput(
            hint_text="Type your answer...",
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )
        self.root_layout.add_widget(self.entry)

        send = Button(
            text="ENTER",
            size_hint_y=None,
            height=dp(55)
        )
        send.bind(on_press=self.submit_text)
        self.root_layout.add_widget(send)

        buttons = GridLayout(
            cols=4,
            spacing=dp(5),
            size_hint_y=None,
            height=dp(65)
        )

        for value in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            btn = Button(text=value, font_size=dp(20))
            btn.bind(on_press=lambda b, v=value: self.submit_value(v))
            buttons.add_widget(btn)

        self.root_layout.add_widget(buttons)

        quick = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(5)
        )

        for text, value in [
            ("NEW", "1"),
            ("LOAD", "2"),
            ("SAVE", "6"),
            ("QUIT", "8")
        ]:
            btn = Button(text=text)
            btn.bind(on_press=lambda b, v=value: self.submit_value(v))
            quick.add_widget(btn)

        self.root_layout.add_widget(quick)

        builtins.input = self.io.input
        builtins.print = self.io.print

        threading.Thread(
            target=self.run_game,
            daemon=True
        ).start()

        Clock.schedule_interval(self.update_output, 0.1)

        return self.root_layout

    def _resize_log(self, instance, size):
        instance.text_size = (self.root_layout.width - dp(20), None)

    def submit_text(self, instance):
        value = self.entry.text.strip()

        if value:
            self.entry.text = ""
            self.io.inputs.put(value)

    def submit_value(self, value):
        self.io.inputs.put(value)

    def run_game(self):
        try:
            from game_cli import main as game_main
            game_main()
        except Exception as e:
            self.io.output.put("")
            self.io.output.put(f"ERROR: {type(e).__name__}: {e}")

    def update_output(self, dt):
        changed = False
        lines = []

        while True:
            try:
                lines.append(self.io.output.get_nowait())
                changed = True
            except queue.Empty:
                break

        if changed:
            current = self.log.text
            new_text = current + ("\n" if current else "") + "\n".join(lines)

            self.log.text = new_text
            Clock.schedule_once(
                lambda _: self.scroll_to_bottom(),
                0
            )

    def scroll_to_bottom(self):
        parent = self.log.parent
        if parent:
            try:
                parent.parent.scroll_y = 0
            except Exception:
                pass


if __name__ == "__main__":
    DiceboundApp().run()
