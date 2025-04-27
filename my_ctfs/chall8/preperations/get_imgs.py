import requests
import os
base_url = "https://anonymous-animals.azurewebsites.net/animal/"
def fetch_animals():
    with open("animal_list.txt","r") as f:
        animals = f.read()
    dir_path = "images"
    arr_animals = animals.split("\n")
    os.makedirs(dir_path,exist_ok=True)
    for animal in arr_animals:
        animal = animal.lower()
        curr_url = base_url+animal
        response = requests.get(curr_url)
        with open(dir_path+"/"+animal+".png","wb") as img_file:
            img_file.write(response.content)
if __name__ == '__main__':
    fetch_animals()