class Room:
    """
    Class that represents the rooms (locations) in
    rpg game (main.py). Rooms can be connected with other
    rooms, can contain items (class Item) and characters
    (class Enemy).
    """
    def __init__(self, name, description=None, character=None, item=None):
        """
        Initializes a Room object with name.
        Description, character and item can be also specified,
        they are None by default. Creates self.doors as dict
        with keys (directions) and values (None).
        :param name: str
        :param description: str
        :param character: Enemy
        :param item: Item
        """
        self.name = name
        self.description = description
        self.doors = {"north": None, "south": None, "east": None, "west": None}
        self.character = character
        self.item = item

    def set_description(self, content):
        """
        Sets attribute self.description to content
        :param content: str
        :return: None
        """
        self.description = content

    def link_room(self, room, direction):
        """
        Links Rooms self and room (not vice-versa):
        adds a room to self.doors[direction]
        :param room: Room
        :param direction: str
        :return: None
        """
        if id(self) != id(room) and direction in ["south", "west", "east", "north"]:
            self.doors[direction] = room

    def set_character(self, character):
        """
        Sets attribute self.character to character
        :param character: Enemy
        :return: None
        """
        self.character = character

    def set_item(self, item):
        """
        Sets attribute self.item to item
        :param item: Item
        :return: None
        """
        self.item = item

    def get_details(self):
        """
        Prints details about current room.
        Prints all available directions ans description
        of the room self.
        :return: None
        """
        print(self.description)
        for direction in self.doors:
            if self.doors[direction]:
                print(f"The {self.doors[direction].name} is {direction}")

    def get_character(self):
        """
        Returns self.character
        :return: Enemy
        """
        return self.character

    def get_item(self):
        """
        Returns self.item
        :return: Item
        """
        return self.item

    def move(self, direction):
        """
        Returns Room, that can be reached by direction
        from the current room. Returns self if direction
        is not specified.
        :param direction: str
        :return: Room
        """
        if not direction:
            return self

        return self.doors[direction]


class Item:
    """
    Class that represents the items in rpg game (main.py).
    Items can be taken by user and they can be used
    to fight with enemies (class Enemy).
    """
    def __init__(self, name, description=None):
        """
        Initializes an item with name and description.
        If description is not specified, than it is None by default.
        :param name: str
        :param description: str
        """
        self.name = name
        self.description = description

    def set_description(self, description):
        """
        Sets attribute self.description to description
        :param description: str
        :return: None
        """
        self.description = description

    def describe(self):
        """
        Prints the name of item (self.name) and self.description
        :return: None
        """
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """
        Returns attribute self.name
        :return: str
        """
        return self.name


class Enemy:
    """
    Class that represents the enemies in rpg game (main.py).
    Enemy objects can speak (self.talk), fight (self.fight).
    They have weakness (Item) and can be defeated.
    """
    num = 0

    def __init__(self, name, description, conversation=None, weakness=None):
        """
        Initializes an Enemy object with name and description. Conversation and
        weakness can also be specified, but they are set None by default
        :param name: str
        :param description: str
        :param conversation: str
        :param weakness: Item
        """
        self.name = name
        self.description = description
        self.conversation = conversation
        self.weakness = weakness

    def set_conversation(self, conversation):
        """
        Sets attribute self.conversation to conversation
        :param conversation: str
        :return: None
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        Sets attribute self.weakness to weakness
        :param weakness: str
        :return: None
        """
        self.weakness = weakness

    def describe(self):
        """
        Prints the name of Enemy object (self.name).
        Prints the description (self.description) as well.
        :return: None
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """
        Prints self.name and self.conversation
        :return: None
        """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, item):
        """
        Returns True if Enemy (self) can be defeated using
        item 'item'. Returns False otherwise.
        :param item: Item
        :return: bool
        """
        return item == self.weakness

    def get_defeated(self):
        """
        Adds 1 to number of current defeated enemies (num) and
        returns that new number num.
        :return: int
        """
        self.num += 1
        return self.num
