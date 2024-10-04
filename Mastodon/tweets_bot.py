from mastodon import Mastodon, StreamListener
from sys import exit
import re
from google_trans_new import google_translator
import requests
from Scweet.scweet import scrape

languagedic = {}

#stream = StreamListener()
trans = google_translator()

class Bot(StreamListener):

    def __init__(self):
        super(Bot, self).__init__() #将实例对象转为父类对象，但貌似这里不写也可以
        self.transm = False

    def on_update(self, status):
        #print('调用on_updata')
        #print(status)
        global language
        language = status['language']
        languagedic['language'] = language
        #print(language)
        content = status['content']
        user_id = status['account']["acct"]
        #print(userid)
        atid = self.find(content)[0]
        #atid2 = self.find(content)[1]
        attext = self.find(content)[1]
        attextl = attext.split(' ')
        bot_mod = attextl[0]
        account_id = attextl[1]
        since_time = attextl[2]
        transc = attextl[3]

        if atid == '@Tweets_bot' and bot_mod == '-uid':
            #transc = attextl[3]
            if transc == 'N':
                self.transm = False
                all_tweets = self.getTweets(since_time, account_id)
                #print(all_tweets)
                try:
                    for tweet in all_tweets:
                        #print(tweet)
                        tweet_id = tweet['id']
                        tweet_text = tweet['text']
                        tweet_time = tweet['time']
                        toott = self.toot_the_tweet(user_id, tweet_id, tweet_text, tweet_time)
                        print(toott)

                except TypeError:
                    print("请检查输入值是否正确, 或指定用户在该时间段并未发表推文。")
                    content = ''
                    #exit(0)

            elif transc == 'Y':
                #global transm
                self.transm = True
                all_tweets = self.getTweets(since_time, account_id)
                #print(all_tweets)
                try:
                    for tweet in all_tweets:
                        #print(tweet)
                        tweet_id = tweet['id']
                        tweet_text = tweet['trans']
                        tweet_time = tweet['time']
                        #tweet_trans = tweet['trans']
                        toott = self.toot_the_tweet(user_id, tweet_id, tweet_text, tweet_time)
                        print(toott)
                except TypeError:
                    print("请检查输入值是否正确, 或指定用户在该时间段并未发表推文。")
                    content = ''

        elif atid == '@Tweets_bot' and bot_mod == '-tag':
            if transc == 'N':
                pass
            elif transc == 'Y':
                pass

        elif atid == '@Tweets_bot' and bot_mod == '-word':
            pass
        #elif atid == '@Tweets_bot' and bot_mod == '-uid':
            #pass

        else:
            content = ''

    def getTweets(self, since_time, account_id):
        all_tweets = []
        data = scrape(since = since_time, from_account = account_id, interval = 1)
        #print(data)
        tweet_id = data['UserName']
        #print(tweet_id)
        tweet_text = data['Embedded_text']
        tweet_time = data['Timestamp']
        trans_text = []
        #print(self.transm)
        if self.transm == True:
            for content in tweet_text:
                #print(content)
                trans_cont = self.tran(content, languagedic['language'])
                trans_text.append(trans_cont)
                #print(trans_text)
            for id,text,time,trans in zip(tweet_id, tweet_text, tweet_time,  trans_text):
                all_tweets.append({"id": id, "text": text, "time": time, "trans": trans})
        if self.transm == False:
            for id,text,time in zip(tweet_id, tweet_text, tweet_time):
                all_tweets.append({"id": id, "text": text, "time": time})

                #print(all_tweets)
        return(
        all_tweets
        if len(all_tweets) > 0
        else None)


    def toot_the_tweet(self, user_id, tweet_id, tweet_text, tweet_time, trans_text = None):


        host_instance = 'https://ahec.world'
        token = 'locf3DeHJAwhQ8Yi3jLd3O6LMEJTYPYIBJFGe-gA7l4'

        headers = {}
        headers['Authorization'] = 'Bearer ' + token

        data = {}

        data['status'] = '@' + user_id + '\nFrom twitter ID: ' + tweet_id + '\n' + tweet_text + '\n发布时间: ' + tweet_time
        data['visibility'] = 'direct'

        response = requests.post(
        url=host_instance + '/api/v1/statuses', data=data, headers=headers)

        if response.status_code == 200:

            return True

        else:
            print(response.text)
            return False

    def find(self,content):
        atidlist = re.findall(r'https://ahec.world/(.+?)"',content)
        atid1 = atidlist[0]
        #atid2 = atidlist[1]
        attext = ''.join(text for text in re.findall(r'> (.+?)</p>', content))
        #text = ''.join(text for text in re.findall(r'>(.+?)</p>', content))
        return atid1, attext


    def tran(self, content, language):
        trans_cont = trans.translate(content, lang_tgt=language)
        return trans_cont

def Login():
    mastodon = Mastodon(
            #client_id = 'client.secret',
            access_token = 'locf3DeHJAwhQ8Yi3jLd3O6LMEJTYPYIBJFGe-gA7l4',
            api_base_url = "https://ahec.world"
            )
    return mastodon

def LTLlisten(mastodon):
    bot = Bot() #创建类Bot()的实例bot
    mastodon.stream_local(bot) #stream_local会自动调用实例bot中的on_update
    #mastodon.stream_direct(bot) #stream_direct会自动调用实例bot中的on_conversation

mastodon = Login() #先登录
LTLlisten(mastodon) #然后将登录数据传入LTLlisten
