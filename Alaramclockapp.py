# Import necessary modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.timepicker import TimePicker

class Alarm:
    def __init__(self, time, tone):
        self.time = time
        self.tone = tone
        self.is_enabled = True

class AlarmApp(App):
    def __init__(self, **kwargs):
        super(AlarmApp, self).__init__(**kwargs)
        self.alarms = []  # List to store Alarm objects

    def build(self):
        # Home Screen
        home_screen = BoxLayout(orientation='vertical')
        self.current_time_label = Label(text="Current Time: 00:00")
        home_screen.add_widget(self.current_time_label)

        # Set New Alarm Button
        set_alarm_button = Button(text="Set New Alarm", on_press=self.show_alarm_setting)
        home_screen.add_widget(set_alarm_button)

        return home_screen

    def show_alarm_setting(self, instance):
        # Alarm Setting Popup
        alarm_setting_popup = Popup(title="Set Alarm", size_hint=(None, None), size=(400, 300))
        alarm_setting_layout = BoxLayout(orientation='vertical')

        time_picker = TimePicker()
        alarm_setting_layout.add_widget(time_picker)

        tone_label = Label(text="Choose Alarm Tone:")
        alarm_setting_layout.add_widget(tone_label)

        # Add logic to choose alarm tone

        save_button = Button(text="Save", on_press=lambda x: self.save_alarm(time_picker.time, "DefaultTone"))
        alarm_setting_layout.add_widget(save_button)

        alarm_setting_popup.add_widget(alarm_setting_layout)
        alarm_setting_popup.open()

    def save_alarm(self, alarm_time, alarm_tone):
        new_alarm = Alarm(alarm_time, alarm_tone)
        self.alarms.append(new_alarm)
        self.update_alarm_list()

    def update_alarm_list(self):
        # Display Alarm Management Screen
        alarm_management_screen = BoxLayout(orientation='vertical')

        for alarm in self.alarms:
            alarm_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
            alarm_box.add_widget(Label(text=alarm.time))
            switch = Switch(active=alarm.is_enabled, on_press=lambda x: self.toggle_alarm(alarm))
            alarm_box.add_widget(switch)
            alarm_management_screen.add_widget(alarm_box)

        # Add Snooze and Dismiss buttons

        self.root.clear_widgets()
        self.root.add_widget(alarm_management_screen)

    def toggle_alarm(self, alarm):
        alarm.is_enabled = not alarm.is_enabled
        # Add logic to handle alarm state change

    def on_start(self):
        # Schedule a function to update the current time every second
        Clock.schedule_interval(self.update_current_time, 1)

    def update_current_time(self, dt):
        # Update the current time label
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.text = f"Current Time: {current_time}"

if __name__ == '__main__':
    AlarmApp().run()
