# strs = ["fliiiir", "flowers", "floight", "floan","flooo","ffffffffffll"]
# strs = ["ab", "a"]
# strs = ["cir", "car"]
# strs = ["dog", "racecar", "racar"]
# strs = ["flower", "flow", "flight"]
strs = ["flower", "flower", "flower", "flower"]


class Wordy:
    def __init__(self, strs):

        self.counter = 0
        self.temp = strs[0]
        self.tally = 0
        self.answer = []

    def check_shortest_word(self):
        """find the shortest word as the prefix
        can not be longer than this one"""
        for word in strs:
            if len(word) < len(self.temp):
                self.temp = word
        print(f"\nshortest word = {self.temp}\n")


    def check_nth_letter(self):
        """Check for same letter at same position in
        each word - and keep a tally"""
        letter = self.temp[self.counter]
        print(f"checking {letter}\n")
        for word in strs:
            if letter in word:
                self.tally += 1


        # exit(0) if (letter/position) occurs less than number of words
        print(f"\n{letter} occurs {self.tally} times! at position {self.counter}")
        print(f"we have {len(strs)} words\n")
        if self.tally == len(strs):
            self.answer.append(letter)
            print(f"adding {letter} to self_answer\n")
        else:
            print(f"longest prefix is \"{''.join(self.answer)}\"")
            print("end!")  #
            exit(0)

        # reset tally for next iteration (next letter to the right)
        self.tally = 0
        # increment the counter (which is the index) so we move right by one
        self.counter += 1


    def check_all(self):
        """while the counter has not reached the right hand end of the list
        keep moving right"""
        while self.counter < len(self.temp):
            self.check_nth_letter()

        if len(self.answer) > 0:
            print(f"longest prefix is \"{''.join(self.answer)}\"")
        else:
            print("No matching prefix\n")


if __name__ == "__main__":

    x = Wordy(strs)

    x.check_shortest_word()
    x.check_nth_letter()
    x.check_all()
