def find_phone_number(contacts, name):
    # TODO: build a dict from `contacts` (list of (name, phone) tuples),
    # then return the phone number for `name`, or "Not found"
   book = dict(contacts)
   if name in book:
      return book[name]
   return "Not found" 


find_phone_number([("Ada", "0801"), ("Bola", "0802")], "Ada")
find_phone_number([("Ada", "0801")], "Chidi")
find_phone_number([], "Ada")
