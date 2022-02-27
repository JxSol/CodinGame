''' www.codingame.com/ide/puzzle/rock-paper-scissors-lizard-spock '''
rules = {'R': ('L', 'C'), 'P': ('R', 'S'), 'C': ('P', 'L'), 'L': ('S', 'P'), 'S': ('C', 'R')}
players_list = []


class Player:
    def __init__(self, data):
        self.num = int(data[0])
        self.sign = data[1].upper()
        self.wins = []

    def __gt__(self, other):
        if self.sign == other.sign:
            return self.num < other.num
        else:
            return other.sign in rules[self.sign]

    def win(self, other):
        self.wins.append(other.num)


for i in range(int(input())):
    players_list.append(Player(input().split()))

while len(players_list) > 1:
    player_1, player_2 = players_list.pop(0), players_list.pop(0)
    if player_1 > player_2:
        player_1.win(player_2)
        players_list.append(player_1)
    else:
        player_2.win(player_1)
        players_list.append(player_2)

print(players_list[0].num)
print(*players_list[0].wins)
