#!/use/bin/python3
"""
Contact manager - main
"""
import contact_manager
import constants

def main():
  """
  """
  contact_mgr = contact_manager.ContactManager()

  mycontact = contact_mgr.load_contacts()

  choice = 0

  while choice != constants.QUIT:
    choice = contact_mgr.get_menu_choice()

    if choice == constants.LOOK_UP:
      contact_mgr.look_up(mycontact)

    elif choice == constants.ADD:
      contact_mgr.add(mycontact)

    elif choice == constants.CHANGE:
      contact_mgr.change(mycontact)

    elif choice == constants.SHOWLIST:
      contact_mgr.showcontacts(mycontact)

    elif choice == constants.DELETE:
      contact_mgr.delete(mycontact)

  contact_mgr.save_contacts(mycontact)

if __name__ == "__main__":
  main()

