class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str):
        # change the topic and the storage folder
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        #  returns a string representation of the topic in the format:
        #  "Topic {id}: {topic} in {storage_folder}"

        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
