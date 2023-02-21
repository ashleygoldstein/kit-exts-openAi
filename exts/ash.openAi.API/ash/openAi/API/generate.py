from api import API_KEY
import openai
import requests # request img from web
import shutil # save img locally

openai.api_key = API_KEY


response = openai.Image.create(
  prompt="long hallway lined with books",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
 
url = image_url
file_name = "generatedImg.png"

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
