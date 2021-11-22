from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder
import re


def __find_contact_after_keyword(data, keyword):
    found_contact = find_contact(data, FIND.TELEGRAM_NUMBER, keyword, WORD_POSITION.AFTER)
    if found_contact and not check_contact(data, found_contact, keyword, WORD_POSITION.AFTER, KIND_CONTACT.TELEPHONE):
        found_contact = ''
    if not found_contact:
        found_contact = find_contact(data, FIND.TELEGRAM_USERNAME, keyword, WORD_POSITION.AFTER)
        if found_contact and not check_contact(data, found_contact, keyword, WORD_POSITION.AFTER, KIND_CONTACT.USERNAME):
            found_contact = ''
    return found_contact


def __find_contacts_after_keyword(data, keyword):
    try:
        result = []
        while True:
            found_contact = __find_contact_after_keyword(data, keyword)
            if found_contact:
                result.append(found_contact)
                data = delete_found_info(data, found_contact, keyword, WORD_POSITION.AFTER)
            else:
                break
        return result
    except:
        return []


def __find_contacts_in_keyword(data, result):
    found_keyword = find_contact(data, FIND.KEYWORD_TELEGRAM, '', WORD_POSITION.NONE)
    while found_keyword:
        if check_contact(data, found_keyword, '', WORD_POSITION.NONE, KIND_CONTACT.NONE):
            data, result = __result_of_search(data, result, found_keyword)
        else:
            data = delete_found_info(data, found_keyword, '', WORD_POSITION.NONE)
        found_keyword = find_contact(data, FIND.KEYWORD_TELEGRAM, '', WORD_POSITION.NONE)
    return data, result


def __delete_found_info(data, contacts, keyword):
    for contact in contacts:
        data = delete_found_info(data, contact, keyword, WORD_POSITION.AFTER)
    data = delete_found_info(data, keyword, '', WORD_POSITION.NONE)
    return data


def __find_link_without_keyword(data, contacts):
    found_link = find_contact(data, FIND.TELEGRAM_LINK, '', WORD_POSITION.NONE)
    while found_link:
        if check_contact(data, found_link, '', WORD_POSITION.NONE, KIND_CONTACT.LINK):
            contacts.append(found_link)
        data = delete_found_info(data, found_link, '', WORD_POSITION.NONE)
        found_link = find_contact(data, FIND.TELEGRAM_LINK, '', WORD_POSITION.NONE)
    return data, contacts


def __result_of_search(data, contacts, keyword):
    result = __find_contacts_after_keyword(data, keyword)
    data = __delete_found_info(data, result, keyword)
    contacts += result
    return data, contacts


def __delete_inaccurate_contacts(contacts):
    result = []
    for contact in contacts:
        if re.search(FIND.TELEGRAM_LINK, contact):
            result.append(contact)
        elif re.search(FIND.TELEGRAM_NUMBER, contact):
            if contact == re.search(FIND.TELEGRAM_NUMBER, contact).group(0):
                result.append(contact)
    return result


def _find_telegram_contacts(data, search_contacts):
    result = []
    data_for_only_numbers = data
    data, result = __find_link_without_keyword(data, result)
    data, result = __find_contacts_in_keyword(data, result)
    if not search_contacts:
        result = __delete_inaccurate_contacts(result)
    data_for_only_numbers, found_numbers = find_only_numbers(data_for_only_numbers, FIND.KEYWORD_TELEGRAM)
    result += found_numbers
    return result


class TelegramFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            result = _find_telegram_contacts(data, search_contacts)
            if not correct_format:
                return result

            for ind_contact in range(len(result)):
                result[ind_contact] = correct_format_contact(result[ind_contact], CONTACT.TELEGRAM)
            return sorted(set(result))
        except:
            return []
