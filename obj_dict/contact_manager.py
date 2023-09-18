#!/use/bin/python3
"""
Contact manager - main
"""
import contact
import constants
import pickle

FILENAME = 'contacts.dat'

class ContactManager:
  """
  """
  def load_contacts(self):
    """
    """
    try:
      input_file = open(FILENAME, 'rb')

      contact_dict = pickle.load(input_file)
      print(contact_dict)
      input_file.close()

    except Exception as err:
      print(err)
      print('Create an empty dictionary')
      contact_dict = {}

    return contact_dict

  def get_menu_choice(self):
    """
    """
    print()
    print('Menu')
    print('----------------------')
    print('1.  Lookup a contact')
    print('2.  Add a contact')
    print('3.  Change a contact')
    print('4.  Delete a contact')
    print('5.  Show total contacts')
    print('6.  Quit')
    print()

    selection = input('Enter your choice: ')
    while not selection.isdigit():
      selection = input('Enter your choice in digit: ')

    choice = int(selection)

    while choice < constants.LOOK_UP or choice > constants.QUIT:
      choice = int(input('Enter a valid choice: '))

    return choice 

  def look_up(self, mycontacts):
    """
    """
    name = input('Enter a name: ')
    print(mycontacts.get(name, 'That name is not found.'))

  def add(self, mycontacts):
    """
    """
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    print('Create Contact object now:')
    entry = contact.Contact(name, phone, email)

    if name not in mycontacts:
      mycontacts[name] = entry
      print('New entry is added.')
    else:
      print('Name already exists')

  def change(self, mycontacts):
    name = input('Enter a name: ')

    if name in mycontacts:
      phone = input('Enter a new phone number: ')
      email = input('Enter a new email: ')

      entry = contact.Contact(name, phone, email)

      mycontacts[name] = entry
      print('Information updated. ')

    else:
      print('That name is not found')

  def delete(self, mycontacts):
    """
    """
    name = input('Enter a name: ')

    if name in mycontacts:
      del mycontacts[name]
      print('Entry deleted')
    else:
      print('That name is not found')

  def showcontacts(self, mycoontacts):
    """
    """
    print('Show contacts: ')
    for key, value in mycoontacts.items():
      # print(format(key, '10s'), value)
      print(f'{key:10s} {value}')
    
  def save_contacts(self, mycontacts):
    """
    """
    print('Save to', FILENAME)
    output_file = open(FILENAME, 'wb')

    pickle.dump(mycontacts, output_file)

    output_file.close()    
