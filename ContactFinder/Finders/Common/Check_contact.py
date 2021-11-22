from libraries.ContactFinder.Finders.Common.Constants import VALIDITY_LENGTH, ERROR
import re
error_before = re.compile('[^ :,();\n\t\v\r\f\a\b •-]')
error_after = re.compile('[^ .!?(),;: •\n\t\v\r\f\a\b-]')


def check_contact(data, contact, keyword, contact_position, kind_contact):
    contact = __delete_spaces(contact)
    if keyword:
        if contact_position == 'after':
            data = data[data.index(keyword)+len(keyword):]
        else:
            data = data[:data.index(keyword)]
    return __check_contact(data, contact, keyword, contact_position, kind_contact)


def __check_contact(data, contact, keyword, position, kind_contact):
    if keyword and kind_contact:
        return __full_check(data, contact, position, kind_contact) and contact.lower() not in ERROR.KEYWORDS
    elif kind_contact:
        return __check_symbols(data, contact) and __check_contact_length(contact, kind_contact) and contact.lower() not in ERROR.KEYWORDS
    if keyword and not kind_contact:
        return __full_check(data, contact, position, kind_contact)
    return __check_symbols(data, contact)


def __full_check(data, contact, position, kind_contact):
    return __check_symbols(data, contact) and __check_contact_length(contact, kind_contact) \
           and __check_contact_in_keyword(data, contact, position)


def __check_symbols(data, contact):
    return not (__check_symbol_before(data, contact) or __check_symbol_after(data, contact))


def __check_contact_length(contact, kind_contact):
    if kind_contact == 'telephone':
        contact = ''.join(re.findall('\d+', contact))
        return VALIDITY_LENGTH.TELEPHONE[0] <= len(contact) <= VALIDITY_LENGTH.TELEPHONE[1]
    if kind_contact == 'link':
        return VALIDITY_LENGTH.LINK[0] <= len(contact) <= VALIDITY_LENGTH.LINK[1]
    if kind_contact == 'username':
        return VALIDITY_LENGTH.USERNAME[0] <= len(contact) <= VALIDITY_LENGTH.USERNAME[1]
    if kind_contact == 'icq':
        contact = ''.join(re.findall('\d+', contact))
        return VALIDITY_LENGTH.ICQ[0] <= len(contact) <= VALIDITY_LENGTH.ICQ[1]
    if kind_contact == 'email':
        if re.search('@', contact):
            local_host = contact[:contact.index('@')]
            domain = contact[contact.index('@')+1:]
            return VALIDITY_LENGTH.EMAIL[0][0] <= len(local_host) <= VALIDITY_LENGTH.EMAIL[0][1] \
                and VALIDITY_LENGTH.EMAIL[1][0] <=  len(domain) <= VALIDITY_LENGTH.EMAIL[1][1]
    return True


def __check_contact_in_keyword(data, contact, position):
    if position == 'after':
        return data.index(contact) <= 5
    else:
        return len(data) - data.index(contact) - len(contact) <= 5


def __check_symbol_before(data, contact):
    if data.index(contact) == 0: return []
    return error_before.findall(data[data.index(contact)-1])


def __check_symbol_after(data, contact):
    if data.index(contact) + len(contact) == len(data): return []
    return error_after.findall(data[data.index(contact)+len(contact)])


def __delete_spaces(contact):
    if contact[0] == ' ':
        contact = contact[1:]
    if contact[-1] == ' ':
        contact = contact[0:len(contact)-1]
    return contact