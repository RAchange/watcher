import pickle
import urllib.request
import cv2
import numpy as np
import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

def list_table():
    with open("./.data/webcam_list.pickle", "rb") as fp:
        webcam_list = pickle.load(fp)
    urls = [*webcam_list]
    table = Table(show_header = True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("url", min_width=20)
    table.add_column("count of cameras", min_width=12, justify="right")
    
    for idx, url in enumerate(urls, start=1):
        table.add_row(str(idx), url, str(webcam_list[url]))
    console.print(table)

@app.command()
def add(url: str, nCam: int = 1):
    with open("./.data/webcam_list.pickle", "rb") as fp:
        webcam_list = pickle.load(fp)
    webcam_list[url] = nCam
    with open("./.data/webcam_list.pickle", "wb") as fp:
        pickle.dump(webcam_list, fp)
    list_table()
    typer.echo(f"{url} has been added to database")

@app.command()
def list():
    list_table()
    typer.echo(f"All camera source has been listed")
        
@app.command()
def remove(ip: str):
    with open("./.data/webcam_list.pickle", "rb") as fp:
        webcam_list = pickle.load(fp)
    del webcam_list[ip]
    with open("./.data/webcam_list.pickle", "wb") as fp:
        pickle.dump(webcam_list, fp)
    list_table()
    typer.echo(f"{ip} has been remove from database")

def camPreview(imgUrl):
    try:
        while True:
            url_response = urllib.request.urlopen(imgUrl)
            
            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            
            img = cv2.imdecode(img_array, -1)
            
            cv2.imshow(imgUrl, img)
            
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
    except:
        cv2.destroyWindow(imgUrl)

@app.command()
def show(url: str, camNo: int = 1):
    imgUrl = url + '/cam_' + str(camNo) + '.jpg'
    typer.echo(f"start {imgUrl}")
    camPreview(imgUrl)

if __name__ == '__main__':
    app()
