import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import sys

################################################
#   Standard workflow for importing the data   #
################################################
sns.set_theme(style="whitegrid")
df = None
name = ""
while df is None:
    name = input('Please insert the name (and path) of the mallet topic-doc-distribution file: ')
    name = name.strip()
    try:
        df = pd.read_csv(name, sep='\t', encoding='utf8', header=None)
    except FileNotFoundError:
        print('No File with name "%s" in the current folder' % name)
        df = None

n_topics = len(df.columns) - 2
df.columns = ['id', 'dokument'] + ['Topic %s' % i for i in range(n_topics)]
# Extracting the information about the years.
years = []
data_topics = pd.DataFrame(df)
correlation_type = input('Do you want to visualize the correlations over time? (Else over documents) - Y/N: ')
if correlation_type in ('Y', 'y', 'yes', 'Yes'):
    for d in df["dokument"]:
        try:
            volume = re.findall(r'[0-9][0-9]?-?[0-9]?_', d)[0]
            volume = volume.split('_')[0]
            volume = int(volume) if '-' not in volume else int(volume.split('-')[0])
        except IndexError:
            print('\n\tCould not parse document-name: "%s".\n' % d)
            sys.exit("Please check %s file for wrong document names." % name)

        year = 1972 + volume
        if year >= 1988:
            year += 1
        years.append(year)
    df['year'] = years
    df = df[['id', 'year',
             'dokument'] + ['Topic %s' % i for i in range(len(df.columns) - 3)]].sort_values(by=['year', 'dokument'])
    df.pop('dokument')
    df.pop('id')
    df = df.groupby(by='year', as_index=False).mean()
    df.pop('year')
    print(df)

    ##########################################
    #   Calculating the topic-correlations   #
    ##########################################

    topic_corr = np.corrcoef([df[t] for t in list(df)])

    print(pd.DataFrame(topic_corr))

    plt.rcParams["figure.figsize"] = (12, 12)
    sns.heatmap(pd.DataFrame(topic_corr), xticklabels=True, vmin=-1, vmax=1, yticklabels=True)
    plt.show()

    inp = input('Do you want to visualize certain correlations? (y, n)')
    while inp not in ('N', 'n'):
        x = int(input('Please insert the number of the topic for the x-axe: '))
        y = int(input('Please insert the number of the topic for the y-axe: '))
        sns.scatterplot(x=df['Topic %i' % x], y=df['Topic %i' % y])

        f = lambda z: (z * topic_corr[x][y]) + (0 if topic_corr[x][y] >= 0 else (topic_corr[x][y] * -1) / 2)
        step = 0.01
        rng = [i * step for i in range(int(max(df['Topic %i' % x]) / step))]
        sns.lineplot(x=rng, y=list(map(f, rng)), label='correlation=%s' % topic_corr[x][y])
        plt.xlabel('Topic %i' % x)
        plt.ylabel('Topic %i' % y)
        print(topic_corr[x][y])
        plt.legend()
        plt.show()
        inp = input('Do you want to visualize more correlations? (y, n)')

else:
    doc_topic_dist = {}
    for _, v in data_topics.iterrows():
        doc_topic_dist[v['dokument'].split('/')[-1]] = {i: v[i] for i in list(filter(lambda z: z not in ('dokument',
                                                                                                         'id'),
                                                                                     list(data_topics)))}

    doc_topic_dist = pd.DataFrame(doc_topic_dist)

    doc_topic_correlation = pd.DataFrame(np.corrcoef(doc_topic_dist))
    topic_combinations = []
    exist = []
    for i, v in doc_topic_correlation.iterrows():
        for j in list(doc_topic_correlation):
            if i != j and ('%s-%s' % (i, j) if i < j else '%s-%s' % (j, i)) not in exist:
                topic_combinations.append({'1-Topic': i, '2-Topic': j, 'corr': v[j]})
                exist.append(('%s-%s' % (i, j)) if i < j else ('%s-%s' % (j, i)))
            else:
                continue
    correlation_list = pd.DataFrame(topic_combinations).sort_values(by='corr', ascending=False)
    correlation_list.to_excel('./document-topic-correlation.xlsx',
                              index=False)
    doc_topic_dist = doc_topic_dist.T
