from google_images_download import google_images_download 

try:
    response = google_images_download.googleimagesdownload()
    args = {
        "keywords": "wallpapers of fall",
        "limit": 10,
        "print_urls":True,
    }
    print(response.download(args))

except:
    print("Didn't work!")
