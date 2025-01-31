import PIL as pillow
import json, zlib, base64
import time

def ToStrawpage(url: str, image: pillow.Image.Image) -> None:
    print('Generating Command...')
    
    if url.endswith("/"): url = url[:-1] # Remove trailing slash

    image = image.convert("RGB") # Alpha channel can't really be used here
    width, height = image.size

    query: list[dict] = []

    starttime: float = time.time()

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            query.append({"type": "start", "x": x, "y": y, "color": f"#{r:02x}{g:02x}{b:02x}", "size": 2})
            query.append({"type": "draw", "x": x, "y": y})
            for nx in range(x, 10):
                for ny in range(y, 10):
                    query.append({"type": "draw", "x": nx, "y": ny})

    data: str = base64.b64encode(zlib.compress(('[' + ','.join([json.dumps(point) for point in query]) + ']').replace(" ", "").encode('utf-8'))).decode('utf-8')
    # ^ Compress the data and encode it in base64

    fetch: str = f"""const a=new URLSearchParams();a.append('comp','{data}');a.append('dims[w]','{width}');a.append('dims[h]','{height}');a.append('dims[r]','1');fetch('{url}/gimmicks/canvas/2',{{method:'POST',headers:{{}},body:a}}).then(response=>response.text()).then(data=>console.log(data)).catch(error=>console.error('Error:',error));"""

    with open("Command.txt", "w") as file:
        file.write(fetch)
        print(fetch)

    print("Done! Time taken:", time.time() - starttime)