from libraries.ContactFinder.Finders.Common.Check_contact import check_contact
from libraries.ContactFinder.Finders.Common.Delete_info import delete_found_info
from libraries.ContactFinder.Finders.Common.Find_contact import find_contact
from libraries.ContactFinder.Finders.Common.Constants import FIND, WORD_POSITION, KIND_CONTACT


all_regex_keywords_for_numbers = [FIND.KEYWORD_VIBER, FIND.KEYWORD_TELEPHONE,
                                  FIND.KEYWORD_TELEGRAM, FIND.KEYWORD_WHATSAPP]


def find_only_numbers(data, main_regex_keyword):
    data, result = __find_numbers_in_keywords(data, main_regex_keyword)
    return data, result


def __find_numbers_in_keywords(data, find_main_keyword):
    result = []
    found_contacts = []
    found_keyword = find_contact(data, find_main_keyword, '', WORD_POSITION.NONE)
    while found_keyword:
        if check_contact(data, found_keyword, '', WORD_POSITION.NONE, KIND_CONTACT.NONE):
            data, found_contacts = __find_number_after_keyword(data, found_keyword)
            if not found_contacts:
                data, found_contacts = __find_number_before_keyword(data, found_keyword)
        data = delete_found_info(data, found_keyword, '', WORD_POSITION.NONE)
        found_keyword = find_contact(data, find_main_keyword, '', WORD_POSITION.NONE)
        result += found_contacts
    return data, result


def __find_number_after_keyword(data, keyword):
    try:
        result = []
        regex_telephone = FIND.TELEPHONE
        if not __check_telegram_keyword(keyword):
            regex_telephone = FIND.TELEGRAM_NUMBER
        found_number = find_contact(data, regex_telephone, keyword, WORD_POSITION.AFTER)
        while found_number:
            if check_contact(data, found_number, keyword, WORD_POSITION.AFTER, KIND_CONTACT.TELEPHONE):
                result.append(found_number)
                data = delete_found_info(data, found_number, keyword, WORD_POSITION.AFTER)
            elif not result and __check_other_keyword(data, keyword, WORD_POSITION.AFTER):
                while __check_other_keyword(data, keyword, WORD_POSITION.AFTER):
                    keyword = __add_new_keyword(data, keyword, WORD_POSITION.AFTER)
            else:
                break
            found_number = find_contact(data, regex_telephone, keyword, WORD_POSITION.AFTER)
        return data, result
    except:
        return data, []


def __find_number_before_keyword(data, keyword):
    try:
        result = []
        regex_telephone = FIND.TELEPHONE
        if not __check_telegram_keyword(keyword):
            regex_telephone = FIND.TELEGRAM_NUMBER
        found_number = find_contact(data, regex_telephone, keyword, WORD_POSITION.BEFORE)
        while found_number:
            if check_contact(data, found_number, keyword, WORD_POSITION.BEFORE, KIND_CONTACT.TELEPHONE):
                result.append(found_number)
                data = delete_found_info(data, found_number, keyword, WORD_POSITION.BEFORE)
            elif not result and __check_other_keyword(data, keyword, WORD_POSITION.BEFORE):
                while __check_other_keyword(data, keyword, WORD_POSITION.BEFORE):
                    keyword = __add_new_keyword(data, keyword, WORD_POSITION.BEFORE)
            else:
                break
            found_number = find_contact(data, regex_telephone, keyword, WORD_POSITION.BEFORE)
        return data, result
    except:
        return data, []


def __find_other_keyword(data, keyword, position):
    new_found_keyword = ''
    for regex_keyword in all_regex_keywords_for_numbers:
        new_found_keyword = find_contact(data, regex_keyword, keyword, position)
        if new_found_keyword and not check_contact(data, new_found_keyword, keyword, position, KIND_CONTACT.NONE):
            new_found_keyword = ''
        elif new_found_keyword:
            break
    return new_found_keyword


def __add_new_keyword(data, keyword, position):
    new_keyword = __find_other_keyword(data, keyword, position)
    if position == WORD_POSITION.AFTER:
        data = data[data.index(keyword)+len(keyword):]
        return keyword + data[:data.index(new_keyword)+len(new_keyword)]
    data = data[:data.index(keyword)]
    return data[data.index(new_keyword):] + keyword


def __check_other_keyword(data, keyword, position):
    new_found_keyword = __find_other_keyword(data, keyword, position)
    if new_found_keyword:
        return True
    return False


def __check_telegram_keyword(keyword):
    return not find_contact(keyword, FIND.KEYWORD_TELEGRAM, '', WORD_POSITION.NONE)
