# NeteaseCloudMusicBatchDownload
网易云音乐歌单批量下载

#python3
#依赖包
requests
lxml 
urllib.request
json
socket

#用法：
python downloadmusic.py +网易云音乐歌单id

比如：
下载歌单：https://music.163.com/#/playlist?id=2450120466 :
python downloadmusic.py 2450120466

#调用只用API完成

列表api:http://music.163.com/api/playlist/detail?id='+listid;
歌曲下载pai:http://music.163.com/song/media/outer/url?id=%s.mp3'%song_id;
仅做学习交流
