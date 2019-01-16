from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class simpleStringApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.words = ['damn', 'daniel', 'at', 'it', 'again', 'with', 'the', 'white', 'vans']

    def build(self):
        self.title = "Dynamic String"
        self.root = Builder.load_file('simpleStrings.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for word in self.words:
            temp_label = Label(text=word)
            temp_label.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_label)

    def press_entry(self, instance):
        self.status_text = "{}".format(instance.text)

    def add_widget(self):
        temp_label = Label(text="new one")
        temp_label.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()


simpleStringApp().run()
