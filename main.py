import os
import Youtube_Class
from time import sleep
import sys

if __name__ == '__main__':
	Y_Class = Youtube_Class.Youtube()

	while True:
		print("1: To download a single video.")
		print("2: To download a playlist.")
		print("3: To download multiple videos.")
		print("4: To download multiple playlist.")
		print("99: To exit.\n\n")

		choice = int(input("? "))

		if choice == 1:
			v_url = str(input("Enter video url here\n--> "))
			Y_Class.single_video_download(video_url=v_url)
	
		elif choice == 2:
			p_url = str(input("Enter playlist url here\n--> "))
			Y_Class.entire_playlist_download(Playlist_url=p_url)
	
		elif choice == 3:
			input("This script will fetch urls from 'paste_video_url_here.txt' file. Press [Enter] after you have pasted playlist urls in the file.")
			Y_Class.multiple_video_download()
	
		elif choice == 4:
			input("This script will fetch urls from 'paste_playlist_url_here.txt' file. Press [Enter] after you have pasted urls in the file.\n\n")
			Y_Class.multiple_playlist_download()
	
		elif choice == 99:
			print("Exiting ...")
			sleep(3)
			sys.exit()
	
		else:
			print("Incorrect choice\n")

