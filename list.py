playlist=["Naa Ready", "Velayadhum", "Believer", "Vel Maral", "Believer"]

#list methods
'''
print(playlist)
playlist.reverse()
print(playlist)
playlist.append("hate you")
print(playlist)
playlist.insert(2,"Love You")
print(playlist)
playlist.remove("Vel Maral")
print(playlist)
playlist.pop()
print(playlist)
print("Count of:",playlist.count("Believer"))
'''


#list_slicing
'''
print(playlist[0:3])
print(playlist[-3:])
'''


#list_iteration
'''
for p in playlist:
    print("count",p)
for p in playlist:
    print(p+" playlist of vicky")
'''

#check_if
'''
if "Vel Maral" in playlist:
    print("Yes")
else:
    print("No")
'''

#replace list value
'''
playlist[0]='RASATHI UNNA'
print(playlist)
'''

#count of index
'''
for i,p in enumerate(playlist):
    print("List of Playlist",i, ": ",p)
'''