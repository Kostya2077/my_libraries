from libraries.ContactFinder.Finders.Common.Constants import FIND
import re


def correct_format_contact(contact, kind_contact):
    if kind_contact == 'telephone':
        contact = __correct_telephone(contact)
    elif kind_contact == 'icq':
        contact = __correct_icq(contact)
    elif kind_contact == 'link':
        contact = __correct_link(contact)
    elif kind_contact == 'telegram':
        contact = __correct_telegram(contact)
    contact = contact.replace(' ', '')
    return contact



def __correct_telephone(contact):
    if re.search('[+][ ]?7', contact):
        REPLACE = re.search('\+[ ]?7', contact).group(0)
        contact = contact.replace(REPLACE, '8')
    return ''.join(re.findall('\d+', contact))

def __correct_icq(contact):
    return ''.join(re.findall('\d+', contact))

def __correct_link(contact):
    if not re.search('http[s]://', contact):
        if re.search('/resumes[?]skills%', contact):
            contact = 'career.habr.com' + contact
        contact = 'https://' + contact
    return contact

def __correct_telegram(contact):
    if re.search(FIND.TELEGRAM_LINK, contact):
        if not re.search('http[s]://', contact):
            contact = 'https://' + contact
    elif re.search(FIND.TELEGRAM_NUMBER, contact) and re.search(FIND.TELEGRAM_NUMBER, contact).group(0) == contact:
        contact = '@' + __correct_telephone(contact)
    else:
        contact = '@' + contact
    while contact.count('@@'):
        contact = contact.replace('@@', '@')
    return contact










