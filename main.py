import pandas as pd
import datetime as dt
import snscrape.modules.twitter as sntwitter
import streamlit as st
import pymongo


# client = pymongo.MongoClient("mongodb+srv://user:a3AxwHpoiKLPuTn1@cluster.rlullov.mongodb.net/?retryWrites=true&w=majority")
# db = client.tw
# coll = db.tweets
# coll.insert_many(
#     {
#     "_id" : 1,
#     "D/T" : '',
#     "ID" : '',
#     "txt" : '',
#     "User" : ''
#     }
# )

max = 100
list = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('into:christmas').get_items()):
    if i > max:
        break
    list.append([tweet.date,tweet.id,tweet.content,tweet.user.username])

df = pd.DataFrame(list, columns=['D/T', 'ID', 'txt', 'User'])
df.head()
df.to_csv('tweets.xls', sep=',', index=False)

st.title("Streamlit Twitter Scrapper")
seg = dt.date.today()
tomorrow = seg + dt.timedelta(days=1)
start = st.date_input("Start",seg)
end = st.date_input("End",tomorrow)
if start < end:
    st.success("Start: '%s'\n\nEnd: '%s'" % (start , end))
else :
    st.error('Incorrect Value: End must fall after Start')
trend = st.text_input("Enter text", "Type")

if (st.button('OK')):
    result = trend.title()
    st.success(result)