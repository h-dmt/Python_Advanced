import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.COLS = 4
        self.photos = [[] for _ in range(pages)]  # representing the album with its pages where you should put the
                                                  # photos. Each page can contain only 4 photos.

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.

        album_pages = math.ceil(photos_count / 4)
        return cls(album_pages)

    def add_photo(self, label: str):
        # adds the photo in the first possible page and slot and return
        # "{label} photo added successfully on page
        # {page_number(starting from 1)} slot {slot_number(starting from 1)}".
        # If there are no free slots left, return "No more free slots"

        for page in range(len(self.photos)):
            if len(self.photos[page]) < self.COLS:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} " \
                       f"slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        # returns a string representation of each page and the photos in it.
        # Each photo is marked with "[]", and the page separation is made using 11 dashes (-).
        # For example, if we have 1 page and 2 photos:
        """
        -----------
        [] []
        -----------
        and if we have 2 empty pages:
        -----------

        -----------

        -----------
        """
        dashes = '-' * 11
        print_out = [dashes]

        for page in range(len(self.photos)):

            print_out.append(('[] ' * len(self.photos[page])).rstrip())
            print_out.append(dashes)

        return '\n'.join(print_out)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())