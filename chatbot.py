from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
import spacy

spacy.load('pt_core_news_sm')
# --------------------------------------
# Instantiate agent
# BestMatch = selects response by best known match to statement
# response_selection_method has 3 options:
# get_first_response,get_most_frequent_response or get_random_response
# statement_comparison_function has 4 options:
# read options and explanations here: https://chatterbot.readthedocs.io/en/stable/comparisons.html#statement-comparison
# default_response is a response in case the bot doesn't know what to say
# maximum_similarity_threshold:
# maximum amount of similarity between 2 statement required before the search process is halted(default:0.95)
bot = ChatBot('chatbot_test',
              read_only=False,
              response_selection_method=get_most_frequent_response,
              logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
                               "response_selection_method": 'chatterbot.response_selection.get_most_frequent_response',
                               "statement_comparison_function": 'chatterbot.comparisons.SynsetDistance',
                               'default_response': 'Ainda não sei responder essa frase.',
                               'maximum_similarity_threshold': 0.95
                               }],
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='postgresql://postgres:postgres@localhost/chatbot_database', )
# local - dev config
# database_uri='postgresql://postgres:postgres@localhost/chatbot_database',)

# online - prod config
# database_uri='postgres://iuznelluxbwsrr:04344ff8343fb2d24f6b53b255898a9cb97ed35024511a8c33cf62e83962e19b@ec2-52-22-238-188.compute-1.amazonaws.com:5432/d7adm1a9fde7ib',)
# --------------------------------------

# Corpus Trainer
corpus_trainer = ChatterBotCorpusTrainer(bot)

# use this line and comment out the complete pack if
# you feel like doing some quick testing
# corpus_trainer.train('data/greetings.yml')


corpus_trainer.train('data/botprofile.yml', 'data/compliment.yml', 'data/computers.yml', 'data/context_free_br.yml',
                     'data/conversations.yml', 'data/emotion.yml', 'data/food.yml', 'data/games.yml',
                     'data/gossip.yml', 'data/greetings.yml', 'data/health.yml', 'data/history.yml',
                     'data/linguistic_knowledge.yml', 'data/literature.yml', 'data/money.yml', 'data/movies.yml',
                     'data/politics.yml', 'data/proverbs.yml', 'data/psychology.yml', 'data/science.yml',
                     'data/sports.yml', 'data/suggestions.yml', 'data/trivia.yml', 'data/unilab.yml')


# --------------------------------------
# Conversation Loop - terminal only
def conversation():
    while True:
        try:
            question = input('Usuário: ')
            answer = bot.get_response(question)
            if answer.confidence > 0.5:
                print('bot: ', answer)
                print('confidence', answer.confidence)
            else:
                print('bot: ', 'Ainda não sei responder essa frase')
                print('confidence', answer.confidence)
        # CONTROL+D to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# --------------------------------------
