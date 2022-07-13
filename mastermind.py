import random
import math
from collections import defaultdict

NUM_COLORS = 8

class MM:
    def __init__(self, code_size):
        self.code = [random.randint(1,NUM_COLORS) for i in range(code_size)]
        self.size = code_size

        self.fcolors = defaultdict(int)
        for i in self.code:
            self.fcolors[i] += 1

        self.possible = []
        for i in range(1,NUM_COLORS+1):
            for j in range(1, NUM_COLORS+1):
                for k in range(1, NUM_COLORS+1):
                    for l in range(1,NUM_COLORS+1):
                        self.possible.append([i,j,k,l])

    def prune(self, guess, ans):		
        next_pos = []

        for i in self.possible:
            if score(i,guess) == ans:
                next_pos.append(i)

        self.possible = next_pos

    def itguess(self):
        best_guess = self.possible[0]
        best_score = 0

        for i in self.possible:
            num_scores = defaultdict(int)
            current_score = 0

            for j in self.possible:
                num_scores[score(j,i)] += 1
            for scores in num_scores:
                prob_score = num_scores[scores] / len(self.possible)
                current_score += prob_score * math.log2(1/prob_score)

            if current_score > best_score:
                best_score = current_score
                best_guess = i

        return best_guess

def play(mm):
    done = True
    counter = 0

    while done:
        counter += 1

        guess = mm.itguess()
        gs = score(mm.code, guess)

        if gs == (4,0):
            print(guess)
            done = False
        else:
            print(guess, gs)

        mm.prune(guess, gs)

    print(counter)

def score(secret,guess): 
    red = 0
    white = 0

    fcolors = defaultdict(int)
    for i in secret:
        fcolors[i] += 1

    ccolors = defaultdict(int)

    used = [False for i in range(mm.size)]

    for i in range(4):
        if guess[i] == secret[i]:
            red += 1
            used[i] = True
            ccolors[guess[i]] += 1

    for i in range(4):
        if ccolors[guess[i]] < fcolors[guess[i]] and not used[i]:
            white += 1
            ccolors[guess[i]] += 1
    return (red, white)

def runner():
    mm = MM(4)
    print(mm.code)
    play(mm)

if __name__ == '__main__':
    runner()
