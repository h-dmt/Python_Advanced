from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        # ◦ Adds an album to the collection and returns
        # "Band {band_name} has added their newest album {album_name}."
        # ◦ If the album is already added, returns
        # "Band {band_name} already has {album_name} in their library."

        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str) -> str:
        # ◦ Removes the album from the collection and returns "Album {name} has been removed."
        # ◦ If the album is published, returns "Album has been published. It cannot be removed."
        # ◦ If the album is not in the collection, returns "Album {name} is not found."

        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album:
            if album.published:
                return "Album has been published. It cannot be removed."

            else:
                self.albums.remove(album)
                return f"Album {album.name} has been removed."

    def details(self) -> str:
        print_out = [f"Band {self.name}"]
        """
        "Band {name}
        {album details}
        ...
        {album details}"
        """
        for album in self.albums:
            print_out.append(album.details())

        return '\n'.join(print_out)
