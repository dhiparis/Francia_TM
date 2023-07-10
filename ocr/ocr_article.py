from ocr_python import *
import os


directory = os.listdir()
pdf_file = 'none'
lang = ''
while pdf_file not in directory and lang not in ('deu', 'fra', 'en'):
    pdf_file = input('Insert the name of the pdf file: ')
    lang = input('Insert language (deu, fra, eng): ')
txt = get_text(pdf_file, lang=lang)
with open(pdf_file.replace('.pdf', '.txt'), 'w', encoding='utf8') as f:
    f.write(txt)
print('Saved text in %s' % pdf_file.replace('.pdf', '.txt'))
