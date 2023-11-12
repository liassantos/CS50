import re

email = input("What's your email? ").strip()
edu = "edu"
if re.search("^\S\w+@\S(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
  print("valid")
else:
  print("invalid")