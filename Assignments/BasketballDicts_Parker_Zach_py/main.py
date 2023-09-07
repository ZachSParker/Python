class Player:
    def __init__(self,player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
    @classmethod
    def get_team(cls,list):
        players = []
        for player in list:
            player_new = cls(player)
            players.append(player_new)
        return players

player = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
]
player_list = Player.get_team(player)
for person in player_list:
    print(person.name)


# kevin_player = player[0]
# jason_player = player[1]
# kyrie_player = player[2]
# player1 = Player(kevin_player)
# player2 = Player(jason_player)
# player3 = Player(kyrie_player)
# print(player1.name)
# print(player2.name)
# print(player3.name)











