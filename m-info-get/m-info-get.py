#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[36m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'#
Beyaz ='\033[1;37m'

import os
import sys
import requests
import time
import json
try:
    import phonenumbers
except:
    os.system('pip install phonenumbers')
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

def mini_banner():
   print(Kalın+"""

, ＜￣｀ヽ、　　　　　 ／￣＞     
　ゝ、　　＼　／⌒ヽ,ノ  　/         •Welcome To•
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°)／      •Morbius.os's•
　　 　　>　 　 　,)         •Info Get Tool•
　　　　 　∠_,,,/      
{}                                                       
Author: {}
Instagram: {}
Github: {}{}""".format(Yeşil,AUTHOR,INSTAGRAM,GİTHUB,Bitir))
   
def seçim_ekranı():
   print("""
============= {}{}GET İNFO WİTH{} =============
{}[1] {}Phone 
{}[2] {}Nick
{}[3] {}IP 
  
{}[99] EXİT{}
========== {}Coded By Morbius.os{} ==========
  """.format(Kırmızı,AltıÇizili,Bitir,Kırmızı,Bitir,Kırmızı,Bitir,Kırmızı,Bitir,Kırmızı, Bitir, Kırmızı, Bitir))
  
while True:
   mini_banner()
   seçim_ekranı()
   giriş = input('''
{}┌──({}root㉿m-info-get{})-[{}ToolMenu{}]
└─{}# {}m-info-get --seçim '''.format(Mavi,Kırmızı,Mavi, Beyaz,Mavi,Kırmızı,Beyaz))

   if giriş == '1':
       os.system('clear')
       time.sleep(1)
       mini_banner()
       print('\n')
       print(Kalın+'Dünya Genelindeki Bütün Telefon Numaralarında Çalışır')
       print(Kalın+AltıÇizili+'İnternetsizde Çalışır!\n'+Bitir)
       phone = input(f'{Beyaz}Numarayı Giriniz {Yeşil} Örnek = +90xxxxxxxxxx{Beyaz}: {Yeşil}')
       if phone == '0':
           break
       
       default_region = "ID"
       def PhoneGiveİnfo():
            parsed_number = phonenumbers.parse(phone, default_region)
            region_code = phonenumbers.region_code_for_number(parsed_number)
            jenis_provider = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "id")
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            is_possible_number = phonenumbers.is_possible_number(parsed_number)
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
            number_type = phonenumbers.number_type(parsed_number)
            timezone1 = timezone.time_zones_for_number(parsed_number)
            timezoneF = ', '.join(timezone1)
            print(f'============={Yeşil} PHONE İNFORMATİON {Bitir}=============')
            print(f"\n {Beyaz}Location             :{Yeşil} {location}")
            print(f" {Beyaz}region Code          :{Yeşil} {region_code}")
            print(f" {Beyaz}Timezone             :{Yeşil} {timezoneF}")
            print(f" {Beyaz}Operator             :{Yeşil} {jenis_provider}")
            print(f" {Beyaz}Valid number         :{Yeşil} {is_valid_number}")
            print(f" {Beyaz}Possible number      :{Yeşil} {is_possible_number}")
            print(f" {Beyaz}International format :{Yeşil} {formatted_number}")
            print(f" {Beyaz}Mobile format        :{Yeşil} {formatted_number_for_mobile}")
            print(f" {Beyaz}Original number      :{Yeşil} {parsed_number.national_number}")
            print(f" {Beyaz}E.164 format         :{Yeşil} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
            print(f" {Beyaz}Country code         :{Yeşil} {parsed_number.country_code}")
            print(f" {Beyaz}Local number         :{Yeşil} {parsed_number.national_number}")
            if number_type == phonenumbers.PhoneNumberType.MOBILE:
                print(f" {Beyaz}Type                 :{Yeşil} This is a mobile number")
            elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                print(f" {Beyaz}Type                 :{Yeşil} This is a fixed-line number")
            else:
                print(f" {Beyaz}Type                 :{Yeşil} This is another type of number")

       if __name__ == '__main__':
            PhoneGiveİnfo()
            time.sleep(10)
            os.system('clear')
   
   elif giriş == '2':
       os.system('clear')
       time.sleep(1)
       mini_banner()
       print('\n')
       
       def TrackUserName(username):
            results = {}
            social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
            ]

            for site in social_media:
                url = site['url'].format(username)
                response = requests.get(url)
                if response.status_code == 200:
                    results[site['name']] = url
                else:
                    results[site['name']] = (f"{Sarı}Username Bulunamadı {Sarı}!")
            return results
       username = input(f"\n {Beyaz}Nick'i Yazınız : {Yeşil}")
       print(f"\n {Beyaz}========== {Yeşil} USERNAME İNFO {Beyaz}==========")
       print()
       results = TrackUserName(username)
       for site, url in results.items():
           print(f" {Beyaz}[ {Yeşil}+ {Beyaz}] {site} : {Yeşil}{url}")
   
   elif giriş == '3':
       os.system('git clone https://github.com/morbius-os/m-location')
       os.system('clear')
       time.sleep(1)
       mini_banner()
       time.sleep(2)
       os.system('cd m-ip-to-location')
       os.system('python3 m-location-v2.py')
       time.sleep(10)
       
   elif giriş == '99':
       os.system('clear')
       print(f'''{Yeşil}
Toolumu kullandığınız için teşekkür ederim.
                                           {Bitir}{Kalın} ~Morbius.os
       ''')
       time.sleep(2)
       sys.exit()
   
   else:
       print(f'{Kırmızı}{Kalın}Böyle bir seçim yok. Lütfen düzgün bir seçim yapınız')