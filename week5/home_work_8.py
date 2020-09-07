def get_full_name(first, last):
    full_name= first+' '+last
    return full_name.title()
qa_tester= get_full_name('nadiya', 'zelman')
print(qa_tester)

################ 8-6 ###############################
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")
city_country('santiago', 'chile')
city_country('lviv', 'ukraine')
city_country('aphine', 'greese')

#################### 8-7 ###############################
def make_album(name, title):
    album= {'name':name.title(), 'title':title.title()}
    return album
album=make_album('kesha', 'high road')
print(album)
album=make_album('krewella', 'zer0')
print(album)
album=make_album('drake', 'scorpion')
print(album)

################# 8-9 #############################
magicians =['David Copperfield', 'David Blaine', 'Harry Houdini', 'Criss Angel']
def show_magicians():
    for magician in magicians:
        print(f"{magician}.")
show_magicians()

################ 8-10 #############################
magicians =['David Copperfield', 'David Blaine', 'Harry Houdini', 'Criss Angel']
def make_great():
    for magician in magicians:
        print(f"The Great {magician}.")
make_great()

################# 8-11 ##########################
magicians =['David Copperfield', 'David Blaine', 'Harry Houdini', 'Criss Angel']
def show_magicians():
    for magician in magicians:
        return magician
def make_great():
    for magician in magicians:
        print(f"The Great {magician}.")
make_great()
show_magicians()
