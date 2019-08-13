class Message:

    def __init__(self, title = None, description = None):
        self.__title = title
        self.__description = description

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

class MessageQueue:

    def __init__(self):
        self.__messages = []

    def add(self, message):
        self.__messages.append(message)

    def remove(self):
        message = self.__messages[0]
        self.__messages = self.__messages[1:]
        return message

    def is_empty(self):
        if self.__messages:
            return False
        return True

class Publisher:

    def publish(self, message, service):
        service.add_message(message)

class Subscriber:

    def __init__(self):
        self.__subscriberMessages = []

    def get_subscriber_messages(self):
        return self.__subscriberMessages

    def set_subscriber_messages(self, value):
        self.__subscriberMessages = value

    def subscribe(self, title, service):
        service.add_subscriber(self, title)

    def unsubscribe(self, title, service):
        service.remove_subscriber(self, title)

    def get_messages(self, title, service):
        service.get_messages(self, title)

    def print_messages(self):
        for message in self.__subscriberMessages:
            print("Message ->", message.get_title(), ":", message.get_description())

class PubSubService:

    def __init__(self):
        self.__messageQueue = MessageQueue()
        self.__subscribersTitle = {}

    def add_message(self, message):
        self.__messageQueue.add(message)

    def add_subscriber(self, subscriber, title):
        if title in self.__subscribersTitle.keys():
            self.__subscribersTitle[title].append(subscriber)
        else:
            self.__subscribersTitle[title] = [subscriber]

    def remove_subscriber(self, subscriber, title):
        self.__subscribersTitle[title].remove(subscriber)

    def broadcast(self):
        if not self.__messageQueue.is_empty():
            while(not self.__messageQueue.is_empty()):
                message = self.__messageQueue.remove()

                title = message.get_title()

                subscribers = self.__subscribersTitle[title]

                for subscriber in subscribers:
                    subscriber.get_subscriber_messages().append(message)
        else:
            print("No messages from publishers to display")

    def get_messages(self, subscriber, title):
        if not self.__messageQueue.is_empty():
            while(not self.__messageQueue.is_empty()):
                message = self.__messageQueue.remove()

                if message.get_title().lower() == title.lower():
                    subscribers = self.__subscribersTitle[title]
                    for subscriber in subscribers:
                        subscriber.get_subscriber_messages().append(message)
        else:
            print("No messages from publishers to display")

def main():
    pythonPublisher = Publisher()
    javaPublisher = Publisher()

    pythonSubscriber = Subscriber()
    javaSubscriber = Subscriber()
    allSubscriber = Subscriber()

    pubSubService = PubSubService()

    pythonMsg1 = Message("Python", "Easy and Powerful programming language")
    pythonMsg2 = Message("Python", "Object Oriented Programming language")

    pythonPublisher.publish(pythonMsg1, pubSubService)
    pythonPublisher.publish(pythonMsg2, pubSubService)

    javaMsg1 = Message("Java", "Core Java Concepts")
    javaMsg2 = Message("Java", "Spring MVC & Hibernate")

    javaPublisher.publish(javaMsg1, pubSubService)
    javaPublisher.publish(javaMsg2, pubSubService)

    pythonSubscriber.subscribe("Python", pubSubService)
    javaSubscriber.subscribe("Java", pubSubService)
    allSubscriber.subscribe("Python", pubSubService)
    allSubscriber.subscribe("Java", pubSubService)

    pubSubService.broadcast()
    print("Messages of Python Subscriber are: ")
    pythonSubscriber.print_messages()
    print()
    print("Messages of Java Subscriber are: ")
    javaSubscriber.print_messages()
    print()
    print("Messages of All Language Subscriber are: ")
    allSubscriber.print_messages()

    print("\nPublishing 2 more Python messages")
    pythonMsg3 = Message("Python", "Django Framework")
    pythonMsg4 = Message("Python", "Flask Framework")

    pythonPublisher.publish(pythonMsg3, pubSubService)
    pythonPublisher.publish(pythonMsg4, pubSubService)

    pythonSubscriber.get_messages("Python", pubSubService)
    print("\nMessages of Python Subscriber now are: ")
    pythonSubscriber.print_messages()

if __name__ == "__main__":
    main()
