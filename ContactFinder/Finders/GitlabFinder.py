from libraries.ContactFinder.Finders.AbstractFinder import AbstractFinder
from libraries.ContactFinder.Finders.Common.Functions import *


class GitlabFinder(AbstractFinder):

    def __init__(self):
        super().__init__()

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        try:
            result = []
            while find_contact(data, FIND.GITLAB_LINK, '', WORD_POSITION.NONE):
                found_contact = find_contact(data, FIND.GITLAB_LINK, '', WORD_POSITION.NONE)
                if check_contact(data, found_contact, '', WORD_POSITION.NONE, KIND_CONTACT.LINK):
                    result.append(found_contact)
                data = delete_found_info(data, found_contact, '', WORD_POSITION.NONE)
            result = sorted(set(result))
            if not correct_format:
                return result
            for index_contact in range(len(result)):
                result[index_contact] = correct_format_contact(result[index_contact], KIND_CONTACT.LINK)
            return result
        except:
            return []