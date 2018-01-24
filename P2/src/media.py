#coding=utf-8
import webbrowser
class Movie():
	#增加电影年代movie_year、类型展示movie_type
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,movie_year,movie_type):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_url = trailer_youtube
		self.year = movie_year
		self.mov_type = movie_type

	def show_trailer(self):
	"""输入播放地址，打开播放窗口"""
		webbrowser.open(self.trailer_url)
