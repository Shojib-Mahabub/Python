import random                                           #random number genaretor
import urllib.request                                   #url library

url= '#calling the function'                            #var declear

def down(url):                                          #starting function
    name = random.randrange(1,10)                       #set name for the file with random number 1 to 10
    name_extension = str(name)+'.jpg'                   #set name with the extension type
    urllib.request.urlretrieve(url, name_extension)     #call function from module and bypass url and name

down('url')                                             #calling the function