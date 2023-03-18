from abc import ABC, abstractmethod

# Adjust according to Open/Close principle (not the goal of exercise)
# Adjust Single Responsibility


class IContent(ABC):
    def __init__(self, content, content_type):
        self.content = content
        self.content_type = content_type

    @abstractmethod
    def format_content(self):
        ...


class FormattedContent(IContent):

    def format_content(self):
        return f"<{self.content_type}> {self.content} </{self.content_type}>"


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content: FormattedContent):
        self.__content = content

    def __repr__(self):

        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content.format_content()}"


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = FormattedContent('Hello, there!', 'MyML')
email.set_content(content)
print(email)
print()
content = FormattedContent('Hello, there!', 'HTML')
email.set_content(content)
print(email)
