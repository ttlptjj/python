"""8-7"""
def album(singer_name,album_name,song_number=' '):
    if song_number:
        al={'singer_name':singer_name,'album_name':album_name,'song_number':song_number}

    else:
        al={'singer_name':singer_name,'album_name':album_name}

    return al

a=album('Huachenyu','xinshijie','7')
b=album('Huachenyu','yilei')
print(a+'\n')
print(b)
