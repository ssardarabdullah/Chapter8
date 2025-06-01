def make_album(artist, title):
    album = {
        'artist': artist,
        'title': title
    }
    return album

# Creating three albums using the function
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('The Beatles', 'Abbey Road')
album3 = make_album('Adele', '25')

# Printing the album dictionaries
print(album1)
print(album2)
print(album3)