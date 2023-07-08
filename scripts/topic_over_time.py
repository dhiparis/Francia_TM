import pandas
from seaborn import set_theme
from convert_mallet_comp import get_n_topics
from plot_vis import visualize_data


def visualize_topic_over_time(topic_doc_dist: pandas.DataFrame, topic_ids: list[(int | str)] = None, smooth: int = 0,
                              use_plot_vis: bool = True, trend_line: bool = False, save_fig: bool = False,
                              thumbnail: bool = False):
    """
    Creates plots for the visualisation of the topics over the years based on the topic-document-distribution.
    :param topic_doc_dist: The topic-document-distribution as a pandas-DataFrame.
    :param topic_ids: The list of topics, which shall be shown
    :param smooth: The value to smooth over
    :param use_plot_vis: Whether to use the visualisation-functions of plot-vis or not.
    :param trend_line: Whether to include a trend-line into the plot or not.
    :param save_fig: If the plot should be saved instantly. Default: False
    :param thumbnail: If the graphic should be shown as a thumbnails for tables.
    """
    set_theme(style="whitegrid")

    df = topic_doc_dist
    n_topics = get_n_topics(df)
    #######################################
    #   Visualizing topic(s) over years   #
    #######################################
    tm_list = -1 if topic_ids is None else topic_ids
    while type(tm_list) is not list:
        tm_list = input('Please insert the topic numbers, of the topics to visualize(number or comma seperated): ')
        if ',' in tm_list:
            tm_list = list(map(lambda x: x.strip(), tm_list.split(',')))
        else:
            tm_list = [tm_list]
        try:
            tm_list = [int(i) for i in tm_list]
            tm_list = list(filter(lambda x: 0 <= x < n_topics, tm_list))
        except ValueError:
            print('Only numbers allowed!')
            tm_list = -1

    tm_list = list(set(tm_list))
    tm_list = ['Topic %i' % i for i in tm_list] if type(tm_list[0]) is int else tm_list
    smooth_value = smooth
    topic_year = df.groupby(by='year',
                            as_index=False).mean(numeric_only=True)[['year'] + tm_list]

    tp_list = ''
    for t in tm_list:
        tp_list += t + ', '
    print(visualize_data(topic_year, x='year', y=tm_list, y_label='Topic Anteil %',
                         x_label='Jahre',
                         title=f'Topics_over_time-{tp_list}', smooth_y=smooth_value, colors=False,
                         trend_line=trend_line, show_title=False, save=save_fig, thumbnail=thumbnail,
                         save_path='../05_visualisierungen/topic_models/' + '/thumbnails' if thumbnail else '')
          )

# visualize_topic_over_time(topic_doc_dist=read_topic_doc_distribution_file())
