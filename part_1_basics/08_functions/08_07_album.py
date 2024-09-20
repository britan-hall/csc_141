def make_album(artist, album_name, number_of_songs = ''):
    album = {'Artist' : artist, 'Album Title' : album_name}
    if number_of_songs:
        album['Copys Sold'] = int(number_of_songs)
    return album

album = make_album('Michael Jackson', 'Thriller')
print(album)

album = make_album('AC/DC', 'Back in Black')
print(album)

album = make_album('The Beatles', 'Abbey Road', 30000000)
print(album)