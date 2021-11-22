from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder


def __find_contacts_before_keyword(data, keyword):
    result = []
    while True:
        found_contact = find_contact(data, FIND.ICQ, keyword, WORD_POSITION.AFTER)
        if found_contact and check_contact(data, found_contact, keyword, WORD_POSITION.AFTER, KIND_CONTACT.ICQ):
            result.append(found_contact)
            data = delete_found_info(data, found_contact, keyword, WORD_POSITION.AFTER)
        else:
            break
    return result


def __find_contacts_after_keyword(data, keyword):
    result = []
    while True:
        found_contact = find_contact(data, FIND.ICQ, keyword, WORD_POSITION.AFTER)
        if found_contact and check_contact(data, found_contact, keyword, WORD_POSITION.AFTER, KIND_CONTACT.ICQ):
            result.append(found_contact)
            data = delete_found_info(data, found_contact, keyword, WORD_POSITION.AFTER)
        else:
            break
    return result


def __delete_found_info(data, contacts, keyword):
    for contact in contacts:
        data = delete_found_info(data, contact, '', WORD_POSITION.NONE)
    data = delete_found_info(data, keyword, '', WORD_POSITION.NONE)
    return data


def _find_icq_numbers(data, contacts, keyword):
    result = __find_contacts_after_keyword(data, keyword)
    if not result:
        result = __find_contacts_before_keyword(data, keyword)
    data = __delete_found_info(data, result, keyword)
    contacts+=result
    return data, contacts


class IcqFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            result = []
            found_keyword = find_contact(data, FIND.KEYWORD_ICQ, '', WORD_POSITION.NONE)
            while found_keyword:
                if check_contact(data, found_keyword, '', WORD_POSITION.NONE, KIND_CONTACT.NONE):
                    data, result = _find_icq_numbers(data, result, found_keyword)
                else:
                    data = delete_found_info(data, found_keyword, '', WORD_POSITION.NONE)
                found_keyword = find_contact(data, FIND.KEYWORD_ICQ, '', WORD_POSITION.NONE)
            result = sorted(set(result))
            if not correct_format:
                return result
            for index_contact in range(len(result)):
                result[index_contact] = correct_format_contact(result[index_contact], KIND_CONTACT.ICQ)
            return result
        except:
            # print('ERROR icq')
            return []



