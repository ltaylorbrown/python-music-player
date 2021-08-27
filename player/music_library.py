# from abc import abstractstaticmethod


class MusicLibrary:
   
    def __init__(self):
        self.playlist = []
    
    def all(self):
        return self.playlist

    def add(self, song):  
        self.playlist.append(song)

    def remove(self, number):
        if number < len(self.playlist):
            self.playlist.pop(number)
            return True
        else:
            return False

    def search(self, field, query):
        query = query.lower()
        if field == "title":
            return [track for track in self.playlist if query in track.title.lower()]
        elif field == "artist":
            return [track for track in self.playlist if query in track.artist.lower()]
        elif field == "file":
            return [track for track in self.playlist if query in track.file.lower()]
        elif field == "any":
            return [
                track
                for track in self.playlist
                if (query in track.title.lower())
                or (query in track.artist.lower())
                or (query in track.file.lower())
            ]
        
        

class Track:

    def __init__(self, title, artist, file): 
        self.title = title
        self.artist = artist
        self.file = file
    
    # def data(self):
    #     return [self.title, self.artist, self.file]
	


	

