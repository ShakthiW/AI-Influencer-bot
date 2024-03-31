import requests

# image_url = "https://m.media-amazon.com/images/I/31iH1SJizUL.jpg"
# count = random.randint(1, 1000)

def download_image(url, file_path, file_name):
    full_path = f"{file_path}{file_name}.jpg"
    image_count = 0
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(full_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        image_count += 1
        print(f"Image downloaded to: {full_path}")
    else:
        print(f"Error downloading image: {response.status_code}")

# download_image(image_url, "Images/", f"image{count}")