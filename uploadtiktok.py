from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend

#  single video
upload_video('mWOc22fXTOupsySVnNtK8w.mp4', 
            description='What do you do when emotional bad? #shorts #IWTL', 
            cookies='cookies.txt')

# Multiple Videos
# videos = [
#     {
#         'path': '00nwNhadSLagt5B1LBQGYA.mp4', 
#         'description': 'This is my first tiktok video'
#     },
#     {
#         'path': 'mWOc22fXTOupsySVnNtK8w.mp4', 
#         'description': 'This is my second tiktok video'
#     }
# ]


# auth = AuthBackend(cookies='cookies.txt')
# upload_videos(videos=videos, "#fyp", auth=auth)