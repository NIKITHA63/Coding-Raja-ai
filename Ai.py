from textblob import TextBlob

def analyze_sentiment(text):
   
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def chatbot_response(user_message):
    sentiment = analyze_sentiment(user_message)
    if sentiment == "positive":
        return "I'm glad you're feeling good! Is there anything specific you'd like to talk about?"
    elif sentiment == "negative":
        return "I'm sorry to hear that. Can I help you with anything?"
    else:
        return "I'm here to help. What can I do for you?"



user_message = str(input())
print(chatbot_response(user_message))
