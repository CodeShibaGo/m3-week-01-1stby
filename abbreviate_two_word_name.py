def abbrev_name(name):
  isupper_name = [char for char in name if char.isupper()]
  return '.'.join(isupper_name)
print(abbrev_name('John Smith'))