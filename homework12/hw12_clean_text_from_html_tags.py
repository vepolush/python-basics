import codecs
import re


def delete_html_tags(html_file: str, result_file:str ='cleaned.txt') -> None:
    """
    Deletes html tags and writes text left to another file
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    html_without_tags = re.sub("<[^<>]*>", '', html)

    with open(result_file, 'w') as file:
        file.write(html_without_tags)


delete_html_tags('draft.html')
