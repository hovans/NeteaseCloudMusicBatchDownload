from requests import request
#from lxml import etree
import urllib.request
import json
import sys,os
import socket
socket.setdefaulttimeout(30)


def getmess(listid):
	header={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
	}

	response=request('GET','http://music.163.com/api/playlist/detail?id='+listid,headers=header)
	html=response.text
	j = json.loads(html)
	mess=j["result"]["tracks"]
	listname=j["result"]["name"]
	if not os.path.exists(listname):
		os.mkdir(listname)
	haddownload=os.listdir(".\\"+listname)
	for i in range(len(mess)):
		if (mess[i]["name"]+".mp3") not in haddownload:
			download_song(mess[i]["id"],mess[i]["name"].replace('/',''),listname)
			print(mess[i]["name"])


def download_song(song_id,song_name,listname):
        song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%song_id
        path ='.\\'+listname+'\\'+song_name+'.mp3'
        try:
            urllib.request.urlretrieve(song_url, path)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(song_url, path)
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")


if __name__ == '__main__':
	listid=sys.argv[1]
	getmess(listid)
