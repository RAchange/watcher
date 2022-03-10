# watcher
## Requirements
* Python 3
* modules listed in _requirements.txt_
## Usage
### list all source url in database
```
python3 main.py list
```
![]('./img/list.png')
### add source url to database
```
python3 main.py add <url> [--ncam <nCam, default=1>]
```
![]('./img/add.png')
### remove source url to database
```
python3 main.py remove <url>
```
![]('./img/remove.png')
### show webcam frame stream
```
python3 main.py show <url> [--camno <camNo, default=1>]
```
[![](https://img.youtube.com/vi/fAkMXMFLvBo/0.jpg)](https://www.youtube.com/watch?v=fAkMXMFLvBo)