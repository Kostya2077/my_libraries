from libraries.ContactScrambler.ContactScrambler import ContactScrambler
from libraries.ContactScrambler.Common.TextScrambler import TextScrambler
from libraries.ContactScrambler.Common.Constants import CONTACT


class TextContactScrambler(ContactScrambler):


    def __init__(self):
        super().__init__()


    def get_encryption_text(self, data, ENCRYPT=CONTACT.ENCRYPT):
        return TextScrambler().encrypt_data(data, ENCRYPT)
