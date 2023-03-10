from project.topic import Topic
from project.document import Document
from project.category import Category


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        # add the category if it is not in the list
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        # add the topic if it does not exist
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        # add the document if it does not exist
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        # edit the name of the category with the provided id
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        # edit the topic with the given id
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        # edit the document with the given id
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document.file_name = new_file_name

    def delete_category(self, category_id):
        # delete the category with the provided id
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        # delete the topic with the provided id
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document)

    def get_document(self, document_id):
        # return the document with the provided id
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return document

    def __repr__(self):
        # returns a string representation of each document on separate lines
        result = [doc.__repr__() for doc in self.documents]
        return '\n'.join(result)
