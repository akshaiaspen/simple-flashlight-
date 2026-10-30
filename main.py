from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

from plyer import flash


class FlashlightApp(App):

    def build(self):
        self.is_on = False

        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=30
        )

        self.status = Label(
            text="FLASHLIGHT OFF",
            font_size="28sp"
        )

        self.button = Button(
            text="TURN ON",
            font_size="25sp",
            size_hint=(1, 0.35)
        )

        self.button.bind(on_press=self.toggle_flash)

        layout.add_widget(self.status)
        layout.add_widget(self.button)

        return layout

    def toggle_flash(self, instance):
        try:
            if not self.is_on:
                flash.on()
                self.is_on = True
                self.status.text = "FLASHLIGHT ON"
                self.button.text = "TURN OFF"
            else:
                flash.off()
                self.is_on = False
                self.status.text = "FLASHLIGHT OFF"
                self.button.text = "TURN ON"

        except Exception as e:
            self.status.text = "Flashlight unavailable"
            print(e)

    def on_stop(self):
        try:
            flash.off()
        except Exception:
            pass


if __name__ == "__main__":
    FlashlightApp().run()