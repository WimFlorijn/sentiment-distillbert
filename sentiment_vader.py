import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()

review_df = pd.read_csv('ALL-DATA.csv', delimiter='\t')
keywords = review_df['Review (Original)'].values

scores, compounds = [], []
keyword_count = len(keywords)
print('Determining overall sentiment.')
for i, sentence in enumerate(keywords):
    if not i % 1000:
        print('Progress: {i}/{count}'.format(i=i, count=keyword_count))

    if isinstance(sentence, str):
        compound = sid.polarity_scores(sentence)['compound']
        if compound >= .75:
            score = 'Positive'
        elif compound <= -.75:
            score = 'Negative'
        else:
            score = 'Neutral'
    else:
        score = 'Neutral'
        compound = 0

    scores.append(score)
    compounds.append(compound)

review_df['Score'] = compounds
review_df['Sentiment'] = scores

print('Writing result')
review_df.to_csv('ALL-DATA-OUT.csv', sep='\t', index=False)
