import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

COLORS = ['blue', 'green', 'orange', 'red', 'yellow', 'pink', 'violett']


def visualize_data(data: pd.DataFrame, x: str, y: (str | list[str]), group: str | None = '', x_label: str = '',
                   y_label: str = '', x_tics: (list | tuple) = (1973, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010,
                                                                2015, 2020),
                   title: str = '', y_tics: list = None, x_size: int = 16, y_size: int = 7, smooth_y: int = 1,
                   group_func: str = 'count', relative: bool = False, save: bool = False, set_null_values: bool = True,
                   show_title: bool = True, percent: bool = True, font_size: int = 16,
                   colors: bool = False, linewidth: int = 2, trend_line: bool = False,
                   thumbnail: bool = False, save_path: str = '../05_visualisierungen/abbildungen') -> pd.DataFrame:
    """
    The function visualize_data visualizes the content of pandas Dataframe in a seaborn plot. It is specifically
    designed for visualizing the metadata of the Francia-articles, but can be further used in other contexts.

    :param data: The Dataframe containing the information to plot.
    :param x: The label of the column for x-axe.
    :param y: The label of the column of th y-axe. Or a list of labels.
    :param group: The label of the column after which the values shall be grouped. Default empty-string.
    :param x_tics: The labels for the x-axe. Default: (1973, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020,
    2025)
    :param y_tics: The labels for ty y-axe. Default: None.
    :param x_size: The width of the diagram.
    :param y_size: The height of the diagram.
    :param x_label: The label of the x-axe. Default: the value of x
    :param y_label: The label of the y-axe. Default: the value of y.
    :param title: The titel of the plot. Default: ''
    :param smooth_y: The value of the range for smoothing thy y-values. Default: 1 ==> No smoothing
    :param group_func: The function after which the data shall be grouped, if empty the data will not be grouped.
    :param relative: If true the function will calculate the relative amount per x, if false it will use the absolute
    numbers. Default: False
    :param save: Whether to save the plot or not.
    :param set_null_values: If this values is set to true, all not existing values in a group of values will be created
    and set to zero.
    :param show_title: Whether a titel should be shown on top of the plot.
    :param percent: Only used, if relative is true. If True, the values will be shown in percent.
    :param font_size: The size of the font for the axe-labels.
    :param colors: If the lines should be separable by colors and not by line-type.
    :param linewidth: The width of the lines to plot.
    :param trend_line: Whether a trend_line should be included or not. Can only be shown if group is empty and colors
    are False. Default: False
    :param thumbnail: If the plot should be shown as a thumbnail -> no ax-labels, white background and as a square.
    :param save_path: The path, where to save the topics.
    :return: The Dataframe which was plotted.
    """
    def create_plot(dataframe: pd.DataFrame, x_axe: str, y_axe: str, group_val: str = None, l_style: str = None,
                    line_label: str = None, is_trend: bool = False):
        if not colors:
            """if x in ('year', 'Jahr', 'jahr', 'Year'):
                sns.lineplot(data=dataframe.loc[dataframe[x_axe] < 1988], x=x_axe, y=y_axe, style=group_val,
                             color='black', linewidth=linewidth, linestyle=l_style, label=line_label)
                sns.lineplot(data=dataframe.loc[dataframe[x_axe] > 1988], x=x_axe, y=y_axe, style=group_val,
                             color='black', linewidth=linewidth, linestyle=l_style)
            else:"""
            graph = sns.lineplot(data=dataframe, x=x_axe, y=y_axe, style=group_val, linewidth=linewidth,
                                 linestyle=l_style, label=line_label, color='black' if not is_trend else 'grey')
        else:
            """if x in ('year', 'Jahr', 'jahr', 'Year'):
                sns.set_palette(sns.color_palette("tab10"))
                sns.lineplot(data=dataframe.loc[dataframe[x_axe] < 1988], x=x_axe, y=y_axe, hue=group_val,
                             linewidth=linewidth, label=line_label)
                sns.set_palette(sns.color_palette("tab10"))
                sns.lineplot(data=dataframe.loc[dataframe[x_axe] > 1988], x=x_axe, y=y_axe, hue=group_val,
                             linewidth=linewidth)
            else:"""
            graph = sns.lineplot(data=dataframe, x=x_axe, y=y_axe, hue=group_val, linewidth=linewidth, label=line_label)
        return graph

    data = pd.DataFrame(data)
    if type(y) is list and group != '':
        raise ValueError('You can\'t use a list of y-labels and a grouping function!')
    if type(y) is not list:
        if group_func != '':
            group_by = [x] if group == '' or group is None else [x, group]
            if group_func == 'sum':
                data = data.groupby(by=group_by, as_index=False).sum(True)[group_by + [y]]
            elif group_func == 'mean':
                data = data.groupby(by=group_by, as_index=False).mean(True)[group_by + [y]]
            elif group_func == 'count':
                data = data.groupby(by=group_by, as_index=False).count()[group_by + [y]]
            if set_null_values and group != '' and group is not None:
                add_values = []
                for x_value in set(data[x].to_list()):
                    t = data.loc[data[x] == x_value]
                    for g in set(data[group].to_list()):
                        if g not in set(t[group].to_list()):
                            add_values.append({x: x_value, group: g, y: 0})
                data = pd.concat([data, pd.DataFrame(add_values)])

        if smooth_y > 1:
            data = smooth_df(data, smooth_value=y, group_value=group, sort_by=x, smooth_over=smooth_y)
        # Main visualisation
        if not thumbnail:
            sns.set_style('whitegrid')
            plt.rcParams["figure.figsize"] = (x_size, y_size)
        else:
            sns.set_style('white')
            square_size = 0.1
            plt.rcParams["figure.figsize"] = (square_size, square_size)

        # data[group] = list(map(lambda z: z.upper(), data[group].to_list()))
        data = data.sort_values(by=[group, x] if group != '' and group is not None else [x])
        if relative:
            data_dict = [{i: v[i] for i in list(data)} for _, v in data.iterrows()]
            data = [{i: v[i] for i in list(data)} for _, v in data.iterrows()]
            for d in data:
                d[y] = d[y]/np.sum(list(map(
                    lambda zz: zz[y],
                    list(filter(lambda z: z[x] == d[x],
                                data_dict))
                )))
            data = pd.DataFrame(data)
            if percent:
                data[y] = list(map(lambda z: z*100, data[y]))
    else:
        for label in y:
            data[label] = smooth_list(data[label], smooth_y)
            if percent:
                data[label] = list(map(lambda z: z*100, data[label]))
    plt.rcParams['font.size'] = font_size
    if font_size > 14:
        plt.xticks(rotation=35)
    plot = None
    if type(y) is not list:
        plot = create_plot(data, x, y, group if group != '' and group is not None else None)
        if group != '' and group is not None:
            handlers, labels = plot.get_legend_handles_labels()
            print(labels)
            if len(labels) > 2 and labels[0] == 'FNZ':
                labels[0], labels[2], labels[1] = labels[2], labels[1], labels[0]
                handlers[0], handlers[2], handlers[1] = handlers[2], handlers[1], handlers[0]
            if len(labels) > 2 and labels[1] == 'Englisch':
                labels[1], labels[2] = labels[2], labels[1]
                handlers[1], handlers[2] = handlers[2], handlers[1]
            print(labels)
            plt.legend(handles=handlers, labels=labels, title=f'{group[0].upper()}{group[1:]}')

    else:
        line_styles = ('-', '--', '-.', ':', '--..')
        c = 0
        for label in y:
            if c >= len(line_styles):
                raise ValueError('Not enough line-styles available.')
            plot = create_plot(data, x, label, l_style=line_styles[c], line_label=label)
            c += 1
        c = 0
        if trend_line:
            for label in y:
                data[label] = smooth_list(data[label], smooth_y+18)
            for label in y:
                plot = create_plot(data, x, label, l_style=line_styles[c], line_label=None,
                                   is_trend=True)
                c += 1
    # plt.legend(title=f'{group[0].upper()}{group[1:]}')

    if x_tics is not None and not thumbnail:
        plt.xticks(x_tics)
    if y_tics is not None and not thumbnail:
        plt.yticks(y_tics)
    if show_title and not thumbnail:
        plt.title(title)
    if x_label != '' and not thumbnail:
        plt.xlabel(x_label)
    if y_label != '' and not thumbnail:
        plt.ylabel(y_label)
    if thumbnail:
        sns.despine()
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('')
        plt.ylabel('')
        plt.title('')
        plot.get_legend().remove()
    if save:

        plt.savefig(f'{save_path}/%s.png' % title.replace(' ', '_'), dpi=300)
    plt.show()
    return data


def smooth_df(df: pd.DataFrame, smooth_value: str, group_value: str, sort_by: str,
              smooth_over: int = 3) -> pd.DataFrame:
    """
    Smooth a list of values in a dataframe which are grouped by another column.

    :param df: The dataframe containing the values.
    :param smooth_value: The value, which shall be smoothed.
    :param group_value: The value after which the smoothed values shall be grouped.
    :param sort_by: The value for the x-label, aka the value to sort the data later.
    :param smooth_over: The range over which the values shall be smoothed.
    :return: The same dataframe with smoothed values.
    """
    if group_value == '':
        df[smooth_value] = smooth_list(df[smooth_value].to_list(), smooth_over=smooth_over)
        return df

    value_list = {}
    for v in set(df[group_value].to_list()):
        value_list[v] = pd.DataFrame([{i: v[i] for i in list(df)} for _, v in df.loc[df[group_value] == v].iterrows()]).sort_values(sort_by)
        value_list[v][smooth_value] = smooth_list(value_list[v][smooth_value].to_list(), smooth_over)
    new_dataframe = []
    for k in value_list.keys():
        for _, v in value_list[k].iterrows():
            new_dataframe.append({i: v[i] for i in list(value_list[k])})
    return pd.DataFrame(new_dataframe).sort_values(by=[sort_by, group_value, smooth_value])


def smooth_list(p_list: list[(int, float)], smooth_over: int) -> list[float]:
    """
    This function smooths integer or float values a long a list.

    :param p_list: The list containing the values
    :param smooth_over: The range over which the values shall be smoothed.
    :return: The list in the exact order with smoothed values.
    """
    if len(p_list) < smooth_over:
        return p_list
    smoothed_list = [i for i in p_list]
    for i in range(len(p_list)):
        s = i - int(smooth_over/2)
        e = i + int(smooth_over/2)
        tmp = [p_list[j] for j in range(s if s >= 0 else 0,
                                        e + 1 if e < len(p_list) else len(p_list))]
        smoothed_list[i] = np.mean(tmp)
    return smoothed_list
