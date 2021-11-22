import re

def delete_found_info(data, contact, keyword, position):
    if contact and keyword:
        data = __delete_found_contact_in_keyword(data, contact, keyword, position)
    else:
        data = __delete_word(data, contact+keyword)
    return data


def __delete_found_contact_in_keyword(data, contact, keyword, contact_position):
    right = 0
    if contact_position == 'after':
        right = 1
        return __data_before_and_after(data, keyword, contact, right)
    return __data_before_and_after(data, contact, keyword, right)


def __delete_word(data, word):
    return data[:data.index(word)] + ' ' + data[data.index(word) + len(word):]


def __data_before_and_after(data, start_word, end_word, position):
    try:
        if position and re.search(end_word, start_word):
            data_before = data[:data.index(start_word)+len(start_word)]
            data = data[len(data_before):]
            return data_before + ' ' + data[data.index(end_word)+len(end_word):]
    except:
        pass
    data_before_keyword = data[:data.index(start_word)+len(start_word)*position]
    data = data[data.index(start_word)+len(start_word):]
    data_after_keyword = data[data.index(end_word)+len(end_word)*position:]
    return data_before_keyword + ' ' +data_after_keyword
