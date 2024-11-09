# 真实播放   https://video.pearvideo.com/mp4/adshort/20200824/cont-1693468-15345492_adpkg-ad_hd.mp4
# 返回的url https://video.pearvideo.com/mp4/adshort/20200824/1726708690442-15345492_adpkg-ad_hd.mp4
import requests
import re
# 反爬机制：防盗链
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
        "Referer": "https://www.pearvideo.com/video_1693468"

}

url = "https://www.pearvideo.com/videoStatus.jsp?contId=1693468&mrd=0.6604989259003331"

resp = requests.get(url=url,headers=headers).json()
# print(resp)

img_url = resp.get("videoInfo").get("video_image")
print(img_url)
video_url = resp.get("videoInfo").get("videos").get("srcUrl")
print(video_url)

pattern = r'17267[0-9]{8}'
new_url = re.sub(pattern, 'cont-1693468', video_url)  #交换
print(new_url)





