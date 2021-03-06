#!/usr/bin/env python

import urllib2, urllib
import json
import os
from sys import stdout, exit
from time import sleep

os.system("clear")

print (''' \033[1;32;40m=============================================================================================\033[0m
\033[1;32;40m =\033[1;31;40m  /$$$$$$$  /$$$$$$$$ /$$$$$$          /$$                     /$$$$$$ /$$$$$$$  /$$$$$$$  \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$__  $$|__  $$__//$$__  $$        | $$                    |_  $$_/| $$__  $$| $$__  $$ \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$  \ $$   | $$  | $$  \__/       /$$$$$$    /$$$$$$         | $$  | $$  \ $$| $$  \ $$ \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$$$$$$    | $$  | $$            |_  $$_/   /$$__  $$        | $$  | $$  | $$| $$$$$$$/ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$__  $$   | $$  | $$              | $$    | $$  \ $$        | $$  | $$  | $$| $$__  $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$  \ $$   | $$  | $$    $$        | $$ /$$| $$  | $$        | $$  | $$  | $$| $$  \ $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$$$$$$/   | $$  |  $$$$$$/        |  $$$$/|  $$$$$$/       /$$$$$$| $$$$$$$/| $$  | $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m |_______/    |__/   \______/          \___/   \______/       |______/|_______/ |__/  |__/ \033[1;32;40m=\033[0m''')
print " \033[1;32;40m=============================================================================================\033[0m"
print " \033[1;37;40m[+] Tools to check the exchange rate virtual money currency to Indonesia Rupiah           [+]\033[0m"
print " \033[1;37;40m[+] Code by : Bayu Fedra                                                                  [+]\033[0m"
print " \033[1;37;40m[+] Github  : https://github.com/B3yeZ/  || FB : Bayu Fedra  ||  Intagram: @bayufedraa    [+]\033[0m"
print " \033[1;37;40m[+] API VIA Btcoin.co.id                                                                  [+]\033[0m"
print " \033[1;32;40m=============================================================================================\033[0m"

def main():
	try:
		#BTC
		api_btc = "https://vip.bitcoin.co.id/api/btc_idr/ticker"
		res_btc = urllib2.urlopen(api_btc)
		wibu_btc = res_btc.read()
		halah_btc = json.loads(wibu_btc)
		last_btc = halah_btc["ticker"]
		harga_btc = int(last_btc["last"])

		#BCH
		api_bch = "https://vip.bitcoin.co.id/api/bch_idr/ticker"
		res_bch = urllib2.urlopen(api_bch)
		wibu_bch = res_bch.read()
		halah_bch = json.loads(wibu_bch)
		last_bch = halah_bch["ticker"]
		harga_bch = int(last_bch["last"])

		#BTG
		api_btg = "https://vip.bitcoin.co.id/api/btg_idr/ticker"
		res_btg = urllib2.urlopen(api_btg)
		wibu_btg = res_btg.read()
		halah_btg = json.loads(wibu_btg)
		last_btg = halah_btg["ticker"]
		harga_btg = int(last_btg["last"])
		
		#ETH
		api_eth = "https://vip.bitcoin.co.id/api/eth_idr/ticker"
		res_eth = urllib2.urlopen(api_eth)
		wibu_eth = res_eth.read()
		halah_eth = json.loads(wibu_eth)
		last_eth = halah_eth["ticker"]
		harga_eth = int(last_eth["last"])
		
		#ETC
		api_etc = "https://vip.bitcoin.co.id/api/etc_idr/ticker"
		res_etc = urllib2.urlopen(api_etc)
		wibu_etc = res_etc.read()
		halah_etc = json.loads(wibu_etc)
		last_etc = halah_etc["ticker"]
		harga_etc = int(last_etc["last"])
		
		#LTC
		api_ltc = "https://vip.bitcoin.co.id/api/ltc_idr/ticker"
		res_ltc = urllib2.urlopen(api_ltc)
		wibu_ltc = res_ltc.read()
		halah_ltc = json.loads(wibu_ltc)
		last_ltc = halah_ltc["ticker"]
		harga_ltc = int(last_ltc["last"])
		
		#NXT
		api_nxt = "https://vip.bitcoin.co.id/api/nxt_idr/ticker"
		res_nxt = urllib2.urlopen(api_nxt)
		wibu_nxt = res_nxt.read()
		halah_nxt = json.loads(wibu_nxt)
		last_nxt = halah_nxt["ticker"]
		harga_nxt = int(last_nxt["last"])
		
		#Waves
		api_waves = "https://vip.bitcoin.co.id/api/waves_idr/ticker"
		res_waves = urllib2.urlopen(api_waves)
		wibu_waves = res_waves.read()
		halah_waves = json.loads(wibu_waves)
		last_waves = halah_waves["ticker"]
		harga_waves = int(last_waves["last"])
		
		#XLM -> API Intterupt
		api_xlm = "https://vip.bitcoin.co.id/api/str_idr/ticker"
		res_xlm = urllib2.urlopen(api_xlm)
		wibu_xlm = res_xlm.read()
		halah_xlm = json.loads(wibu_xlm)
		last_xlm = halah_xlm["ticker"]
		harga_xlm = int(last_xlm["last"])
		
		#XRP
		api_xrp = "https://vip.bitcoin.co.id/api/xrp_idr/ticker"
		res_xrp = urllib2.urlopen(api_xrp)
		wibu_xrp = res_xrp.read()
		halah_xrp = json.loads(wibu_xrp)
		last_xrp = halah_xrp["ticker"]
		harga_xrp = int(last_xrp["last"])

		#XZC
		api_xzc = "https://vip.bitcoin.co.id/api/xzc_idr/ticker"
		res_xzc = urllib2.urlopen(api_xzc)
		wibu_xzc = res_xzc.read()
		halah_xzc = json.loads(wibu_xzc)
		last_xzc = halah_xzc["ticker"]
		harga_xzc = int(last_xzc["last"])
	
		print " [+] Bitcoin to Indonesia Rupiah          : Rp.{:,.0f}".format(harga_btc) + " /BTC"
		print " [+] Bitcoin Cash to Indonesia Rupiah     : Rp.{:,.0f}".format(harga_bch) + "  /BCH"
		print " [+] Bitcoin Gold to Indonesia Rupiah     : Rp.{:,.0f}".format(harga_btg) + "   /BTG"
		print " [+] Ethereum to Indonesia Rupiah         : Rp.{:,.0f}".format(harga_eth) + "  /ETH"
		print " [+] Ethereum Classic to Indonesia Rupiah : Rp.{:,.0f}".format(harga_etc) + "     /ETC"
		print " [+] Litecoin to Indonesia Rupiah         : Rp.{:,.0f}".format(harga_ltc) + "   /LTC"
		print " [+] NXT to Indonesia Rupiah              : Rp.{:,.0f}".format(harga_nxt) + "      /NXT"
		print " [+] Waves to Indonesia Rupiah            : Rp.{:,.0f}".format(harga_waves) + "     /Waves"
		print " [+] Stellar Lumens to Indonesia Rupiah   : Rp.{:,.0f}".format(harga_xlm) + "       /XLM"
		print " [+] Ripple to Indonesia Rupiah           : Rp.{:,.0f}".format(harga_xrp) + "      /XRP"
		print " [+] Zcoin to Indonesia Rupiah            : Rp.{:,.0f}".format(harga_xzc) + "   /XZC"
		print "\033[F"*12
	except:
		print "\n\n\n\n\n\n\n\n\n\n\n"
		print "\033[1;31;40m [+] Your Connection is slow or you was press to exiting the program\033[0m"
		x = raw_input("\033[1;37;40m [+] Exit the program (Y/N) : \033[0m")
		if x == "y" or x == "Y" or x == "Yes" or x == "YES":
			bayu = "Exiting The Program..."
			fedra = ""
			for i in bayu:
				fedra += i
				stdout.write("\r \033[1;33;40m[+] %s" %fedra)
				stdout.flush()
				sleep(0.1)
			print "\n \033[1;33;40m[+] Happy Mining \033[0m"
			exit(0)
		elif x == "n" or x == "N" or x == "No" or x == "NO":
			print "\033[F"*2
			stdout.write("                                                                    ")
			stdout.flush()                                                                    
			print "\033[F"*2                                                                  
			stdout.write("                                                                    ")
			stdout.flush()                                                                    
			print "\033[F"*13                                                                 
			pass                                                                              
		else:                                                                                 
			print "\033[F"*2                                                                  
			stdout.write("                                                                    ")
			stdout.flush()                                                                    
			print "\033[F"*2                                                                  
			stdout.write("                                                                    ")
			stdout.flush()
			print "\033[F"*13
			pass
		
while True:
    try:
        main()
    except KeyboardInterrupt:
		print "\n\n"
		bayu = "Exiting The Program..."
		fedra = ""
		for i in bayu:
			fedra += i
			stdout.write("\r \033[1;33;40m[+] %s" %fedra)
			stdout.flush()
			sleep(0.1)
		print "\n \033[1;33;40m[+] Happy Mining \033[0m"
		exit(0)