from pytube import YouTube

def download_video(url, save_path):
    try:
        # YouTube videosunu indirmek için YouTube nesnesi oluşturun
        yt = YouTube(url)

        # En yüksek çözünürlükteki videoyu seçin
        video = yt.streams.get_highest_resolution()

        # Videoyu belirtilen yola kaydedin
        video.download(save_path)

        print("Video başarıyla indirildi!")
    except Exception as e:
        print("Hata oluştu:", str(e))

if __name__ == "__main__":
    video_url = input("YouTube video URL'sini girin: ")
    save_path = input("Videoyu kaydetmek için dosya yolunu girin: ")

    download_video(video_url, save_path)