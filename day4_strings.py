#input

text = "             Hello, Python!  "

# Basic properties

print("og: ", text)
print("Length = ", len(text))
print("First character: ", text[0])

# Strip spaces

cleaned = text.strip()
print("stripped : ", cleaned)

# Upper and lower
print("UPPER = ", cleaned.upper())
print("lower = ", cleaned.lower())