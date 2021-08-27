import unittest, subprocess

from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer
from ui.mocks import MockSubprocess

class TestMusicPlayer(unittest.TestCase):

    def test_constructs(self):
        MusicPlayer(subprocess)

    def TestMusicPlayer(self):
        mock_subprocess = MockSubprocess()
        player = MusicPlayer(mock_subprocess)
        test1 = MusicLibrary
        test1.add(Track("Fav", "Artist", "data/tunes/myfav.wav"))
        test1.add(Track("Two", "Artist", "data/tunes/sent.wav"))
        test1.add(Track("Three", "Artist", "data/tunes/myfav.wav"))
        self.assertEqual(player.play(test1.all()[1].file), "data/tunes/sent.wav" )
        self.assertTrue(mock_subprocess.called)

# class TestMusicPlayer(unittest.TestCase):


#     def test_constructs(self):
#         MusicPlayer(subprocess)

#     def test_play(self):
#         player = MusicPlayer(subprocess)
#         test1 = MusicLibrary()
#         test1.add(Track("Fav", "Artist", "data/tunes/myfav.wav"))
#         test1.add(Track("Two", "Artist", "data/tunes/sent.wav"))
#         test1.add(Track("Three", "Artist", "data/tunes/myfav.wav"))

#         self.assertEqual(player.play(test1.all()[1].file), "data/tunes/sent.wav" )


