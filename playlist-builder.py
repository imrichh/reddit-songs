import urllib.request
from bs4 import BeautifulSoup

def main():
	with open("songs-list.txt","r") as f:
		lines = []
		for line in f:
			lines.append(line)

	for line in lines:
		# Inspired: https://stackoverflow.com/questions/45362731/how-can-i-scrape-videos-from-a-youtube-search
		textToSearch = line
		query = urllib.parse.quote(textToSearch)
		url = "https://www.youtube.com/results?search_query=" + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')

		vid = soup.find(attrs={'class':'yt-uix-tile-link'})
		if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
			first_vid = 'https://www.youtube.com' + vid['href'] + "\n"
			with open("yt-links.txt", "a") as yt_file:
				yt_file.write(first_vid)
				print(first_vid)

if __name__ == "__main__":
 	main()