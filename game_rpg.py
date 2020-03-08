class Room:
    def __init__(self, name, description=None, character=None, item=None):
        self.name = name
        self.description = description
        self.doors = {"north": None, "south": None, "east": None, "west": None}
        self.character = character
        self.item = item

    def set_description(self, content):
        self.description = content

    def link_room(self, room, direction):
        if id(self) != id(room):
            self.doors[direction] = room

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(self.description)
        for direction in self.doors:
            if self.doors[direction]:
                print(f"The {self.doors[direction].name} is {direction}")

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        if not direction:
            return self

        return self.doors[direction]


class Item:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        return self.name


class Enemy:
    num = 0

    def __init__(self, name, description, conversation=None, weakness=None):
        self.name = name
        self.description = description
        self.conversation = conversation
        self.weakness = weakness

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, item):
        return item == self.weakness

    def get_defeated(self):
        self.num += 1
        return self.num
