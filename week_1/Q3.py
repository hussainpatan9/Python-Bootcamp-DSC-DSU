from time import sleep
song ="""[Verse 1]
    The club isn't the best place to find a lover
    So the bar is where I go
    Me and my friends at the table doing shots
    Drinking fast and then we talk slow
    And you come over and start up a conversation with just me
    And trust me I'll give it a chance now
    Take my hand, stop, put Van the Man on the jukebox
    And then we start to dance, and now I'm singing like

    [Pre-Chorus]
    Girl, you know I want your love
    Your love was handmade for somebody like me
    Come on now, follow my lead
    I may be crazy, don't mind me
    Say, boy, let's not talk too much
    Grab on my waist and put that body on me
    Come on now, follow my lead
    Come, come on now, follow my lead
    """
song_lines = song.splitlines( )
for i,lines in enumerate(song_lines):
    print(song_lines[i])
    sleep(1)