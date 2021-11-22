from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder
import re


def check_email(contact):
    return re.search('[a-z]', contact) and re.search('[а-я]',contact)


class EmailFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            result = []
            while find_contact(data, FIND.EMAIL, '', WORD_POSITION.NONE):
                found_email = find_contact(data, FIND.EMAIL, '', WORD_POSITION.NONE)
                if check_contact(data, found_email, '', WORD_POSITION.NONE, KIND_CONTACT.EMAIL):
                    if not found_email.count('..'):
                        if search_contacts:
                            result.append(found_email)
                        elif not check_email(found_email):
                            result.append(found_email)
                data = delete_found_info(data, found_email, '', WORD_POSITION.NONE)
            if not correct_format:
                return result
            for index_contact in range(len(result)):
                contact = result[index_contact]
                if re.search(FIND.EMAIL, contact) and contact == re.search(FIND.EMAIL, contact).group(0):
                    result[index_contact] = correct_format_contact(result[index_contact], KIND_CONTACT.EMAIL)
                else:
                    result[index_contact] = correct_format_contact(result[index_contact], KIND_CONTACT.LINK)
            return result
        except:
            # print('ERROR email')
            return []
