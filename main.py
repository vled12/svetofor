
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.lang import Builder
from kivy.adapters.models import SelectableDataItem
from kivy.clock import Clock

Svetofors=['Primorsky 144','Blagodatnaya 21']

class SvetoforView(ScreenManager):
    def build(self):
        return self

    def svetofor_changed(self,list_adapter, *args):
        if len(list_adapter.selection) == 0:
            self.current = None
        else:
            selected_object = list_adapter.selection[0]
            self.current = 'screen_'+selected_object.text
        #self.redraw()

class SvetoforItem(SelectableDataItem):
    def __init__(self, name='', code=0, is_selected=False, **kwargs):
        super(SvetoforItem, self).__init__(is_selected=is_selected, **kwargs)
        self.name = name
        self.code = code
        self.is_selected = is_selected

svetofor_items = [SvetoforItem(name,i) for i,name in enumerate(sorted(Svetofors))]

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols =2
        svetoforview=SvetoforView()
        self.list_item_args_converter = lambda row_index, obj: {'text': obj.name,'size_hint_y': None,'height': 45}

        self.svetofor_list_adapter = ListAdapter(data=svetofor_items,
                                   args_converter=self.list_item_args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls=ListItemButton)

        self.svetofor_list_adapter.bind(on_selection_change=svetoforview.svetofor_changed)
        self.list_view = ListView(adapter=self.svetofor_list_adapter)

        self.add_widget(self.list_view)
        self.add_widget(svetoforview)
        #Clock.schedule_interval(self.update_list_data, 1)

    #def update_list_data(self,dt):
        #items=self.list_adapter.data
        #items.append({'text':'abs'})


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
