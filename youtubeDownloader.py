import requests
import yt_dlp

def dosya_verisini_cek(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        # İçerik verisini döndür
        return response.content
    else:
        # İstekte hata oluştu, hata mesajını döndür
        return "İstekte hata oluştu: {}".format(response.status_code)


def youtube_video_indir(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # En iyi kalitede videoyu indir
        'outtmpl': 'video_temp.mp4',  # İndirilen videoyu geçici bir dosyada sakla
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(video_url, download=False)
            # Videoyu indir ve içeriği bir değişkende sakla
            with ydl.urlopen(info_dict['url']) as f:
                video_icerik = f.read()

            return video_icerik
        except yt_dlp.utils.DownloadError as e:
            print(f"Hata oluştu: {e}")
            return None

url_list = [
    ("video1", "https://valentura.com/images/slides/Web_Slider.mp4", True),
    ("photo1", "https://img.memurlar.net/galeri/6361/463c6370-ad1b-e411-a1b0-14feb5cc13c9.jpg", True),
    ("data1", "http://date.jsontest.com/.json", False)]

# for asset_name, url, _bin in url_list:
#     veri = dosya_verisini_cek(url)
#     write_type = "wb" if _bin else "w"          
#     # print(veri)
#     with open(f'{asset_name}.{url.split(".")[-1]}', write_type) as f:
#         f.write(veri.decode("utf-8") if not _bin else veri)
    
kaydet_yolu = "kayit_dizini/"
video_url = "https://www.youtube.com/watch?v=64CIh2Vw358"

video_icerik = youtube_video_indir(video_url)