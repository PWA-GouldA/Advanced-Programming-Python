from Contacts import Contacts
from DoublyLinkedList import DoublyLinkedList

aContact = Contacts()
ContactList = DoublyLinkedList()

aContact = Contacts("Fred", "Bloggs", "fb@example.com")
ContactList.push(aContact)

aContact = Contacts("Ivana", "Vin", "iv@example.com")
ContactList.push(aContact)

aContact = Contacts("Robyn", "Banks", "rb@example.com")
ContactList.append(aContact)

aContact = Contacts("Eileen", "Dover", "id@example.com")
ContactList.insert(aContact, 2)

aContact = Contacts("Jacques", "d'Carre", "jdc@example.com")
ContactList.insert(aContact, 1)

print("ADDED SIX ENTRIES")
entries = ContactList.size()
for entry in range(entries):
    print(ContactList.fetch(entry))

ContactList.pop()
print("POPPED FIRST ENTRY")
entries = ContactList.size()
for entry in range(entries):
    print(ContactList.fetch(entry))

ContactList.truncate()
print("TRUNCATED LIST")
entries = ContactList.size()
for entry in range(entries):
    print(ContactList.fetch(entry))

print("FINDING NEMO (Actually Jacques)")
found = ContactList.find("Jacques")
print("[", found, "]")
