from pprint import pprint
import requests

#using azure text analytic API to get the sentimental score
text_analytics_base_url =\
    "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

def get_key():
    """
    get subscription key from API_key.txt file
    """
    try:
        with open("API_key.txt", "r") as file:
            subscription_key = file.read()
            return subscription_key
    except Exception as e:
        print("Can't get subscription_key due to: "+e)
        return None

def pack_sentence_toidlist(sentences):
    """
    pack sentences to the API format
    """
    sentence_idlist = []
    for i in range(len(sentences)):
        sentence_idelement = {}
        sentence_idelement["id"] = i+1
        sentence_idelement["language"] = "en"
        sentence_idelement["text"] = sentences[i]
        sentence_idlist.append(sentence_idelement)
    #pprint(sentence_idlist)
    return sentence_idlist

def get_sentimental_score(sentences):
    """
    send sentences to API to get sentimental score
    """
    sentiment_api_url = text_analytics_base_url+"sentiment"
    documents = {'documents' : pack_sentence_toidlist(sentences)}
    #send request to API
    headers   = {"Ocp-Apim-Subscription-Key": get_key()}
    response  = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    if "errors" in sentiments:
        if sentiments["errors"] == []:
            print("get scores successfully")
        else:
            pprint(sentiments)
            exit()
    else:
        pprint(sentiments)
        exit()
    #pprint(sentiments)
    return sentiments

if __name__ == "__main__":
    test_sentences = ["Hello, this is a test message.", 
                      "Welcome to Westworld", 
                      "You are sun of a beach.",
                      "You are son of a bitch."]
    #pack_sentence_toidlist(test_sentences)
    get_sentimental_score(test_sentences)
