import untangle
import pprint

obj = untangle.parse('data/imac.itunes.xml')


def get_playlists():
    ret = []
    plists = obj.plist.dict.array.dict[10:]
    for plist in plists:
        ret.append(plist.string[0].cdata)
    return ret


def get_tracks():
    ret = {}
    tracks = obj.plist.dict.dict.dict
    for track in tracks[:100]:
        id = track.integer[0].cdata
        t = {'id': id,
             'name': track.string[0].cdata,
             'artist': track.string[1].cdata,
             'album': track.string[2].cdata,
             'year': track.integer[7].cdata}
        ret[id] = t
    return ret


if __name__ == '__main__':
    # lists = get_playlists()
    # print(lists)
    tracks = get_tracks()
    pprint.pprint(tracks)
    print('track 2084 is', tracks['2084'])
