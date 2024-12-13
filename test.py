def line_length(abc):
  if abc =="" or abc.isspace():
    return "N"
  else:
    return len(abc)

assert line_length("int") == 3
assert line_length("") == "N"
assert line_length("    ") == "N"


