from project.song import Song


class Album:
    def __init__(self, name: str, *album_songs: Song):
        self.name = name
        self.published = False
        self.songs = [*album_songs]

    def add_song(self, song: Song) -> str:
        # ◦ Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
        # ◦ If the song is single, returns "Cannot add {song_name}. It's a single"
        # ◦ If the album is published, returns "Cannot add songs. Album is published."
        # ◦ If the song is already added, return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return "Cannot add songs. Album is published."

        elif song in self.songs:
            return "Song is already in the album."

        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        # ◦ Removes the song with the given name and returns
        #   "Removed song {song_name} from album {album_name}."
        # ◦ If the song is not in the album, returns "Song is not in the album."
        # ◦ If the album is published, returns "Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        else:
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}."

    def publish(self) -> str:
        # ◦ Publishes the album (set to True) and returns "Album {name} has been published."
        # ◦ If the album is published, returns "Album {name} is already published."
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        else:
            return f"Album {self.name} is already published."

    def details(self) -> str:
        print_out = [f"Album {self.name}"]
        """
        Album {name}
        == {first_song_info}
        == {second_song_info}
         …
        == {n_song_info}
        """
        for song in self.songs:
            print_out.append(f"== {song.get_info()}")

        return '\n'.join(print_out)
