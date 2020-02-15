class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)



bulls_on_parade = ("They rally around the family",
                    "With pockets full of shells")

s1 = Song(bulls_on_parade)
s1.sing_me_a_song()


