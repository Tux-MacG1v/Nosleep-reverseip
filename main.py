import requests,re
from fake_useragent import UserAgent
from multiprocessing import Pool

class Ipto():
	def __init__(  self , ip , proxy = None ,  browser = UserAgent().random ):
		self.ip = ip
		self.website = "https://domains.tntcode.com/ip/%s" % ip
		self.browser = browser

	def __action_to(  self ):
		Headers = {"User-Agent": self.browser,
						"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
									"Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
														"Origin": "https://127.0.0.1", "Connection": "close", "DNT": "1",
																	"Expires": "Null","Referer": "https://127.0.0.1"}
		res = requests.get(self.website  , headers= Headers ).text
		return re.findall( '<a href="/domain/(.+?)"' , res )
		
	def domains_list( self ):
		return self.__action_to()
		
		
def findandsave(ip , trys=False):
	for x in range(5):
		try:
			list = Ipto(ip).domains_list()
			if list:
				[ open("domains.txt",  "a"  , encoding="Latin-1").write("%s\n" % bb ) for bb in list  ]
				print("From this ip ==> %s saved %s domains "  % ( ip  , len(list)     ) )
				break
		except:
			time.sleep(20)
			pass


def main():
	
	smiya = input("[x] list ip : " )
	
	try:
		listip = open( smiya , "r" , encoding="Latin-1" ).read().splitlines()
	except:
		try:
			listip = open( smiya , "r" , encoding="utf-8" ).read().splitlines()
		except:
			print("List Problem !")
			exit()

	ThreadPool = Pool(50)
	ThreadPool.map(findandsave, listip)


if __name__ == "__main__":
	main()
