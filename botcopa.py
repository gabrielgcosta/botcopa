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

def main():
    while True:
        auxHour = time.asctime()
        month = auxHour[4:7]
        day = auxHour[9:10]
        date1 = date(2022, int(dic[month]), int(day))
        date2 = date(2022, 11, 21)
        if numOfDays(date1, date2) > 1:
            tweet = 'Faltam '+str(numOfDays(date1, date2))+' dias para o começo da copa!'
        elif numOfDays(date1, date2) == 1:
            tweet = 'Faltam '+str(numOfDays(date1, date2))+' dia para o começo da copa!'
        elif numOfDays(date1, date2) == 0:
            tweet = 'A copa começou!'
            client.create_tweet(text = tweet)
            quit()
        client.create_tweet(text = tweet)
        time.sleep(86400)

if __name__== "__main__" :
    main()