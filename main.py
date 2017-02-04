import kivy
kivy.require('1.1.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from svetofor import Svetofor

from kivy.clock import Clock

class Light(GridLayout):
    label = StringProperty('')
    time_left = StringProperty('')
    color=ListProperty()
    def __init__(self, address, **kwargs):
        super(Light,self).__init__(**kwargs)
        self.label=address
        self.light=Svetofor()
        self.color=([0,0,0,1])
        Clock.schedule_interval(self.update, 0.1)

    def update(self,dt):
        self.light.check()
        self.time_left='{:{width}.{prec}f}'.format(self.light.time_left, width=2, prec=1)
        self.color[0]=0.0 if self.light.status else 1.0
        self.color[1] = 1.0 if self.light.status else 0.0


class StartScreen(Widget):
    def __init__(self, **kwargs):
        self.lightsView = ObjectProperty(None)
        self.entered_address=ObjectProperty()
        super(StartScreen, self).__init__(**kwargs)
    def add_svetofor(self):
        self.lightsView.add_widget(Light(self.entered_address.text))

class LightsApp(App):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    LightsApp().run()
