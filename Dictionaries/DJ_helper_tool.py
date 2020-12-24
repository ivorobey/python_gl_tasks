# Create get_song() helper function that takes two parameters - dictionary with songs (see below) and integer argument which is a maximum length of a song in seconds.

# songs is an array of objects which are formatted as follows:
# {
#  'artist': 'Artist',
#  'title': 'Title String',
#  'playback': '04:30'
# }
# You can expect playback value to be formatted exactly like above.

# Result should be a title of the longest song from the database that matches the criteria of not being longer than specified time.
# If there's no songs matching criteria in the database, return False.

songs_db = [{
    'artist': 'Led Zeppelin',
    'title': 'Stairways to heaven',
    'playback': '09:20'
}, {
    'artist': 'Metallica',
    'title': 'Master of puppets',
    'playback': '04:30'
}, {
    'artist': 'Nirvana',
    'title': 'The Man who sold the world',
    'playback': '03:10'
}, {
    'artist': 'Stepan Galyabarda',
    'title': 'Lyst do mamy',
    'playback': '02:20'
}]


def get_song(db, len_seconds):
    if len_seconds == 0:
        return False

    for i in db:
        time = i.get('playback').split(':')
        time_in_sec = int(time[0]) * 60 + int(time[1])
        if len_seconds >= time_in_sec:
            return "Best possible song: {}/{}".format(i['artist'], i['title'])


print(get_song(songs_db, 145))

