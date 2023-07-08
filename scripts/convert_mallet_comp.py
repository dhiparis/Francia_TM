from datetime import date
import pandas as pd
import re
import sys


TODAY = date.today()
# Converting the tsv-file to excel.


# Reading the path of the file.
def read_topic_doc_distribution_file(file_path: str = ''):
    """
    Reads the mallet-comp file --> the topic-doc-distribution file. Which is marked as txt, but actually is a tsv file.
    It returns the content of the file as a pandas DataFrame.

    :param file_path: The path to the mallet.comp.txt file.
    :return: The document topic distribution as a pandas-Dataframe.
    """
    data = None
    name = ""
    while data is None:
        name_input = input('Please insert the name (and path) of'
                           'the mallet topic-doc-distribution file: ') if file_path == '' else file_path
        name = name_input
        try:
            data = pd.read_csv(name, sep='\t', encoding='utf8', header=None)
        except FileNotFoundError:
            print('No File with name "%s" in the current folder' % name)
            data = None

    data.columns = ['id', 'dokument'] + ['Topic %s' % i for i in range(len(data.columns)-2)]
    # Extracting the information about the years.
    years = []
    for d in data["dokument"]:
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
    data['year'] = years
    n_topics = len(data.columns)-3
    data = data[['id', 'year', 'dokument'] + ['Topic %s' % i for i in range(n_topics)]].sort_values(by=['year',
                                                                                                        'dokument'])
    # updating the document names.
    documents = []
    for _, v in data.iterrows():
        documents.append(v['dokument'].split('/')[-1])
    data["dokument"] = documents
    return data


# dirs = os.listdir()
# path = 'tables/' if 'tables' in dirs else ''
# df = read_topic_doc_distribution_file()
# df.to_excel('%s_document_topic_dist_%s.xlsx' % (path + str(TODAY), (df.shape[1]-3)), index=False)

# print('Created table "%s_document_topic_dist_%s.xlsx".' % (str(TODAY), (df.shape[1]-3)))


############################################################
#   Creating the Table with the year-topic-distribution.   #
############################################################
def create_year_topic_dist(topic_doc_dist_file: str = '', export_path: str = ''):
    """
    Creates the Excel file including the year-topic-distribution.

    :param topic_doc_dist_file: The path to the comp-file.
    :param export_path: The path where to export the created file.
    """
    topic_doc_dist = read_topic_doc_distribution_file(topic_doc_dist_file)
    year_topic_dist = pd.DataFrame(topic_doc_dist)
    year_topic_dist.pop('dokument')
    year_topic_dist.pop('id')
    year_topic_dist = year_topic_dist.groupby(by='year', as_index=False).mean()
    print(year_topic_dist)
    year_topic_dist.to_excel('%s_year_topic_distribution_%s.xlsx' % (export_path + str(TODAY),
                                                                     (year_topic_dist.shape[1]-1)),
                             index=False)
    print('Created table "%s_year_topic_distribution_%s.xlsx".' % (TODAY, (year_topic_dist.shape[1]-1)))


# create_year_topic_dist()


def get_n_topics(topic_doc_dist: pd.DataFrame) -> int:
    """
    Calculates the number of topics based on the topic_doc_dist Dataframe.

    :param topic_doc_dist: The topic-document-distribution as a pandas-Dataframe.
    :return: The number of topics as an integer-value.
    """
    return topic_doc_dist.shape[0] - 3
