import json
import datetime
from session import Session
from money import Money
class Player(object):
    def __init__(self, name = None, email = None, password = None, sessions = None, wallet = None):
        self.name = name
        self.email = email
        self.password = password
        self.sessions = list()
        self.wallet = {}
    def player_as_dict(self):
        player_as_dict = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions,
            "wallet": self.wallet
        }
        return player_as_dict
    def save(self, file_object):
        json.dump(self.player_as_dict(), file_object)
    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        return object_as_dict
    def register(self):
        self.email = raw_input('Enter your email: ')
        self.password = raw_input('Enter your password: ')
        print("Registration completed. Player {} is created".format(self.name))
    def login(self):
        password = raw_input("{},please,enter your password: ".format(self.name))
        if password != self.password:
            raise Exception("Wrong password")
        else:
            print("You are logged in successfully")
            s = Session(starttime=datetime.datetime.now())
            self.sessions.append(s)
    def init_money(self):
        global USD
        USD = 'USD'
        global GOLD
        GOLD = 'GOLD'
        self.wallet[USD] = Money(USD, 100)
        self.wallet[GOLD] = Money(GOLD, 200)
    def give_money(self, code, amount):
        self.wallet[code].amount += amount
    def take_money(self, code, amount):
        self.wallet[code].amount -= amount
    def logout(self):
        print("You are logout")
        self.sessions[-1].finishtime = datetime.datetime.now()

