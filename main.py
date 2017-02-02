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
        #svetoforview = SvetoforView()
        #self.list_item_args_converter = lambda row_index, obj: {'text': obj.name, 'size_hint_y': None, 'height': 45}


        #self.svetofor_list_adapter.bind(on_selection_change=svetoforview.svetofor_changed)
        #self.list_view = ListView(adapter=self.svetofor_list_adapter)

        #self.add_widget(self.list_view)
        #self.add_widget(svetoforview)

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
