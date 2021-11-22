import re


def find_contact(data, regex, keyword, contact_position):
    if keyword and contact_position == 'after':
        return __find_contact_after_keyword(data, keyword, regex)
    elif keyword:
        return __find_contact_before_keyword(data, keyword, regex)
    else:
        return __find_contact_without_keyword(data, regex)


def __find_contact_after_keyword(data, keyword, regex):
    data_after_keyword = data[data.index(keyword) + len(keyword):]
    regex = re.compile(regex)
    if regex.search(data_after_keyword):
        return regex.search(data_after_keyword).group(0)
    return ''


def __find_contact_before_keyword(data, keyword, regex):
    data_before_keyword = data[:data.index(keyword)]
    regex = re.compile(regex)
    found_contact = ''
    while regex.search(data_before_keyword):
        found_contact = regex.search(data_before_keyword).group(0)
        data_before_keyword = data_before_keyword[data_before_keyword.index(found_contact)+len(found_contact):]
    return found_contact


def __find_contact_without_keyword(data, regex):
    regex = re.compile(regex)
    if regex.search(data):
        return regex.search(data).group(0)
    return ''















