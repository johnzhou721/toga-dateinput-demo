import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from datetime import date


class DateInputApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, gap=10))

        self.date_input = toga.DateInput(style=Pack(padding=5))
        self.date_input.on_change = self.on_date_change

        self.status_label = toga.Label("Selected Date: None", style=Pack(padding=5))

        self.date_text_input = toga.TextInput(placeholder="YYYY-MM-DD", style=Pack(padding=5))

        set_button = toga.Button("Set Date", on_press=self.set_date, style=Pack(padding=5))
        get_button = toga.Button("Get Date", on_press=self.get_date, style=Pack(padding=5))
        enable_button = toga.Button("Enable", on_press=self.enable_dateinput, style=Pack(padding=5))
        disable_button = toga.Button("Disable", on_press=self.disable_dateinput, style=Pack(padding=5))

        set_min_button = toga.Button("Set Min Date", on_press=self.set_min_date, style=Pack(padding=5))
        get_min_button = toga.Button("Get Min Date", on_press=self.get_min_date, style=Pack(padding=5))
        set_max_button = toga.Button("Set Max Date", on_press=self.set_max_date, style=Pack(padding=5))
        get_max_button = toga.Button("Get Max Date", on_press=self.get_max_date, style=Pack(padding=5))

        main_box.add(self.date_input)
        main_box.add(self.status_label)
        main_box.add(toga.Label("Enter a date (YYYY-MM-DD):", style=Pack(padding=5)))
        main_box.add(self.date_text_input)

        button_box1 = toga.Box(style=Pack(direction=ROW, gap=5))
        button_box1.add(set_button)
        button_box1.add(get_button)
        button_box1.add(enable_button)
        button_box1.add(disable_button)

        button_box2 = toga.Box(style=Pack(direction=ROW, gap=5))
        button_box2.add(set_min_button)
        button_box2.add(get_min_button)

        button_box3 = toga.Box(style=Pack(direction=ROW, gap=5))
        button_box3.add(set_max_button)
        button_box3.add(get_max_button)

        main_box.add(button_box1)
        main_box.add(button_box2)
        main_box.add(button_box3)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_date_change(self, widget):
        self.status_label.text = f"Selected Date: {widget.value}"

    def set_date(self, widget):
        self._set_date_input_value('value', "Date set to")

    def get_date(self, widget):
        selected_date = self.date_input.value
        self.status_label.text = f"Current date: {selected_date}"
        self.date_text_input.value = str(selected_date)

    def enable_dateinput(self, widget):
        self.date_input.enabled = True
        self.status_label.text = "DateInput enabled."

    def disable_dateinput(self, widget):
        self.date_input.enabled = False
        self.status_label.text = "DateInput disabled."

    def set_min_date(self, widget):
        self._set_date_input_value('min', "Minimum date set to")

    def get_min_date(self, widget):
        min_date = self.date_input.min
        self.status_label.text = f"Minimum date: {min_date}"
        self.date_text_input.value = str(min_date)

    def set_max_date(self, widget):
        self._set_date_input_value('max', "Maximum date set to")

    def get_max_date(self, widget):
        max_date = self.date_input.max
        self.status_label.text = f"Maximum date: {max_date}"
        self.date_text_input.value = str(max_date)

    def _set_date_input_value(self, attr, message_prefix):
        setattr(self.date_input, attr, self.date_text_input.value)


def main():
    return DateInputApp("DateInput Tester", "org.beeware.dateinputtester")
