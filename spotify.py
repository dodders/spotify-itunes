import json

plistf = open('data/playlists.txt', 'r')
plists = json.load(plistf)
trackf = open('data/tracks.txt', 'r')
tracks = json.load(trackf)


def verify(lists, tracks):
    verified = True
    for id, plist in lists.items():
        for track in plist['tracks']:
            if track not in tracks:
                print('didn\'t find track ', track, ' in playlist ', list['name'])
                verified = False
    if verified:
        print("verified!")
    return verified


if __name__ == '__main__':
    verify(plists, tracks)
