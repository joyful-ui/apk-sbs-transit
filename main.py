import kivy as kv
kv.require("2.3.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window


# ================= Window =================

Window.size = (400, 750)
Window.clearcolor = (1, 1, 1, 1)


# ================= Click Anywhere =================

class ClickableScreen(FloatLayout):

    def on_touch_down(self, touch):
        App.get_running_app().start_voice()
        return super().on_touch_down(touch)


# ================= Main App =================

class SBSApp(App):

    def build(self):

        self.title = "SBS Transit Assistant"

        layout = ClickableScreen()

        # ================= SBS Logo =================

        logo = Image(
            source="sbs_logo.png",
            size_hint=(0.95, None),
            height=170,
            allow_stretch=True,
            keep_ratio=True,
            pos_hint={
                "center_x":0.5,
                "top":0.98
            }
        )

        layout.add_widget(logo)

        # ================= HUGE Microphone =================

        self.mic = Image(
            source="microphone.png",
            size_hint=(None,None),
            size=(700,700),          # Huge microphone
            allow_stretch=True,
            keep_ratio=True,
            pos_hint={
                "center_x":0.5,
                "center_y":0.34
            }
        )

        layout.add_widget(self.mic)

        return layout


    # ================= Voice =================

    def start_voice(self):

        # Turn microphone blue
        self.mic.source = "blue_microphone.png"

        # Pop animation
        self.mic.size = (740,740)

        print("Voice recognition started")

        # ===========================================
        # Put teammate's voice recognition code here
        # ===========================================

        Clock.schedule_once(self.reset_mic,0.5)


    def reset_mic(self,dt):

        # Back to purple
        self.mic.source = "microphone.png"

        self.mic.size = (700,700)


# ================= Run =================

if __name__ == "__main__":
    SBSApp().run()
