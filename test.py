def line_length(abc):
  if abc =="" or abc.isspace():
    return "N"
  else:
    return len(abc)

assert line_length("int") == 3
assert line_length("") == "N"
assert line_length("    ") == "N"

def line_in_the_file(abc):
  f = open("File.txt", "w+")
  f.write(abc)
  f.close()

line_in_the_file("Hi 123456789")
f = open("File.txt", "r")
assert f != None
