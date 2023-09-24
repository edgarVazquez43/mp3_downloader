# YOUTUBE DOWNLOAD
--------------------

This repo contains python script to download and convert youtube videos to mp3 files.

## Requirements
- python => 3.9
- youtube_dl

## Instalation
1. Create a virtual env 
```bash
python -m venv .venv
```
1.1. Activate the virtual env
```
source .venv/bin/activate
```

2. Install the requirements
```bash
pip install -r requirements.txt
```

3. A change is needed in the file `.venv/lib/python[VERSION]/site-packages/youtube_dl/extractor/youtube.py` line `1794`. Replace with the follow code: 
```python
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id', fatal=False) if owner_profile_url else None
```



## Usage
0. The zero step is to search on YT for the video you want download to.
1. Save the video url link on a txt file `test.txt`, for instance. __*NOTE: Playlist links are also allowed__
```
https://www.youtube.com/watch?v=EAa4WlrBq9I
```
2. If url_file is not set, the script will ask you for a a single youtube_link.


```bash
python download.py --url [PATH TO URLS FILE] --path [OUTPUT PATH]
```

- Example
```
python download.txt --url urls/test.txt --path downloads/test
```