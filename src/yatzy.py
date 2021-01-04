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
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
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
