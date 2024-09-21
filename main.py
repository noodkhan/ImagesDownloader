# Developed by Noodkhan navin 

# get API
# get Image
# Download Image

import os
from os import listdir
import requests 
import urllib
from playsound import playsound 

# get Image API
def GetImage():
    try :
        accessKey = "YOUR_API_KEY"                     # API KEY
        url = f'https://api.unsplash.com/photos/random/?client_id={accessKey}&orientation=landscape&h=4000&w=2160&fit=max'
        response  = requests.get(url)                  # HTTP get Resquest
        if response.status_code == 200 :
            data = response.json()                     # Image Data as json
            randomPhoto = data['urls']['raw']          # get URL
            print("Random Photo : \n" , randomPhoto)
            return randomPhoto
        else : 
            print("ERROR Failed to Call API")
        print(response)
    except Exception as err:
        print('Error : ' , err)

# Download Image
def Download(imageURL , filepath):
    urllib.request.urlretrieve(imageURL , filepath) # DownloadImage    
    print("\t --- Image Download Sucessful ---")

def DownloadImages(max):
    for i in range(max + 1 , max + 50): 
        playsound('sound.mp3') # testing
        filepath = "C:\\Users\\Nood\\python\\programImage\\"
        filepath += str(i) + ".jpg"
        imageURL = GetImage()
        Download(imageURL , filepath)
        print(filepath)
   

def MaxNumberInFile():
    max = -999999
    filepath = "YOUR_FILE" # C:\\Users\\Nood\\python\\programImage\\
    folder = os.listdir(filepath)
    for file in folder : 
        if (file.endswith(".jpg")):
            file = file.replace('.jpg' , "")
            num = int(file)
            if num > max : 
                max = num
    return max

def main():
    max = MaxNumberInFile()
    DownloadImages(max)
    return 0

main()
