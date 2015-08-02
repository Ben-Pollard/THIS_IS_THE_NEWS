# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:54:21 2015

@author: user

Get top 5 articles from BBC top stories
"""
import feedparser
from bs4 import BeautifulSoup
import urllib2
import time

#get feed data
d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
summaries = [{'title':entry['title'], 'summary':entry['summary_detail']['value'], 'link':entry['link']} for entry in d['entries']]

#get first n
summaries = summaries[0:5]

#extract news from links
def output_if_text(t):
    if t.attrs=={}:
        return t.text
    else: return ''

for summary in summaries:
    time.sleep(2)
    print summary['title']
    soup = BeautifulSoup(urllib2.urlopen(summary['link']).read()) #download and make soup
    summary['article']=''.join(map(output_if_text,soup.find_all('p'))) # extract all paragraphs with no additional attributes
    summary['article'] = summary['article'].replace('\t',' ').replace('\n',' ') # remove newlines and whitespace
    

#output
with open('/home/user/Projects/THIS_IS_THE_NEWS/articles.txt','w+') as f:
    for summary in summaries:
        print summary['title']
        f.write(summary['title'] + '\t' + summary['title'] + ' ' + summary['summary'] + ' ' + summary['article'])
