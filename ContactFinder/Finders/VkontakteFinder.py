from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder


def __find_contact_after_keyword(data, keyword):
    found_contact = find_contact(data, FIND.VKONTAKTE_USERNAME, keyword, WORD_POSITION.AFTER)
    if found_contact and not check_contact(data, found_contact, keyword, WORD_POSITION.AFTER, KIND_CONTACT.USERNAME):
        found_contact = ''
    return found_contact


def __find_vk_contacts(data, keyword):
    try:
        result = []
        while True:
            found_contact = __find_contact_after_keyword(data, keyword)
            if found_contact:
                data = delete_found_info(data, found_contact, keyword, WORD_POSITION.AFTER)
                result.append(found_contact)
            else:
                break
        return result
    except:
        return []


def __delete_found_info(data, contacts, keyword):
    for contact in contacts:
        data = delete_found_info(data, contact, keyword, WORD_POSITION.AFTER)
    data = delete_found_info(data, keyword, '', WORD_POSITION.NONE)
    return data


def _find_link_without_keyword(data, contacts):
    found_link = find_contact(data, FIND.VKONTAKTE_LINK, '', WORD_POSITION.NONE)
    while found_link:
        if check_contact(data, found_link, '', WORD_POSITION.NONE, KIND_CONTACT.LINK):
            contacts.append(found_link)
        data = delete_found_info(data, found_link, '', WORD_POSITION.NONE)
        found_link = find_contact(data, FIND.VKONTAKTE_LINK, '', WORD_POSITION.NONE)
    return data, contacts


def _result_of_search(data, contacts, keyword):
    result = []
    result += __find_vk_contacts(data, keyword)
    data = __delete_found_info(data, result, keyword)
    contacts += result
    return data, contacts


class VkontakteFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            result = []
            data, result = _find_link_without_keyword(data, result)
            if search_contacts:
                while find_contact(data, FIND.KEYWORD_VKONTAKTE, '', WORD_POSITION.NONE):
                    found_keyword = find_contact(data, FIND.KEYWORD_VKONTAKTE, '', WORD_POSITION.NONE)
                    if check_contact(data, found_keyword, '', WORD_POSITION.NONE, KIND_CONTACT.NONE):
                        data, result = _result_of_search(data, result, found_keyword)
                    else:
                        data = delete_found_info(data, found_keyword, '', WORD_POSITION.NONE)
            result = sorted(set(result))
            if not correct_format:
                return result
            for index_contact in range(len(result)):
                result[index_contact] = correct_format_contact(result[index_contact], KIND_CONTACT.LINK)
            return result
        except:
            # print('ERROR vk')
            return []

