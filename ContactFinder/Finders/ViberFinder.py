from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder


class ViberFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            data, result = find_only_numbers(data, FIND.KEYWORD_VIBER)
            if not correct_format:
                return result

            for ind_contact in range(len(result)):
                result[ind_contact] = correct_format_contact(result[ind_contact], CONTACT.TELEPHONE)
            return sorted(set(result))
        except:
            # print('ERROR viber')
            return []