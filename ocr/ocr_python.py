import pdf2image
import pytesseract


def pdf_to_img(pdf_file):
    """
    Converts pdf-files into a list of images.

    :param pdf_file: The path and name of the pdf-file to convert.
    """
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(image, lang=None) -> str:
    """
    Converts the text on an image into str.

    :param image: The image file as a bitstream.
    :param lang: The language-package used. Default: None
    :return: The text of the image.
    """
    if lang is None:
        return pytesseract.image_to_string(image)
    else:
        return pytesseract.image_to_string(image, lang)


def print_pages(pdf_file, lang=None):
    """
    Prints out the text of a pdf-file in the terminal.

    :param pdf_file: The path and name of the pdf-file.
    :param lang: The language-package used for the ocr. Default: None.
    """
    for i in pdf_to_img(pdf_file):
        print(ocr_core(i, lang=lang))


def get_text(pdf_file, lang=None):
    """
    Returns the text of a pdf-file as a string.

    :param pdf_file: The path and name of the pdf-file.
    :param lang: The language-package used for the ocr. Default: None.
    """
    pdf_text = ''
    for i in pdf_to_img(pdf_file):
        pdf_text += ocr_core(i, lang=lang) + '\n\n'
    return pdf_text
