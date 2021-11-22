from libraries.ContactFinder.Finders.Common.Constants import *



class AbstractFinder:

    def __init__(self):
        pass

    def find(self, data='', correct_format=CONTACT_FORMAT.CORRECT, search_contacts=SEARCH_CONTACTS.STRICT):
        pass
