import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root, topdown=True):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


album_finder = find_albums("music", "Black*")
song_list = find_songs(album_finder)

for s in song_list:
    print(s)
