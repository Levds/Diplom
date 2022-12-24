import pandas as pd
import datetime as dt
import snscrape.modules.twitter as sntwitter
import streamlit as st

max = 100
list = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('into:').get_items()):
    if i > max:
        break
    list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

df = pd.DataFrame(list, columns=['D/T', 'ID', 'txt', 'User'])
df.head()
df.to_csv('tweets.csv', sep=',', index=False)

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