from player.music_library import MusicLibrary

class MusicPlayer:

  def __init__(self, subprocess):
    self.subprocess = subprocess

  def play(self, file):
    self.subprocess.call(["afplay", file])
    return file

  