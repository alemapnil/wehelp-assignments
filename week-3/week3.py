from urllib.request import urlopen
import json,csv


myURL = urlopen('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')

my_bytes_value = myURL.readlines()[0]
my_json_str = my_bytes_value.decode('utf8').replace("'", '"')
my_json_dic = json.loads(my_json_str)['result']['results']

with open('data.csv','a', newline='') as f:
    writer = csv.writer(f)
    for dic in my_json_dic:
        stitle, address, longitude, latitude, file  = dic['stitle'], dic['address'], dic['longitude'], dic['latitude'], 'https:' + dic['file'].split('https:')[1]
        index = address.find('區')
        address = address[index-2:index+1]
        print(stitle)
        print(address)
        print(longitude,latitude)
        print(file)
        print('---------------')
        writer.writerow([stitle,address,longitude,latitude,file])


