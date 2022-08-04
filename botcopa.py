import tweepy
import time
from datetime import date

api_key = 'In0O6T3hakRxaWlSYkLRG4cY9'
api_secret_key = '1pYnHiqNFNXwDGwKXOZO9zLBaIn3XMlMLLgFMkibDZvDdzd39W'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEATfgEAAAAALA7tyhnnc1B7e%2F1MFzEcpoaHVYo%3DEW7Gm4cGojQtu9hwmY0FzShIU5zfeF4QU7rRP7IsbEmbi4U1X2'
acess_key = '1554477824559415296-x5YaCSYbRO5gdmu7Q6pdJnI3eqN1z4'
acess_secret = '0Nmuh5PcZVFQFa31qCQd0RU5jpIIgALAVRwrjMMmAFaaP'
 

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret_key,
    access_token=acess_key,
    access_token_secret=acess_secret
)

def numOfDays(date1, date2):
    return (date2-date1).days

dic = {'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
i=0
rodou = False
while True:
    auxHour = time.asctime()
    hour = auxHour[len(auxHour)-13:len(auxHour)-8]
    if str(hour) == '08:00' or rodou == True:
        rodou = True
        month = auxHour[4:7]
        day = auxHour[9:10]
        arquivo = open("tweets.txt", "a")
        date1 = date(2022, int(dic[month]), int(day))
        date2 = date(2022, 11, 21)
        if numOfDays(date1, date2) > 1:
            tweet = 'Faltam '+str(numOfDays(date1, date2))+' dias para a copa!'
        elif numOfDays(date1, date2) == 1:
            tweet = 'Faltam '+str(numOfDays(date1, date2))+' dia para a copa!'
        elif numOfDays(date1, date2) == 0:
            tweet = 'A copa começou!'
            client.create_tweet(text = tweet)
            quit()
        client.create_tweet(text = tweet)
        print(tweet)
        time.sleep(86400)