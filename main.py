import kivy
kivy.require('1.1.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

from kivy.clock import Clock

class Light(Widget):
    pass
class StartScreen(Widget):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.lights = []

        # Clock.schedule_interval(self.update_list_data, 1)

    def add_svetofor(self):
        #self.lights.append(Light())
        self.ids.lightsView.add_widget(Light())
        #self.ids['svetofor_list'].adapter.data.append('lol')
        # def update_list_data(self,dt):
        # items=self.list_adapter.data
        # items.append({'text':'abs'})


class LightsApp(App):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    LightsApp().run()
