from random import randint
class Yatzy:

    def __init__(self, name_players):
        #players is an integer which represents the number of players in this game
        self.players = self.Players()
        #self.players.nadia = Yatzy.Players.Player("nadia")
        for name in name_players:
            exec("self.players."+name.lower()+" = self.Players.Player(\""+name+"\")")
        
    def get_participants(self):
        return [x for x in self.players.__dict__.keys()]
    
    class Players:

        class Player:

            def __init__(self, name):
                self._name = name
                self._points = 0
                self._used_scores = []
                self.dice = self.Dice()

            @property
            def name(self):
                return self._name

            @property
            def points(self):
                return self._points

            @property
            def used_scores(self):
                return "\n".join(self._used_scores)

            class Dice:

                def __init__(self):
                    self._first = 0
                    self._second = 0
                    self._third = 0
                    self._fourth = 0
                    self._fifth = 0
                    self._rolls = 0

                @property
                def first(self):
                    return self._first

                @property
                def second(self):
                    return self._second

                @property
                def third(self):
                    return self._third

                @property
                def fourth(self):
                    return self._fourth

                @property
                def fifth(self):
                    return self._fifth
                
                @property
                def rolls(self):
                    return self._rolls
                
                def get_all_dice(self):
                    dice = []
                    dice.append(self._first)
                    dice.append(self._second)
                    dice.append(self._third)
                    dice.append(self._fourth)
                    dice.append(self._fifth)
                    return dice

                def roll(self, discrimator=[]):
                    if self._rolls <= 2:
                        if self._first not in discrimator:
                            self._first = randint(1,6)
                        if self._second not in discrimator:
                            self._second = randint(1,6)
                        if self._third not in discrimator:
                            self._third = randint(1,6)
                        if self._fourth not in discrimator:
                            self._fourth = randint(1,6)
                        if self._fifth not in discrimator:
                            self._fifth = randint(1,6)
                        self._rolls += 1
                        msg="You rolled "+str(self._rolls)+" time(s)!"
                    else:
                        msg="You cant reroll anymore!"
                    return msg

    class Score:
        @staticmethod
        def chance(dice):
            total = 0
            for die in dice:
                total += die
            return total

        @staticmethod
        def yatzy(dice):
            yatzy_candidate = dice[0]
            answer = 50
            for die in dice:
                if die != yatzy_candidate:
                    answer = 0
                    break
            return answer
        
        @staticmethod
        def aces(dice):
            sum = 0
            for die in dice:
                if die == 1:
                    sum += 1
            return sum

        @staticmethod
        def twos(dice):
            sum = 0
            for die in dice:
                if die == 2:
                    sum += 2
            return sum
        
        @staticmethod
        def threes(dice):
            sum = 0
            for die in dice:
                if die == 3:
                    sum += 3
            return sum
        
        @staticmethod
        def fours(dice):
            sum = 0
            for die in dice:
                if die == 4: 
                    sum += 4
            return sum
        
        @staticmethod
        def fives(dice):
            sum = 0
            for die in dice:
                if die == 5:
                    sum += 5
            return sum
        
        @staticmethod
        def sixes(dice):
            sum = 0
            for die in dice:
                if die == 6:
                    sum += 6
            return sum
        
        @staticmethod
        def three_of_a_kind(dice):
            dict_dice = dict.fromkeys(dice,0)
            for die in dice:
                dict_dice[die] += 1
            for die in dict_dice:
                if dict_dice[die] >= 3:
                    sumator = 0
                    for i in dice:
                        sumator += i
                    answer = sumator
                    break
                else:
                    answer = 0
            return answer
        
        @staticmethod
        def four_of_a_kind(dice):
            dict_dice = dict.fromkeys(dice,0)
            for die in dice:
                dict_dice[die] += 1
            for die in dict_dice:
                if dict_dice[die] >= 4:
                    sumator = 0
                    for i in dice:
                        sumator += i
                    answer = sumator
                    break
                else:
                    answer = 0
            return answer
        
        @staticmethod
        def small_straight(dice):
            new_dice = sorted(dice)[:-1]
            if new_dice == [1,2,3,4] or new_dice == [2,3,4,5] or new_dice == [3,4,5,6]:
                answer = 30
            else:
                answer = 0
            return answer

        @staticmethod
        def large_straight(dice):
            sorted_dice = sorted(dice)
            if sorted_dice == [1,2,3,4,5] or sorted_dice == [2,3,4,5,6]:
                answer = 40
            else:
                answer = 0
            return answer
        

        @staticmethod
        def full_house(dice):
            dict_dice = dict.fromkeys(dice,0)
            if len(dict_dice) == 2:
                answer = 25
            else:
                answer = 0
            return answer

yatzy = Yatzy(["Juan","Nadia"])

list_of_players = yatzy.get_participants()

print("Bienvenidos al juego de Yatzy sin Copyright!")
print("Que empiece el juego!")

for name in list_of_players:
    exec('player = yatzy.players.'+name)
    print(player.name + ", tu turno!")
    discriminator = []
    while True:
        player.dice.roll()
        print(player.name + ", Has sacado estos dados:")
        player_dice = player.dice.get_all_dice()
        for i in range(len(player_dice)):
            print("dado numero " + (i+1) + " es: " + player_dice[i] + "\n")
            while True:
                print(player.name + ", que dados quieres quedarte y cuales tirar de nuevo?")
                decision = input("Tomaré el dado número...: ")
                discriminator.append(player_dice[int(decision)-1])
                print("Quieres coger otro dado mas?")





print("prueba")