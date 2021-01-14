class Monkey:
    actions = ['saying "Boo boo boo"', "dancing rock&roll", "jumping like a crazy frog"]

    def __init__(self, name="Dummy Monkey", age=2, actions=None):
        self.name = name
        self.age = age
        if actions is not None:
            self.actions = actions

    def __str__(self):
        return f"Monkey '{self.name}' ({self.age} years old)"

    def action(self):
        from random import choice

        return f"{self.name} is {choice(self.actions)}"

    def set_name(self, new_name):
        if new_name:
            self.name = new_name

    def set_age(self, age):
        if age > 0:
            self.age = age

    def set_actions(self, actions):
        if isinstance(actions, (list, tuple)):
            self.actions = actions
    
