import youtube_dl
import argparse
import os


class MP3Download():
    """Class for download and convert youtube videos to MP3 files.
    Args:
        args: [url_path] [download_path]
    """
    def __init__(self, args):
        self.urls_file = args.urls_file
        self.path = os.path.join("downloads", args.path)

    def run(self):
        # Check if the output path already exist if not create the dir
        if self.path is not None:
            self.__check_if_path_exist()
        else:
            self.path = os.getcwd()

        # If the url list is None
        if self.urls_file is None:
            print("## Downloading a single youtube mp3 file ##\n\n")
            print(" - Saving mp3 files in: ", self.path)
            self.__download__()
        else:
            print("## Downloading a youtube mp3 files from file: ##")
            print(" - Saving mp3 files in: ", self.path)
            print(" - urls_file: ", self.urls_file)
            print(" - Reading the text file. . . \n")
            urls_list = self.get_urls_from_file(self.urls_file)
            for indx, video_url in enumerate(urls_list):
                print(f"Processing file [{indx+1} of {len(urls_list)}] \n")
                self.__download__(video_url)

    def get_urls_from_file(self, urls_file):
        lines = []
        with open(urls_file, 'r') as f:
            for line in f:
                if not line.isspace():
                    lines.append(line)
        return lines

    def __check_if_path_exist(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
            print(" - Creating dir: ", self.path)

    def __download__(self, video_url = None):
        if video_url is None:
            video_url = input("Please enter youtube video url:")

        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl': str(self.path)+'/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        }

        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_url])
                print("Download complete")
        except:
            print(" - Error: Can not downloading:  "+str(video_url))

if __name__=='__main__':
    # Create instance of argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("--urls_file",
                        type = str,
                        help='Path to Text file with the list of Youtube urls',
                        required=False)
    parser.add_argument("--path",
                        default="downloads",
                        type = str,
                        help='Path to store the mp3 files',
                        required=False)
    args = parser.parse_args()

    # Create the instance of downloader
    downloader = MP3Download(args)
    # Run the downloader
    downloader.run()
