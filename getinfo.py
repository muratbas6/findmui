import sys
import spotipy.util as util
import json
import spotipy

scope = 'user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    username = "fotntys10iaawb4qd2nexvz50"

token = util.prompt_for_user_token(username, scope, client_id='client_id',
                                   client_secret='your_client_secret', redirect_uri='http://www.google.com/')

sp = spotipy.Spotify(auth=token)


def get_current_song_info():
    results = sp.currently_playing()
    content = results.get("item")
    song_name = content['name']
    artist = content['artists'][0]['name']
    with open('song.json', 'w') as outfile:
        json.dump(content, outfile, sort_keys=True,
                  indent=4, separators=(',', ':'))
    return song_name, artist


def user_info():
    user_information = sp.current_user()
    content = user_information['display_name']
    with open('user.json', 'w') as outfile:
        json.dump(content, outfile, sort_keys=True,
                  indent=4, separators=(',', ':'))
    return content


while token:
    if token:
        song_name, artist = get_current_song_info()
        user = user_info()
        print("Şuanda çalan", artist, "-", song_name, user)
    else:
        print("Can't get token for", username)
