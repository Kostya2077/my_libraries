from libraries.ContactFinder.TextContactFinder import TextContactFinder
from libraries.ContactFinder.Finders.Common.Functions import *
from libraries.ContactScrambler.Common.Sort import sort_contacts_by_length
from libraries.ContactScrambler.Common.Constants import *
import re
symbols = ['.','*', '+', '?', '/', '-', '(', ')']


def _find_contacts_in_data(data):
    contacts = []
    copy_data = data
    finder = TextContactFinder(copy_data)
    contacts += finder.get_email(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_facebook(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_github(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_icq(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_linkedin(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_telephone(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_skype(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_telegram(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_viber(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_vkontakte(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_whatsapp(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_gitlab(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_careerhabr(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_qnahabr(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_habr(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_youtube(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_behance(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_dribbble(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_freelance(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_instagram(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_resume(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_twitter(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts += finder.get_stackoverflow(CONTACT_FORMAT.INCORRECT, SEARCH_CONTACTS.LAX)
    contacts = sorted(set(contacts))
    contacts = sort_contacts_by_length(contacts, 0, len(contacts)-1)
    return contacts


def _find_keywords_in_data(data):
    keywords = []
    regex = REGEX_KEYWORD
    array_of_keywords = [regex.EMAIL, regex.FACEBOOK, regex.GITHUB, regex.ICQ,
                         regex.LINKEDIN, regex.TELEPHONE, regex.SKYPE, regex.TELEGRAM,
                         regex.VIBER, regex.VKONTAKTE, regex.WHATSAPP, regex.YOUTUBE,
                         regex.DRIBBBLE, regex.HABR, regex.QNAHABR, regex.TWITTER,
                         regex.FREELANCE, regex.BEHANCE, regex.INSTAGRAM, regex.RESUME,
                         regex.STACKOVERFLOW, regex.GITLAB]
    for regex_keyword in array_of_keywords:
        for found_keyword in re.findall(regex_keyword, data):
            if check_contact(data, found_keyword, '', WORD_POSITION.NONE, KIND_CONTACT.NONE):
                keywords.append(found_keyword)
    keywords = sort_contacts_by_length(keywords, 0, len(keywords) - 1)
    return keywords


def _result_of_encryption(data, contacts, encrypt):
    for contact in contacts:
        for symbol in symbols:
            contact = contact.replace(symbol, '['+symbol+']')
        while contact[0] == ' ':
            contact = contact[1:]
        if re.search(contact, data):
            if contact[0] == ' ':
                contact = contact[1:]
            data = re.sub(contact, '*' * len(contact) * encrypt, data)
    keywords = _find_keywords_in_data(data)
    for keyword in keywords:
        if re.search(keyword, data):
            data = re.sub(keyword, '*' * len(keyword) * encrypt, data)
    return data


def encrypt_data_after_contacts(data, encrypt):
    for hashtag in re.findall(INFO_SCRAMBLER.HASHTAG, data):
        data = data.replace(hashtag, '*'*len(hashtag)*encrypt)
    for word in re.findall(INFO_SCRAMBLER.STRANGE_WORDS, data):
        data = data.replace(word, '*'*len(word)*encrypt)
    for email in re.findall(INFO_SCRAMBLER.ERROR_EMAIL, data):
        data = data.replace(email, '*'*len(email)*encrypt)
    while data.count('  '):
        data = data.replace('  ', ' ')
    return data


class TextScrambler:

    def __init__(self):
        pass

    def encrypt_data(self, data, ENCRYPT):
        try:
            contacts = _find_contacts_in_data(data)
            if contacts:
                data = _result_of_encryption(data, contacts, ENCRYPT)
            data = encrypt_data_after_contacts(data, ENCRYPT)
            return data
        except:
            return data
