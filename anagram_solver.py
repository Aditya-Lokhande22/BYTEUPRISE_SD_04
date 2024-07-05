from itertools import permutations

class AnagramSolver:
    def __init__(self, dictionary):
        self.dictionary = set(dictionary)

    def is_valid_word(self, word):
        return word in self.dictionary

    def solve_anagram(self, jumbled_word):
        solutions = set()
        for perm in permutations(jumbled_word):
            possible_word = ''.join(perm)
            if self.is_valid_word(possible_word):
                solutions.add(possible_word)
        return solutions
