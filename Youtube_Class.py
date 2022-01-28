class Youtube:
	def __init__(self):
		from pytube import YouTube
		from pytube import Playlist
		import os
		from urllib.error import URLError
		import time
		
		self.Youtube = YouTube
		self.Playlist = Playlist
		self.os = os
		self.time = time

		self.BD = self.os.path.dirname(self.os.path.abspath(__file__))
		self.Default_Folder = 'Output_Files'

		self.input_video_url_file = 'paste_video_url_here.txt'
		self.input_playlist_url_file = 'paste_playlist_url_here.txt'


	def entire_playlist_download(self, Playlist_url):
		PL = self.Playlist(Playlist_url)
		PL_list = list(PL)

		Title = PL.title.replace('/',' ').replace('\\',' ').replace(':', ' ').replace('*',' ').replace('?', ' ').replace('"','').replace('|', ' ')

		Output_Folder = self.os.path.join(self.BD, self.Default_Folder, Title)
		Skipped = 0

		for count, video in enumerate(PL_list[::-1]):
			try:
				y_v = self.Youtube(video)
				y_s = y_v.streams.filter(progressive=True).order_by('resolution').desc().first()
				y_s.download(Output_Folder)
				print(count+1, "Done")
			except (TimeoutError, URLError) as e:
				Skipped+=1

		print("Download Completed\n")
		self.time.sleep(2)
		if Skipped>0:
			print(f"{Skipped} videos skipped\n")


	def single_video_download(self, video_url):
		Output_Folder = self.os.path.join(self.BD,self.Default_Folder)

		y_v = self.Youtube(video_url)
		y_s = y_v.streams.filter(progressive=True).order_by('resolution').desc().first()
		y_s.download(Output_Folder)

		print("Download Completed\n")
		self.time.sleep(2)

	
	def multiple_video_download(self):
		file_path = self.os.path.join(self.BD,self.input_video_url_file)
		f = open(file_path, 'r')
		v_urls = f.readlines()
		f.close()

		Folder = str(input("Enter folder name to save files\n-->"))
		Output_Folder = self.os.path.join(self.BD,self.Default_Folder,Folder)

		count = 0
		for url in v_urls:
			if url:
				url = url.strip('\n')
				y_v = self.Youtube(url)
				y_s = y_v.streams.filter(progressive=True).order_by('resolution').desc().first()
				y_s.download(Output_Folder)
				count+=1
				print(count, "Done")
		print("Download Completed\n")
		self.time.sleep(2)

			
	def multiple_playlist_download(self):
		file_path = self.os.path.join(self.BD,self.input_playlist_url_file)
		f = open(file_path, 'r')
		p_urls = f.readlines()
		f.close()

		p_count = 1
		for url in p_urls:
			if url:
				print(f"Downloading Playlist {p_count}")
				url = url.strip('\n')
				self.entire_playlist_download(Playlist_url=url)
				p_count+=1
		print("Full Download Completed")

