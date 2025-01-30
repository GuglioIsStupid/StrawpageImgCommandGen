import PIL.Image as __I
import json as __J, zlib as __Z, base64 as __B

StrawPageURL = 'https://hawktooah.straw.page/'  # Edit this URL as needed
ImagePath = r"pathtoimage"  # Edit this path as needed

if StrawPageURL.endswith("/"): StrawPageURL = StrawPageURL[:-1]

_ = __I.open(ImagePath).convert("RGB")
__W, __H = _.size
__Q = []

for __Y in range(__H):
    for __X in range(__W):
        __R, __G, __BL = _.getpixel((__X, __Y))  # Renamed __B to __BL
        __Q.append({"type": "start", "x": __X, "y": __Y, "color": f"#{__R:02x}{__G:02x}{__BL:02x}", "size": 2})
        __Q.append({"type": "draw", "x": __X, "y": __Y})
        for __NX in range(__X, 10):
            for __NY in range(__Y, 10):
                __Q.append({"type": "draw", "x": __NX, "y": __NY})

__D = __B.b64encode(__Z.compress(('[' + ','.join([__J.dumps(__P) for __P in __Q]) + ']').replace(" ", "").encode('utf-8'))).decode('utf-8')

__F = f"""const a=new URLSearchParams();a.append('comp','{__D}');a.append('dims[w]','{__W}');a.append('dims[h]','{__H}');a.append('dims[r]','1');fetch('{StrawPageURL}/gimmicks/canvas/2',{{method:'POST',headers:{{}},body:a}}).then(response=>response.text()).then(data=>console.log(data)).catch(error=>console.error('Error:',error));"""

with open("pasteintoconsole.txt", "w") as __V:
    __V.write(__F)
