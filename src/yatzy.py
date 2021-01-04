class Yatzy:

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

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
"""
#Yatzy.three_of_a_kind([3,3,3,4,5])
Yatzy(3,3,3,4,5).three_of_a_kind()

dice = Dice([4,5,3,2,1])
Yatzy(dice).largeStraight()
class Saludo:
    def __init__(self):
        self.adios = self.Adios()
    def reveal(self, msg):
        self.adios.despedida(msg)
    class Adios:
        def despedida(self, msg):
            print(msg)
first_game = Yatzy()
first_game.first_player.roll()
first_game.first_player.rolled.rules.pick()
first_game.first_player.rolled.rules.picked.three_of_a_kind()
first_game.rules.three_of_a_kind(dice)
"""
