from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.tags = []
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        # create a new instance using the provided category and topic instances

        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        # if the tag is not already in the tags list, add it to the tags list
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content:str):
        # if the tag is in the tags list, delete it
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        # change the file name with the given one
        self.file_name = file_name

    def __repr__(self):
        # returns a string representation of a document in the format:

        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, " \
               f"tags: {', '.join(self.tags)}"
