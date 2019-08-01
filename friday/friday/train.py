from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import datetime
chatterbot = ChatBot(
    'Friday',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatterbot)
# trainer = ChatterBotCorpusTrainer(chatterbot)
#
# trainer.train(
#     "chatterbot.corpus.english"
# )

# trainer.train([
#     'Hello',
#     'Hi',
#     'How are you?',
#     'I am good, How about you?',
#     'I am also good.',
#     'Thank you',
#     'How can I help you?',
#     'I want to create a chat bot',
#     'Have you read the documentation?',
#     'No, I have not',
#     'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html',
# ])

# trainer.train([
#     'hello Friday',
#     'Hello sir, Nice to see you.',
# ])
# trainer.train([
#     'hi Friday',
#     'Hello sir, Nice to see you.',
# ])
#
# trainer.train([
#     'get lost',
#     'Please be gentle'
# ])
# trainer.train([
#     'what is the time',
#     str(datetime.datetime.now()),
#     'what is current time',
#     str(datetime.datetime.now()),
#     'current time',
#     str(datetime.datetime.now()),
#     'current date and time',
#     str(datetime.datetime.now()),
#     'current date time',
#     str(datetime.datetime.now()),
#     'current date',
#     str(datetime.datetime.now()),
#     'date',
#     str(datetime.datetime.now()),
#     'time',
#     str(datetime.datetime.now())
# ])

# trainer.train([
#     'Whats your name',
#     'I am Friday. I am AI created By Devender',
# ])