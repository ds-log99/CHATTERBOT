from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False,
    logic_adapters=[{
                     "import_path":"chatterbot.logic.BestMatch",
                      "default_response":"Sorry I don't have an answer",
                      "maximum_similarity_treshold": 0.9
                    }
                    ])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

#list_trainer = ListTrainer(bot)

#list_trainer.train(list_to_train)
#list_trainer.train(list_to_train2)

@app.route("/")
def main():
    return render_template("index.html")

#while True:
#    user_response = input("user: ")
#    print( "Chatbot: " + str(bot.get_response(user_response)))
#    if user_response == "exit":
#        break
@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
