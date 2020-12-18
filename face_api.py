import requests
from PIL import Image
from io import BytesIO

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f12693bc12c7479d829a57734f145e24',
}
body = dict()
body["url"] = "https://sun9-76.userapi.com/impg/U_sbr3ZvtKamMovdlPoaH6QuWjExjcxD963UGg/TCW_Sk7WQi8.jpg?size=1173x657&quality=96&proxy=1&sign=428f6c22d6472fc3b0a8e403bae44926&type=album"
body = str(body)

FaceApiDetect = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true'
top_word = "top"
left_word = "left"
width_word = "width"
height_word = "height"
url_im = "https://sun9-76.userapi.com/impg/U_sbr3ZvtKamMovdlPoaH6QuWjExjcxD963UGg/TCW_Sk7WQi8.jpg?size=1173x657&quality=96&proxy=1&sign=428f6c22d6472fc3b0a8e403bae44926&type=album"
try:
    response = requests.post(FaceApiDetect, data=body, headers=headers)
    res = response.text
    res = res[res.find(top_word):]
    
    res = res.replace(":", "")
    res = res.replace("}}]", "")
    res = res.replace("\"", " ")
    
    left = int(res[res.find(left_word)+5 : res.find("w")].replace(",",""))
    top = int(res[res.find(top_word)+4 : res.find(",")])
    width = int(res[res.find(width_word)+6 : res.find("height")].replace(",",""))
    height = int(res[res.find(height_word)+7 :])
    
    response = requests.get(url_im)
    img = Image.open(BytesIO(response.content))
    
    cropped = img.crop((left-250,top-150, left+width+200,top+height+300))
    cropped.save('D:/crop5.png')
    cropped.show()
except Exception as e:
    print(e)
