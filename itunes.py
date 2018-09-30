import untangle
import json

obj = untangle.parse('data/imac.itunes.xml')
includef = open('data/playlist-include.txt', 'r')
dolist = json.loads(includef.read())
print('process list: ', dolist)


def get_playlists():
    ret = {}
    plists = obj.plist.dict.array.dict[10:]
    for plist in plists:
        pname = plist.string[0].cdata
        if pname in dolist:
            print('adding playlist ', pname)
            playlist = {}
            playlist['name'] = pname
            tracks = []
            for id in plist.array.dict:
                tracks.append(id.integer.cdata)
            playlist['tracks'] = tracks
            ret[playlist['name']] = playlist
        else:
            print('skipping playlist ', pname)

    return ret


def get_tracks():
    ret = {}
    tracks = obj.plist.dict.dict.dict
    for track in tracks:
        id = track.integer[0].cdata
        t = {'id': id,
             'name': track.string[0].cdata,
             'artist': track.string[1].cdata,
             'album': track.string[2].cdata}
        ret[id] = t
    return ret


if __name__ == '__main__':
    lists = get_playlists()
    with open('data/playlists.txt', 'w') as f:
        f.write(json.dumps(lists))
    tracks = get_tracks()
    with open('data/tracks.txt', 'w') as f:
        f.write(json.dumps(tracks))
