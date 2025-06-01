Question 5________
Write a function called make
_album() that builds a dictionary
describing a music album
. The function should take in an
artist name and an album title,
and it should return a dictionary
containing these two pieces of
information. Use the function to 
make three dictionaries 
representing different albums. 
Print each return value to show 
that the dictionaries are storing 
the


solution ___________________
def make_album(artist, title):
    album = {
        'artist': artist,
        'title': title
    }
    return album

 Creating three albums using the function
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('The Beatles', 'Abbey Road')
album3 = make_album('Adele', '25')

Printing the album dictionaries
print(album1)
print(album2)
print(album3)
