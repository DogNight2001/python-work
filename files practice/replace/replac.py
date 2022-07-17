word=["donkey","fuck","motherfucker"]
with open("text.txt") as f:
    c=f.read()
for word in c:
    c=c.replace(word,"####")
with open("text.txt","w") as f:
    f.write(c)
