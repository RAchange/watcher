# watcher
## Requirements
* Python 3
* modules listed in _requirements.txt_
## Usage
### list all source url in database
```
python3 main.py list
```
![]('https://github.com/RAchange/watcher/raw/main/img/list.png')
### add source url to database
```
python3 main.py add <url> [--ncam <nCam, default=1>]
```
![]('https://github.com/RAchange/watcher/raw/main/img/add.png')
### remove source url to database
```
python3 main.py remove <url>
```
![]('https://github.com/RAchange/watcher/raw/main/img/remove.png')
### show webcam frame stream
```
python3 main.py show <url> [--camno <camNo, default=1>]
```
[![](https://img.youtube.com/vi/fAkMXMFLvBo/0.jpg)](https://www.youtube.com/watch?v=fAkMXMFLvBo)