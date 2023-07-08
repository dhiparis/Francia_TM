from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import os


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 100%, 0%)"


def create_topic_cloud(topic_labels: list[int | str], diag_file: str = '', save_path: str = '',
                       change_labels: dict[(int | str), (int | str)] = None):
    """
    Create a word-cloud based on a given path to a mallet diagnostics file.

    :param diag_file: The path to the Diagnostics file.
    :param topic_labels: The labels of the topics which should be created.
    :param save_path: The path to the folder, where the topics should be saved.
    :param change_labels: If the labels of the topic should be changed or not.
    """
    if change_labels is None:
        change_labels = {t: t for t in topic_labels}

    # Importing the mallet xml-file containing the topic information.
    xml_topics = None
    while xml_topics is None:
        name = input('Please insert the name of the mallet diagnostics-file:').strip() if diag_file == '' else diag_file
        try:
            with open(name, encoding='utf8') as f:
                xml_topics = f.read()
        except FileNotFoundError:
            print('Didn\'t found diagnostics file "%s" in the current folder.' % name)
            xml_topics = None
        except UnicodeDecodeError:
            with open(name, encoding='iso-8859-1') as f:
                print('Doesn\'t use unicode. Trying ISO-8859.')
                xml_topics = f.read()

    bs = BeautifulSoup(xml_topics, 'xml')
    topics = bs.find_all('topic')
    topic_dist = {int(i.attrs['id']): {} for i in topics}
    for t in topics:
        words = list(filter(lambda x: x != '\n', t.children))
        try:
            for w in filter(lambda x: x.text.strip() != '', words):
                attributes = w.attrs
                topic_dist[int(t.attrs['id'])].update({w.text: int(attributes['count'])})
        except AttributeError:
            print(words)
            raise AttributeError

    # Asking the user, which topic should be visualized.
    get_input = diag_file != ''
    ids = [] if topic_labels is None else topic_labels
    while not get_input:
        topic_id = input(
            'Please insert the topic-id from the topic to build the word cloud of (number, comma-seperated list of '
            'numbers, "all"): ')
        if ',' in topic_id:
            try:
                ids = list(map(lambda x: int(x.strip()), topic_id.split(',')))
                get_input = True
            except ValueError:
                print('Coudn\'t read input. Please try again')
        elif topic_id == 'all':
            ids = list(topic_dist.keys())
            get_input = True
        else:
            try:
                ids = [int(topic_id)]
                get_input = True
            except ValueError:
                print('Coudn\'t read input. Please try again')

    save_now = input('Should the topics bee saved instantly instead of shown (Y,N)?') if save_path == '' else 'Y'

    # Visualizing the topics.
    for i in ids:
        txt = ''
        topic = topic_dist[i]
        for w in topic.keys():
            for n in range(topic[w]):
                txt += w + ' '
        ############################
        #   WORDCLOUD Parameters ###
        ############################
        # Start
        wc = WordCloud(collocations=False, width=1200, height=800,
                       background_color='white', color_func=grey_color_func,
                       prefer_horizontal=1, max_words=30, relative_scaling=0.5)
        # End
        ############################
        cloud = wc.generate(txt)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')
        if save_now not in ('Y', 'y', 'yes', 'Yes'):
            plt.show()
            word_list = [{'word': i, 'n': 1} for i in txt.split()]
            print(pd.DataFrame([(w, wc.words_[w]) for w in wc.words_.keys()], columns=["word", "freq"]))
            # pd.DataFrame([(w, wc.words_[w]) for w in wc.words_.keys()],
            # columns=["word", "freq"]).to_excel('word_freq.xlsx', index=False)
        else:
            dirs = os.listdir(save_path)
            if 'vis' in dirs:
                plt.savefig(f'{save_path.strip("/")}/vis/topic_%s.png' % change_labels[i])
            else:
                plt.savefig(f'{save_path.strip("/")}/topic_%s.png' % change_labels[i])

    if save_now not in ('Y', 'y', 'yes', 'Yes'):
        print('Finished.')
    else:
        print('All wordclouds created.')
