

def sort_contacts_by_length(contacts, start_index, end_index):
    if start_index < end_index:
        split_index = __split_index(contacts, start_index, end_index, contacts[(start_index + end_index) // 2])
        sort_contacts_by_length(contacts, start_index, split_index)
        sort_contacts_by_length(contacts, split_index + 1, end_index)
    return contacts


def __split_index(contacts, start_index, end_index, emphasis):
    start_index -= 1
    end_index += 1
    while True:
        start_index += 1
        while len(contacts[start_index]) > len(emphasis):
            start_index += 1
        end_index -= 1
        while len(contacts[end_index]) < len(emphasis):
            end_index -= 1
        if start_index >= end_index:
            return end_index
        contacts[start_index], contacts[end_index] = contacts[end_index], contacts[start_index]