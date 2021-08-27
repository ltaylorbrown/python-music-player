import unittest

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):

    # def setUp(self):
    #     test1 = MusicLibrary()
    #     test1.add(Track("Run","Foo Fighters", "Run.mp3"))
    #     test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
    #     test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        
    def test_constructs(self):
        MusicLibrary()

    def test_add(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        self.assertEqual(test1.all()[0].title, "Run")
        self.assertEqual(test1.all()[0].artist, "Foo Fighters")
        self.assertEqual(test1.all()[0].file, "Run.mp3")

    def test_remove_song(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        test1.remove(1)
        self.assertEqual(len(test1.all()), 2 )

    def test_remove_two(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        test1.remove(1)
        self.assertEqual(test1.all()[0].title, "Run")
        self.assertEqual(test1.all()[1].title, "Learn to Fly")
   

    def test_search_track_title(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        searching = test1.search("title", "Run")
        self.assertEqual(len(searching), 1)

    def test_search_track_artist(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        searching = test1.search("artist", "Foo")
        self.assertEqual(len(searching), 3)

    def test_search_track__file(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        searching = test1.search("file", "Fly.mp3")
        self.assertEqual(len(searching), 1)

    def test_search_track_any(self):
        test1 = MusicLibrary()
        test1.add(Track("Run","Foo Fighters", "Run.mp3"))
        test1.add(Track("Monkey Wrench","Foo Fighters", "Wrench.mp3"))
        test1.add(Track("Learn to Fly","Foo Fighters", "Fly.mp3"))
        searching = test1.search("any", "Monkey")
        self.assertEqual(len(searching), 1)
