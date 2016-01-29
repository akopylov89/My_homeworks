import json
from player import Player
class Moderator(Player):
    def __init__(self, name = None, email = None, password = None, sessions = None, wallet = None, player_for_control = None):
        self.name = name
        self.email = email
        self.password = password
        self.sessions = list()
        self.wallet = {}
        self.player_for_control = {}
    def moderator_as_dict(self):
        moderator_as_dict = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions,
            "wallet": self.wallet,
            "player_for_control": self.player_for_control
        }
        return moderator_as_dict
    def save(self, file_object_moderator):
        json.dump(self.moderator_as_dict(), file_object_moderator)
    def load(self, file_object_moderator):
        object_as_dict = json.load(file_object_moderator)
        self.name = object_as_dict["name"]
        return object_as_dict
    def give_a_ban(self):
        player = raw_input('Write the name of a banned player: ')
        self.player_for_control[player] = "banned"
        print("Player {} is banned".format(player))
    def take_a_ban(self):
        player = raw_input('Write the name of a player to take ban: ')
        if player in self.player_for_control.keys():
            self.player_for_control[player] = "unbanned"
            print("Player {} is unbanned".format(player))
        else:
            raise Exception('Ban error: {} is not banned'.format(player))
    def __repr__(self):
        return '{}'.format(self.name)