from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder
import re
error_keywords = '[iI][sS][oO]|[гГ][оО][сС][тТ][ ]?[рРpPвВ]*|[iI][dD]'
all_regex_keywords_for_numbers = [FIND.KEYWORD_VIBER, FIND.KEYWORD_TELEPHONE,
                                  FIND.KEYWORD_TELEGRAM, FIND.KEYWORD_WHATSAPP,
                                  error_keywords]


def __delete_numbers_in_others_keywords(data):
    try:
        for regex_keyword in all_regex_keywords_for_numbers:
            data, [] = find_only_numbers(data, regex_keyword)
        return data
    except:
        return data


def _find_numbers_without_keyword(data):
    try:
        data = __delete_numbers_in_others_keywords(data)
        result = []
        found_number = find_contact(data, REGEX_CONTACT.TELEPHONE, '', WORD_POSITION.NONE)
        while found_number:
            if check_contact(data, found_number, '', WORD_POSITION.NONE, KIND_CONTACT.TELEPHONE):
                result.append(found_number)
            data = delete_found_info(data, found_number, '', WORD_POSITION.NONE)
            found_number = find_contact(data, REGEX_CONTACT.TELEPHONE, '', WORD_POSITION.NONE)
        return result
    except:
        return []


class PhoneFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            data, result = find_only_numbers(data, FIND.KEYWORD_TELEPHONE)
            result += _find_numbers_without_keyword(data)
            if not correct_format:
                return result

            for ind_contact in range(len(result)):
                result[ind_contact] = correct_format_contact(result[ind_contact], CONTACT.TELEPHONE)
            return sorted(set(result))
        except:
            return []

