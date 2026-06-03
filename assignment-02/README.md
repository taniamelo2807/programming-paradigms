Media Library Hub

This project is a small Media Library Hub made in Python. The program creates different types of media items, such as songs, podcasts and audiobooks. Each media item has a title, a creator and a duration. The program loads the media items from a small dataset, adds them to a playlist, stores the playlist inside a library and then prints useful information about the library. It also shows sorting and CSV export. The project was made in one Python file, so it is simple to run and easy to understand.

How to run

python media_library.py

One OOP example used in this project is inheritance. The classes Song, Podcast and Audiobook inherit from the abstract class MediaItem. This avoids repeating the same attributes in every class and allows each media type to have its own describe method.

Another OOP example is composition. The Library class contains playlists, and the Playlist class contains media items. This means the program is built using objects that work together.

One design pattern used in the project is the Observer pattern. The EventBus class allows the playlist to publish an event when an item is added. A subscriber then receives that event and saves a message in the log.

The project also uses the Strategy pattern for sorting. The playlist can use SortByTitle or SortByDuration without changing the playlist code.

Sample output

Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman - episode 400 (7200s)
Audiobook: Clean Code by Robert Martin - 17 chapters (25200s)
{'total_items': 4, 'total_duration': 33054}
['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:Lex Fridman #400', 'added:Clean Code']
Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400
type,title,duration
Song,Bohemian Rhapsody,354
Song,Blinding Lights,200
Podcast,Lex Fridman #400,7200
Audiobook,Clean Code,25200
