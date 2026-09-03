import builtins
import threading
import queue

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle


class TouchIO:
    def __init__(self):
        self.inputs = queue.Queue()
        self.output = queue.Queue()

    def input(self, prompt=""):
        if prompt:
            self.output.put(prompt)
        return self.inputs.get()

    def print(self, *args, **kwargs):
        self.output.put(" ".join(str(x) for x in args))


class Panel(BoxLayout):
    def __init__(self, bg=(0.07, 0.08, 0.12, 1), radius=16, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*bg)
            self._bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *_):
        self._bg.pos = self.pos
        self._bg.size = self.size


class DiceboundApp(App):

    def build(self):
        self.io = TouchIO()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        # Background
        with root.canvas.before:
            Color(0.035, 0.04, 0.06, 1)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(pos=self._update_root_bg, size=self._update_root_bg)

        # ─────────────────────────────
        # HEADER
        # ─────────────────────────────

        header = Panel(
            orientation="vertical",
            size_hint_y=None,
            height=dp(90),
            padding=[dp(16), dp(10)]
        )

        title = Label(
            text="⚔  THE DICEBOUND KINGDOM",
            font_size=dp(23),
            bold=True,
            color=(0.95, 0.85, 0.45, 1),
            halign="left",
            valign="middle"
        )

        subtitle = Label(
            text="ROLL • FIGHT • CHOOSE • SURVIVE",
            font_size=dp(11),
            color=(0.65, 0.68, 0.75, 1),
            halign="left"
        )

        header.add_widget(title)
        header.add_widget(subtitle)
        root.add_widget(header)

        # ─────────────────────────────
        # GAME LOG
        # ─────────────────────────────

        game_panel = Panel(
            orientation="vertical",
            padding=dp(12)
        )

        scroll = ScrollView(
            size_hint=(1, 1),
            bar_width=dp(5)
        )

        self.log = Label(
            text="🎲  Welcome to The Dicebound Kingdom!\n\nStarting game...",
            font_size=dp(16),
            color=(0.9, 0.9, 0.92, 1),
            halign="left",
            valign="top",
            size_hint_y=None,
            text_size=(None, None)
        )

        self.log.bind(texture_size=self._resize_log)

        scroll.add_widget(self.log)
        game_panel.add_widget(scroll)

        root.add_widget(game_panel)

        # ─────────────────────────────
        # INPUT
        # ─────────────────────────────

        input_row = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            spacing=dp(8)
        )

        self.entry = TextInput(
            hint_text="Type your answer...",
            multiline=False,
            font_size=dp(16),
            padding=[dp(14), dp(12)]
        )

        send = Button(
            text="SEND",
            size_hint_x=None,
            width=dp(90),
            font_size=dp(15)
        )

        send.bind(on_press=self.submit_text)

        input_row.add_widget(self.entry)
        input_row.add_widget(send)

        root.add_widget(input_row)

        # ─────────────────────────────
        # CHOICE BUTTONS
        # ─────────────────────────────

        choices = GridLayout(
            cols=4,
            spacing=dp(7),
            size_hint_y=None,
            height=dp(115)
        )

        for value in range(1, 9):
            button = Button(
                text=str(value),
                font_size=dp(19),
                background_normal="",
                background_color=(0.12, 0.14, 0.20, 1)
            )

            button.bind(
                on_press=lambda btn, v=value:
                self.submit_value(str(v))
            )

            choices.add_widget(button)

        root.add_widget(choices)

        # ─────────────────────────────
        # QUICK ACTIONS
        # ─────────────────────────────

        actions = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            spacing=dp(7)
        )

        action_data = [
            ("⚔ NEW", "1"),
            ("📂 LOAD", "2"),
            ("💾 SAVE", "6"),
            ("✕ QUIT", "8")
        ]

        for text, value in action_data:
            button = Button(
                text=text,
                font_size=dp(14),
                background_normal="",
                background_color=(0.16, 0.18, 0.25, 1)
            )

            button.bind(
                on_press=lambda btn, v=value:
                self.submit_value(v)
            )

            actions.add_widget(button)

        root.add_widget(actions)

        # Redirect terminal I/O
        builtins.input = self.io.input
        builtins.print = self.io.print

        threading.Thread(
            target=self.run_game,
            daemon=True
        ).start()

        Clock.schedule_interval(
            self.update_output,
            0.1
        )

        return root

    def _update_root_bg(self, instance, *_):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def _resize_log(self, instance, size):
        instance.text_size = (
            self.root.width - dp(50),
            None
        )

    def submit_text(self, *_):
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
            self.io.output.put(
                f"ERROR: {type(e).__name__}: {e}"
            )

    def update_output(self, dt):
        lines = []

        while True:
            try:
                lines.append(
                    self.io.output.get_nowait()
                )
            except queue.Empty:
                break

        if not lines:
            return

        current = self.log.text

        if current:
            self.log.text = (
                current +
                "\n" +
                "\n".join(lines)
            )
        else:
            self.log.text = "\n".join(lines)

        Clock.schedule_once(
            lambda _: self.scroll_to_bottom(),
            0
        )

    def scroll_to_bottom(self):
        scroll = self.log.parent

        if scroll is not None:
            try:
                scroll.parent.scroll_y = 0
            except Exception:
                pass


if __name__ == "__main__":
    DiceboundApp().run()
