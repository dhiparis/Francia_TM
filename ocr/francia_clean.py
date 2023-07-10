import re
import pandas as pd


def replace_chars(txt: str) -> str:
    """
    Replaces the "4" in a text through à and |’ through l’
    """
    txt_list = txt.split(' ')
    text = ''
    for word in txt_list:
        if word == '4':
            text += ' à'
        elif re.search(r'\|’[A-Za-zàéáî]+', word):
            text += ' ' + word.replace('|’', 'l’')
        else:
            text += ' ' + word
    return text


def delete_page_numbers(txt: str) -> str:
    """
    Deletes the page-numbers in a text.
    """
    lines = txt.split('\n')
    text = ''
    for line in lines:
        pattern1 = r'[0-9][0-9]?[0-9]?$'
        if re.search(pattern1, line):
            line = re.sub(pattern1, '', line)
            text += '%s\n' % line
        else:
            text += '%s\n' % line
    pattern2 = r'\x0c\n\n[0-9][0-9]?[0-9]?[A-Za-z ]+\n'
    text = re.sub(pattern2, '\x0c\n', text)
    return text


def delete_multi_line(txt: str, n: int = 3) -> str:
    """
    Delete lines, which occur more than n times.
    """
    txt_list = txt.split('\n')
    df = pd.DataFrame([(line, 0) for line in filter(lambda x: x.strip() != '', txt_list)],
                      columns=['line', 'c']).groupby(by='line', as_index=False).count()
    df = df.loc[df.c > n]
    df = df['line'].tolist()
    txt_list = list(filter(lambda x: x not in df, txt_list))
    text = ''
    for line in txt_list:
        text += '%s\n' % line
    return text


def list_special_chars(txt: str) -> list:
    special_chars = []
    for t in txt:
        if not re.search(r'[A-Za-zàáâÁÀÂéèêÉÈÊìíîÍÌÎòóôÓÒÔúùûÚÙÛöäüÖÄÜẞß0-9\n\-’ —\x0c]', t):
            special_chars.append(t)
    return special_chars
