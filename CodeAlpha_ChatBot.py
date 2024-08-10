
#BASIC CHATBOT FOR VISITING NORTHEN PAKISTAN

import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

try:

    nltk.data.find('tokenizers/punkt')

    print("Congratulations...Downloaded successfully....")

except LookupError:

    print("Punkt tokenizer is not available.")

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, I will help you about visiting the northern areas of Pakistan."]
    ],
    [
        r"hi|hey|hello",
        ["Hello, I will help you about visiting the northern areas of Pakistan."]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot, and I'm here to assist you with visiting northern Pakistan."]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing well! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no need to apologize."]
    ],
    [
        r"i'm (.*) (good|well|okay|fine)",
        ["Good to hear that!"]
    ],
    [
        r"quit",
        ["Bye! Have a great day."]
    ],
    [
        r"(.*)",
        ["I can help with that! Could you please tell me more?"]
    ],
    [
        r"tell me about northern areas of pakistan",
        ["The northern areas of Pakistan are known for their stunning landscapes, including mountains, valleys, and lakes. Places like Hunza, Skardu, and Swat are popular tourist destinations."]
    ],
    [
        r"what are the best places to visit in northern pakistan?",
        ["Some of the best places to visit include Hunza Valley, Skardu, Naran Kaghan, Fairy Meadows, and the Swat Valley."]
    ],
    [
        r"what is the best time to visit northern pakistan?",
        ["The best time to visit the northern areas of Pakistan is during the summer months from May to September when the weather is pleasant, and the roads are accessible."]
    ],
    [
        r"how can i reach hunza valley?",
        ["You can reach Hunza Valley by road from Islamabad via the Karakoram Highway. The journey takes around 18-20 hours by car or bus."]
    ],
    [
        r"is it safe to travel to northern pakistan?",
        ["Yes, the northern areas of Pakistan are generally safe for tourists. However, it's always a good idea to stay updated on local news and travel advisories."]
    ],
    [
        r"what activities can i do in the northern areas of pakistan?",
        ["You can enjoy trekking, hiking, camping, sightseeing, and exploring the unique culture and cuisine of the northern areas."]
    ],
    [
        r"do i need a visa to visit northern pakistan?",
        ["If you are an international tourist, you will need a visa to enter Pakistan. However, no special permit is required to visit the northern areas."]
    ],
    [
        r"why should i visit hunza valley?",
        ["Hunza Valley is known for its breathtaking scenery, including the Rakaposhi Mountain, Altit and Baltit forts, and the serene Attabad Lake. It's a perfect place for nature lovers and adventurers."]
    ],
    [
        r"what can i do in hunza valley?",
        ["In Hunza Valley, you can explore historical forts, hike to glaciers, enjoy boating on Attabad Lake, and experience the unique local culture and hospitality."]
    ],
    [
        r"why should i visit skardu?",
        ["Skardu is a gateway to some of the world's highest peaks, including K2. It's famous for its beautiful landscapes, such as Shangrila Resort, Deosai Plains, and the tranquil Sheosar Lake."]
    ],
    [
        r"what can i do in skardu?",
        ["In Skardu, you can visit ancient forts, enjoy trekking in the Karakoram Range, camp by stunning lakes, and explore the Deosai National Park, known as the 'Land of Giants.'"]
    ],
    [
        r"why should i visit naran kaghan?",
        ["Naran Kaghan is famous for its lush green meadows, rivers, and the famous Saif-ul-Muluk Lake. It's a great spot for hiking, trout fishing, and experiencing the beauty of the Himalayas."]
    ],
    [
        r"what can i do in naran kaghan?",
        ["In Naran Kaghan, you can take a jeep safari to Saif-ul-Muluk Lake, hike to the Lulusar-Dudipatsar lakes, and enjoy the scenic views along the Kunhar River."]
    ],
    [
        r"why should i visit fairy meadows?",
        ["Fairy Meadows offers a close-up view of the mighty Nanga Parbat, the world's ninth-highest mountain. It's a tranquil place perfect for camping and experiencing nature at its best."]
    ],
    [
        r"what can i do in fairy meadows?",
        ["In Fairy Meadows, you can camp under the stars, trek to Nanga Parbat base camp, and enjoy the stunning alpine scenery and peaceful environment."]
    ],
    [
        r"why should i visit swat valley?",
        ["Swat Valley, often called the 'Switzerland of the East,' is known for its lush green landscapes, rivers, and rich history. It's a wonderful place for both nature and culture enthusiasts."]
    ],
    [
        r"what can i do in swat valley?",
        ["In Swat Valley, you can visit historical sites like the Buddhist ruins, hike through the lush green hills, explore the Malam Jabba ski resort, and enjoy the Swat River's beauty."]
    ]
]

questions_and_responses = [(pair[0], pair[1][0]) for pair in pairs]   #Extracting questions on any one keyword

# Create Chatbot instance
chatbot = Chat(pairs, reflections)


def suggest_questions(user_input):           # Function to suggest questions based on user input
  
    suggestions = []
  
    for question, response in questions_and_responses:
  
        if any(word in user_input for word in question.split()):
  
            suggestions.append((question, response))
  
    return suggestions


def chatbot_conversation():                                  # Function to start the chatbot
  
    print("Hi, I'm ChatBot. Type 'quit' to exit.")
  
    while True:
  
        user_input = input("> ").lower()
  
        if user_input == "quit":
  
            print("Bye! Have a great day.")
  
            break
  
        else:
  
            suggested_questions = suggest_questions(user_input)
  
            if suggested_questions:
  
                print("\n\nDid you mean one of these questions?\n\n")
  
                for idx, (question, _) in enumerate(suggested_questions, 1):
  
                    print(f"{idx}. {question}")
  
                chosen_question = input("Please type the number of the question you meant, or type 'none': ")

                print("\n")
  
                if chosen_question.isdigit() and int(chosen_question) <= len(suggested_questions):
  
                    _, response = suggested_questions[int(chosen_question) - 1]
  
                    print(response)

                    print("\n\n")
  
                else:
  
                    print("Sorry, I couldn't understand that. Could you please rephrase?")
  
            else:
  
                response = chatbot.respond(user_input)
  
                print(response)




if __name__ == "__main__":
    chatbot_conversation()
