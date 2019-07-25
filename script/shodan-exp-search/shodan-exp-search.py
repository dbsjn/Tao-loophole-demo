#! /usr/bin/env python3

import requests
import argparse
import demjson

#使用说明利用shodan 接口 查询历史cve上的漏洞组件信息
#
#
#
#pip install demjson json模块
#pip install argparse 命令行模块
#
#by Greekn 

print ("""

  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █ ▓█████ ▒██   ██▒ ██▓███    ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒███   ░░  █   ░▓██░ ██▓▒░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░░▒████▒▒██▒ ▒██▒▒██▒ ░  ░▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░░░   ░▒ ░░▒ ░     ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░    ░    ░    ░  ░░       ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
      ░   ░  ░  ░    ░ ░     ░          ░  ░         ░    ░  ░ ░    ░                 ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                           ░                                                                                      ░                
"""
)




def shodan(args):
	shodansearch = args.search
	shodankey = args.key
	try:
		data = requests.get("https://exploits.shodan.io/api/search?query="+shodansearch+"&key="+shodankey+"")
		textdata = demjson.decode(data.text)
		print("[+]发送数据成功")
		for i in range(100):
			print ("CVE漏洞编号：","[+]",textdata["matches"][i]["cve"],"\n")
		
	except :
		print("[-]发送数据失败")	
                                                                                                                                           
def main():
	parser = argparse.ArgumentParser()
	parser.description='shodan-exp-search'
	parser.add_argument("-s","--search", help="shodan搜索",type=str,required=True)
	parser.add_argument("-k","--key", help="填写key",type=str,required=True)
	args = parser.parse_args()
	shodan(args)


if __name__== "__main__":
    main()


