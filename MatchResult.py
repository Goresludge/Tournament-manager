class MatchResult:
    def __init__(self, player, result, score):
        self.player = player
        self.result = result
        self.score = score
        self.data = [player, result, score]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr((self.player, self.result, self.score))
