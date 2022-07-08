from jsonserializaer import JsonSerializer
from xmlserializer import XmlSerializer
from song import Song


song = Song(song_id="1", title="The Same River", artist="Riverside")

print(song.serialize(JsonSerializer()))
print(song.serialize(XmlSerializer()))
