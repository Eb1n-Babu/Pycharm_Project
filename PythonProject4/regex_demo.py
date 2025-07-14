import re

word = "good is greate"
y = re.search("^good.*greate$", word)
if y:
 print("match")
else:
 print("not match")