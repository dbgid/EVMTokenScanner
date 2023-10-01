"""DBG ID  Multichain Token Checker
Version : 1.0
Author : Ajones
Supported Chain : ETH, Polygon, BSC.
Bug: May have some bug in some chain, like the website that pure javascript / xhr requests like in polygon chain.
Another chain will come ASAP if Ajones mood to ngoding.
bcoz 'Ngoding doang caer kagak :v'
"""
from requests import get
from colorama import Fore,Style,init
from bs4 import BeautifulSoup as DOM
import argparse,os,threading
from time import sleep
class DbgBlockChain:
  def __init__(self) -> None:
    self.RED = Fore.RED
    self.YELLOW = Fore.YELLOW
    self.BRIGHT = Style.BRIGHT
    self.WHITE = Fore.WHITE
    self.GREEN = Fore.GREEN
    self.bsc_explorer = 'https://bscscan.com/address/'
    self.polygon_explorer = 'https://polygonscan.com/address/'
    self.eth_explorer = 'https://etherscan.com/address/'
    self.bscListToken_element = 'html#html>body#body>main#content>section#ContentPlaceHolder1_divSummary>div:nth-of-type(2)>div>div>div>div#ContentPlaceHolder1_divTokenHolding>div#ContentPlaceHolder1_tokenbalance>div>div#availableBalance>div:nth-of-type(2)>ul>li>div>span'
    self.bscTokenInfo_class = 'a.nav-link.d-flex.justify-content-between.align-items-center.gap-2.px-2'
    self.polygonListToken_element = 'html>body#body>div>main#content>div#ContentPlaceHolder1_divSummary>div>div>div>div:nth-of-type(2)>div#ContentPlaceHolder1_tokenbalance>div>div:nth-of-type(2)>div>a#availableBalanceDropdown>span'
    self.polygonTokenName_class ='span.list-name.hash-tag.text-truncate'
    self.polygonTokenAmount_class ='span.list-amount.link-hover__item.hash-tag.hash-tag--md.text-truncate'
    """end init callable"""
  
  
  def _eth(self,address : str) -> str:
    try:
      r = get(self.eth_explorer+address,headers={'accept':'text/html,text/javascript,*/*','user-agent':'DBG ID Dapps (Android 12/Linux; en-us)'},timeout=30)
      sop = DOM(r.content,'html.parser')
      get_erc20 = sop.select(self.bscListToken_element)
      assert len(get_erc20)!=0,"{0}{1}The wallet {2}{3} is not have any erc20 token yet or have some bug, total token is ({4})".format(self.BRIGHT,self.WHITE,self.RED,address,len(get_erc20))
      get_token_info = sop.select(self.bscTokenInfo_class)
      total_erc20 = get_erc20[0].get_text()
      print(f"{self.BRIGHT}{self.WHITE}[+] Wallet: {self.YELLOW}{address}\n{self.WHITE}[-] {self.GREEN}{total_erc20}")
      res = []
      for i,data in enumerate(get_token_info):
        sc = data.get('href').split('/token/')[1].split("?a=")[0]
        print(f"{self.BRIGHT}{self.WHITE}[{self.YELLOW}{i}{self.WHITE}] {data.get_text()} ( {self.YELLOW}{sc} {self.WHITE})")
        res.append(f"[{i}] "+data.get_text()+" | contract: "+sc)
      result = "\n".join(res)
      with open('listoken.txt','a') as save:
        save.write(f"Wallet: {address} (ETH) \n{result}\n")
        save.close()
    except (AssertionError,Exception) as e:
      print("Error: %s"%str(e))
  """end eth chain"""
  
  
  def _polygon(self,address : str) -> str:
    try:
      r = get(self.polygon_explorer+address,headers={'accept':'text/html,text/javascript,*/*','user-agent':'DBG ID Dapps (Android 12/Linux; en-us)'},timeout=30)
      sop = DOM(r.content,'html.parser')
      get_erc20 = sop.select(self.polygonListToken_element)
      assert len(get_erc20)!=0,"{0}{1}The wallet {2}{3} is not have any erc20 token yet or have some bug, total token is ({4})".format(self.BRIGHT,self.WHITE,self.RED,address,len(get_erc20))
      get_token_name = sop.select(self.polygonTokenName_class)
      get_token_amount = sop.select(self.polygonTokenAmount_class)
      total_erc20 = get_erc20[0].get_text()
      print(f"{self.BRIGHT}{self.WHITE}[+] Wallet: {self.YELLOW}{address}\n{self.WHITE}[-] {self.GREEN}ERC20 w/ or w/o ERC1155 (NFT) Total:  {total_erc20}")
      res = []
      for i,data in enumerate(get_token_name):
        print(f"{self.BRIGHT}{self.WHITE}[{self.YELLOW}{i}{self.WHITE}] {data.get_text()} ( {self.YELLOW}{get_token_amount[i].get_text()} {self.WHITE})")
        res.append(f"[{i}]{data.get_text()} | Token Amount: {get_token_amount[i].get_text()}")
      result = "\n".join(res)
      with open('listoken.txt','a') as save:
        save.write(f"Wallet: {address} (Polygon)\n{result}\n")
        save.close()
    except (AssertionError,Exception) as e:
      print("Error: %s"%str(e))
  """end polygon chain"""
  
  
  def _bsc(self,address : str) -> str:
    try:
      r = get(self.bsc_explorer+address,headers={'accept':'text/html,text/javascript,*/*','user-agent':'DBG ID Dapps (Android 12/Linux; en-us)'},timeout=30)
      sop = DOM(r.content,'html.parser')
      get_bep20 = sop.select(self.bscListToken_element)
      assert len(get_bep20)!=0,"{0}{1}The wallet {2}{3} is not have any bep20 token yet or have some bug, total token is ({4})".format(self.BRIGHT,self.WHITE,self.RED,address,len(get_bep20))
      get_token_info = sop.select(self.bscTokenInfo_class)
      total_bep20 = get_bep20[0].get_text()
      print(f"{self.BRIGHT}{self.WHITE}[+] Wallet: {self.YELLOW}{address}\n{self.WHITE}[-] {self.GREEN}{total_bep20}")
      res = []
      for i,data in enumerate(get_token_info):
        sc = data.get('href').replace('/token/','').replace('?a=%s'%address,'')
        print(f"{self.BRIGHT}{self.WHITE}[{self.YELLOW}{i}{self.WHITE}] {data.get_text()} ( {self.YELLOW}{sc} {self.WHITE})")
        res.append(f"[{i}] "+data.get_text()+" | contract: "+sc)
      result = "\n".join(res)
      with open('listoken.txt','a') as save:
        save.write(f"Wallet: {address} (BSC) \n{result}\n")
        save.close()
    except (AssertionError,Exception) as e:
      print("Error: %s"%str(e))
  """end bsc chain"""
"""end classes"""
def dbgThread(fn):
  def _wrap(*args,**kwargs):
    t = threading.Thread(target=fn,args=args,kwargs=kwargs)
    t.start()
  return _wrap
"""end threading function wrapper"""

class dbgRunner(DbgBlockChain):
  def __init__(self):
    super().__init__()
  
  
  def _clear(self):
    with open('listoken.txt','w') as save:
      save.close()
      print("%s%s[√] File listoken.txt succsesfully cleaned"%(self.BRIGHT,self.GREEN))
  
  def _chain(self,chain : int, file : str):
    try:
      assert os.path.isfile(file)==True,"%s%s%s%s%s%s"%(self.BRIGHT,self.RED,"The file ",file," not found in current directory ",os.getcwd())
      if chain ==1:
        w = open(file,'r').readlines()
        for i, wallet in enumerate(w,1):
          if '\n' in wallet:
            wallet=wallet.replace('\n','')
          print("%s%s[!] Proccess %s%s %s %d of %d"%(self.BRIGHT,self.WHITE,self.YELLOW,wallet,self.WHITE,i,len(w)-1))
          self._bsc(wallet)
          #sleep(2)
      elif chain==2:
        w = open(file,'r').readlines()
        for i, wallet in enumerate(w,1):
          if '\n' in wallet:
            wallet=wallet.replace('\n','')
          print("%s%s[!] Proccess %s%s %s %d of %d"%(self.BRIGHT,self.WHITE,self.YELLOW,wallet,self.WHITE,i,len(w)))
          self._polygon(wallet)
          #sleep(2)
      elif chain==3:
        w = open(file,'r').readlines()
        for i, wallet in enumerate(w,1):
          if '\n' in wallet:
            wallet=wallet.replace('\n','')
          print("%s%s[!] Proccess %s%s %s %d of %d"%(self.BRIGHT,self.WHITE,self.YELLOW,wallet,self.WHITE,i,len(w)))
          self._eth(wallet)
          #sleep(2)
      else:
        raise ValueError("You must select value 1-3. the value only support by number")
    except (AssertionError,Exception) as e:
      print("Error: %s"%str(e))
      
      
if __name__=='__main__':
  parser= argparse.ArgumentParser()
  parser.add_argument('-c','--chain',type=int,help="chainlist: [1] BSC | [2] Polygon | [3] ETH")
  parser.add_argument('-w','--wallet',type=str,help="file list wallet")
  parser.add_argument('-x','--delete',action="store_true",help="clear file listoken.txt")
  args = parser.parse_args()
  lib = dbgRunner()
  file = args.wallet
  chain = args.chain
  if chain and file:
    lib._chain(chain,file)
  elif args.delete:
    lib._clear()
  else:
    print("please type %s -h for help"%os.path.basename(__file__))