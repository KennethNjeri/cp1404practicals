from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ""
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_label.text)
            kilometres = miles * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

    def handle_increment(self, increment):
        try:
            miles = float(self.root.ids.input_label.text) + increment
            self.root.ids.input_label.text = str(miles)
            self.handle_convert()
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_update(self, delta):
        self.message = self.root.ids.output_label.text

MilesConverterApp().run()
