USD = 'USD'
GOLD = 'GOLD'
from player import Player
from moderator import Moderator
from admin import Admin
name = (raw_input("Write your username: "))
if __name__ == '__main__':
    player1 = Player(name)
    player1.register()
    player1.login()
    player1.init_money()
    player1.give_money(USD, 1000)
    player1.give_money(USD, 2000)
    player1.give_money(GOLD, 20)
    player1.take_money(GOLD, 50)
    player1.logout()
    print(player1.sessions)
    print(player1.player_as_dict())
    moder1 = Moderator(name)
    moder1.register()
    moder1.login()
    moder1.give_a_ban()
    moder1.take_a_ban()
    moder1.logout()
    print(moder1.moderator_as_dict())
    admin1 = Admin(name)
    admin1.register()
    admin1.login()
    admin1.make_a_moderator()
    import MySQLdb

    con = MySQLdb.connect('localhost', 'root', 'root', 'classes');

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM players")
        for row in cur.fetchall():
            print(row)