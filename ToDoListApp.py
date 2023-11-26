# Import necessary modules
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

class Task:
    def __init__(self, title, description="", priority="Low", due_date=""):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.is_completed = False

class TodoListApp(App):
    def __init__(self, **kwargs):
        super(TodoListApp, self).__init__(**kwargs)
        self.tasks = []  # List to store Task objects

    def build(self):
        # Home Screen
        home_screen = BoxLayout(orientation='vertical')
        self.task_list_label = Label(text="Task List")
        home_screen.add_widget(self.task_list_label)

        # Add tasks to the layout
        self.update_task_list()

        # Add New Task Button
        add_task_button = Button(text="Add New Task", on_press=self.show_task_creation)
        home_screen.add_widget(add_task_button)

        return home_screen

    def show_task_creation(self, instance):
        # Task Creation Popup
        task_creation_popup = Popup(title="Create New Task", size_hint=(None, None), size=(400, 300))
        task_creation_layout = BoxLayout(orientation='vertical')

        title_input = TextInput(multiline=False, hint_text="Task Title")
        description_input = TextInput(multiline=True, hint_text="Task Description")
        priority_input = TextInput(multiline=False, hint_text="Priority (Low, Medium, High)")
        due_date_input = TextInput(multiline=False, hint_text="Due Date (optional)")

        save_button = Button(text="Save", on_press=lambda x: self.save_task(
            title_input.text, description_input.text, priority_input.text, due_date_input.text
        ))

        task_creation_layout.add_widget(title_input)
        task_creation_layout.add_widget(description_input)
        task_creation_layout.add_widget(priority_input)
        task_creation_layout.add_widget(due_date_input)
        task_creation_layout.add_widget(save_button)

        task_creation_popup.add_widget(task_creation_layout)
        task_creation_popup.open()

    def save_task(self, title, description, priority, due_date):
        new_task = Task(title, description, priority, due_date)
        self.tasks.append(new_task)
        self.update_task_list()

    def update_task_list(self):
        # Display the task list
        task_list_screen = BoxLayout(orientation='vertical')

        for task in self.tasks:
            task_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
            task_box.add_widget(Label(text=task.title))
            task_box.add_widget(Label(text=task.priority))
            task_box.add_widget(ToggleButton(text="Done" if task.is_completed else "Active", on_press=lambda x: self.toggle_task_completion(task)))
            task_box.add_widget(Button(text="Edit", on_press=lambda x: self.show_task_editing(task)))
            task_box.add_widget(Button(text="Delete", on_press=lambda x: self.delete_task(task)))
            task_list_screen.add_widget(task_box)

        self.task_list_label.text = "Task List"
        self.root.clear_widgets()
        self.root.add_widget(self.task_list_label)
        self.root.add_widget(task_list_screen)

    def toggle_task_completion(self, task):
        task.is_completed = not task.is_completed
        self.update_task_list()

    def show_task_editing(self, task):
        # Task Editing Popup
        task_editing_popup = Popup(title="Edit Task", size_hint=(None, None), size=(400, 200))
        task_editing_layout = BoxLayout(orientation='vertical')

        title_input = TextInput(multiline=False, text=task.title)
        description_input = TextInput(multiline=True, text=task.description)
        save_button = Button(text="Save", on_press=lambda x: self.edit_task(task, title_input.text, description_input.text))

        task_editing_layout.add_widget(title_input)
        task_editing_layout.add_widget(description_input)
        task_editing_layout.add_widget(save_button)

        task_editing_popup.add_widget(task_editing_layout)
        task_editing_popup.open()

    def edit_task(self, task, new_title, new_description):
        task.title = new_title
        task.description = new_description
        self.update_task_list()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.update_task_list()

if __name__ == '__main__':
    TodoListApp().run()
