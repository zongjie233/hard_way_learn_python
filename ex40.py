class Song(object):

    def __init__(self,lyrics, author, name):
        self.lyrics = lyrics
        self.author = author
        self.name = name

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def tell_me_the_author(self):
        print(self.author)

    def tell_me_the_song_name(self):
        print(self.name)








happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"],"hs", "happy birthday")

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"],"dont know","dont know")

happy_bday.sing_me_a_song()
happy_bday.tell_me_the_author()
happy_bday.tell_me_the_song_name()

bulls_on_parade.sing_me_a_song()
bulls_on_parade.tell_me_the_author()
bulls_on_parade.tell_me_the_song_name()

