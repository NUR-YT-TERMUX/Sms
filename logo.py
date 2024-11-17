import os,sys,time

def sty(sty):
	for x in sty+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.009)
		
		
def sty2(sty2):
	for x in sty2+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.003)
		

def sty3(sty3):
	for x in sty3+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.01)
		
		
class logo:
	@classmethod
	def logox(self):
		print('''\033[1;37m

  
  
███╗   ██╗██╗   ██╗██████╗     ██╗   ██╗████████╗
████╗  ██║██║   ██║██╔══██╗    ╚██╗ ██╔╝╚══██╔══╝
██╔██╗ ██║██║   ██║██████╔╝     ╚████╔╝    ██║   
██║╚██╗██║██║   ██║██╔══██╗      ╚██╔╝     ██║   
██║ ╚████║╚██████╔╝██║  ██║       ██║      ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝       ╚═╝      ╚═╝   
                                                 \033[1;31mV2''')
                                                 
                                                 
	@classmethod
	def logo1(self):
		sty('''\033[1;37m


  
███╗   ██╗██╗   ██╗██████╗     ██╗   ██╗████████╗
████╗  ██║██║   ██║██╔══██╗    ╚██╗ ██╔╝╚══██╔══╝
██╔██╗ ██║██║   ██║██████╔╝     ╚████╔╝    ██║   
██║╚██╗██║██║   ██║██╔══██╗      ╚██╔╝     ██║   
██║ ╚████║╚██████╔╝██║  ██║       ██║      ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝       ╚═╝      ╚═╝   
                                            \033[1;31mV2''')

class menux:
	@classmethod
	def menu3(self):
		print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mCREATOR      \033[1;31m:  \033[1;32mASSADUZZMAN NUR")
		print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mGITHUB      \033[1;31m:  \033[1;32mNUR-YT-TERMUX")
		print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mTELEGRAM    \033[1;31m:  \033[1;32mNUR100")
		print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mTOOL       \033[1;31m:  \033[1;32mSMS-BOOMING")
		
		
	@classmethod
	def menu2(self):
		sty("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mCREATOR      \033[1;31m:  \033[1;32mASSADUZZMAN NUR")
		sty("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mGITHUB      \033[1;31m:  \033[1;32mNUR-YT-TERMUX")
		sty("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mTELEGRAM    \033[1;31m:  \033[1;32mNUR100")
		sty("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mTOOL       \033[1;31m:  \033[1;32mSMS-BOOMING")
		
	@classmethod
	def menu1(self):
		sty("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mCREATOR      \033[1;31m:  \033[1;32mASSADUZZMAN NUR")
		sty("\033[1;33m[\033[1;31m01\033[1;33m]  \033[1;37mGITHUB      \033[1;31m:  \033[1;32mNUR-YT-TERMUX")
		sty("\033[1;33m[\033[1;31m02\033[1;33m]  \033[1;37mTELEGRAM    \033[1;31m:  \033[1;32mNUR100")
		sty("\033[1;33m[\033[1;31m03\033[1;33m]  \033[1;37mTOOL       \033[1;31m:  \033[1;32mSMS-BOOMING")
		
		
		
