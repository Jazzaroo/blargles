
print("Welcome to the Blargle Generator, perhaps more famously known as the Blarglator.")
blarglist = []
class Blargle:
    mood = "calm"
    name = "blargie"      
new_blargle = Blargle()
new_blargle.name = input("Please name the Blargle.")
new_blargle.mood = input("How does %s feel today?" %new_blargle.name)
blarglist.append(new_blargle)
print("%s is feeling %s." % (blarglist[0].name, blarglist[0].mood))
for x, blarglist in enumerate(blarglist):
    print (x, "%s is feeling %s." % (blarglist[x].name, blarglist[x].mood))