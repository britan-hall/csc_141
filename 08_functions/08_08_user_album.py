user_album_active = True

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

while user_album_active == True:
    print('AT ANY POINT ENTER "q" to quit')
    
    user_artist = input('Name of the artist: ')
    if user_artist == 'q':
        user_album_active = False
        break
    
    user_album_title = input('Name of the album: ')
    if user_album_title == 'q':
        user_album_active = False
        break
   
    user_sold = input('Albums Sold (Optional, press enter to skip) : ')
    if user_sold == 'q':
        user_album_active = False
        break
    
    if user_sold:   
        album = make_album(user_artist,user_album_title,user_sold)
        print(album)
        user_album_active = False
        break
    else:
        album = make_album(user_artist,user_album_title)
        print(album)
        user_album_active = False
        break