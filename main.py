import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class IntermittentFastingApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = None
        self.end_time = None

    def build(self):
        layout = GridLayout(cols=2)
        label = Label(text="Start Time")
        button = Button(text="Start")
        layout.add_widget(label)
        layout.add_widget(button)

        def start_fasting():
            self.start_time = kivy.Clock.get_time()
            button.text = "Stop"

        button.bind(on_press=start_fasting)

        return layout

    def on_stop(self):
        if self.start_time is not None:
            end_time = kivy.Clock.get_time()
            hours = (end_time - self.start_time) / 3600
            print(f"You fasted for {hours} hours.")


if __name__ == "__main__":
    IntermittentFastingApp().run()
