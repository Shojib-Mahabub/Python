from urllib import request

url = 'http://www.textfiles.com/100/adventur.txt'
def download(url):
    response = request.urlopen(url) #request to open the URL
    read = response.read()          #read from url
    read_str = str(read)            #converting to string
    file = read_str.split('\\n')    #setting up lines
    save = r'first.txt'             #file name and path [directory folder here]
    fo = open(save, 'w')            #open/create the file in write mode
    for i in file:                  #loop through the lines
        fo.write(i + '\n')          #write in
    fo.close()                      #closing file

download(url)                       #calling function for downloading the file

