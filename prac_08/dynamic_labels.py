from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        names = ["Bob", "Jane", "Alex", "Alice"]
        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root

DynamicLabelsApp().run()
