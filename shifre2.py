import base64
import os
print(os.system("clear"))
print("\033[1;31m#############################################################")
print("\033[1;31m###################################################   #######")
print("###############################################\033[1;32m   /~\   \033[1;31m#####")
print("############################################\033[1;32m   _- `~~~',\033[1;31m ####")
print("##########################################\033[1;32m  _-~       )  \033[1;31m####")
print("####################################### \033[1;32m _-~          |  \033[1;31m####")
print("#################################### \033[1;32m _-~            ;  \033[1;31m#####")
print("##########################\033[1;32m  __---___-~              |   \033[1;31m#####")
print("#######################   \033[1;32m_~   ,,                  ;  `,,  \033[1;31m##")
print("##################### \033[1;32m _-~    ;'                  |  ,'  ; \033[1;31m##")
print("#####################\033[1;32m  _-~    ;'                  |  ,'  ; \033[1;31m##")
print("############  \033[1;32m __---;                                 ,' \033[1;31m####")
print("######## \033[1;32m  __~~  ___                                ,' \033[1;31m######")
print("#####\033[1;32m `-_         _                              ; \033[1;31m##########")
print("#######\033[1;32m  ~~----~~~   ;                          ; \033[1;31m###########")
print("#########  \033[1;32m/          ;                        ; \033[1;31m############")
print("#######\033[1;32m  /             ;                      ; \033[1;31m#############")
print("##### \033[1;32m /                `                    ; \033[1;31m##############")
print("###  \033[1;32m/                                      ; \033[1;31m###############")
print("### \033[1;32m /                                      ; \033[1;31m###############")
print("#                                            ################")
print("")
print("\033[0;29m_\033[0;36mhelp \033[0;23mand \033[0;36mexit \033[0;23m \033[0;36m\033[0;29m .")
print("\033[0;29m_\033[0;36mthis script is encode and decode text on shifre base64 and base85 and base32 and 16 and a85\033[0;29m .")
print("")
while True:
	awa = input("\033[1;32menter your nember shifre :\033[0;29m")
	if awa != "1":
		if awa != "help":
			if awa != "exit":
				if awa != "2":
					if awa != "3":
						if awa != "4":
							if awa != "5":
								print("\033[0;31mthis","\033[0;26m",awa,"\033[0;31mis not difientid")
	if awa == "1":
		print("\033[0;33mencode == 1 and decode == 2")
		aw = input("enter encode and decode: \033[0;29m")
		if aw  == "1":
			a = input("\033[0;33mencode text ====> :\033[0;29m")
			print("\033[0;32mencode is:\033[0;34m",base64.b64encode(a.encode()))
		try:
			if aw == "2":
				b = input("\033[0;33mdecode text =====> :\033[0;29m")
				print("\033[0;32mdecode is:\033[0;34m",base64.b64decode(b))
			if aw != "1":
				if aw != "2":
					print("\033[0;31mpleas enter 1 or 2")
		except:
			print("\033[0;31mpleas enter text shifre vrai")
	if awa == "2":
		print("\033[0;33mencode == 1 and decode == 2")
		cv = input("enter encode and decode : \033[0;29m")
		if cv == "1":
			c = input("\033[0;33mencode text ====> :\033[0;29m")
			print("\033[0;32mencode is:\033[0;34m",base64.b85encode(c.encode()))
		try:
			if cv == "2":
				d = input("\033[0;33mdecode text ====> :\033[0;29m")
				print("\033[0;32mdecode is:\033[0;34m",base64.b85decode(d))
			if cv != "1":
				if cv != "2":
					print("\033[0;31mpleas enter 1 or 2")
		except:
			print("\033[0;31mpleas enter text shifre vrai")
	if awa == "3":
		print("\033[0;33mencode == 1 and decode == 2")
		nb =input("enter encode and decode:  \033[0;29m")
		if nb == "1":
			e = input("\033[0;33mencode text ====>:\033[0;29m")
			print("\033[0;32mencode is:\033[0;34m",base64.b32encode(e.encode()))
		try:
			if nb == "2":
				f = input("\033[0;33mdecode text ====> :\033[0;29m")
				print("\033[0;32mdecode is:\033[0;34m",base64.b32decode(f))
			if nb != "1":
				if nb != "2":
					print("\033[0;31mpleas enter 1 or 2")
		except:
			print("\033[0;031mpleas enter text shifre vrai")
	if awa == "4":
		print("\033[0;33mencode == 1 and decode == 2")
		vb = input("enter encode and decode: \033[0;29m")
		if vb == "1":
			j = input("\033[0;33mencode text ===> :\033[0;29m")
			print("\033[0;32mencode is:\033[0;34m",base64.b16encode(j.encode()))
		try:
			if vb == "2":
				h = input("\033[0;33mdecode text ====> :\033[0;29m")
				print("\033[0;32mdecode is :\033[0;34m",base64.b16decode(h))
			if vb != "1":
				if vb != "2":
					print("\033[0;31mpleas enter 1 or 2")
		except:
			print("\033[0;31mpleas enter text shifre vrai")			
	if awa == "5":
		print("\033[0;33mencode == 1 and decode== 2")
		jj =input("enter encode and decode:  \033[0;29m")
		if jj == "1":
			i = input("\033[0;33mencode text ====> :\033[0;29m")
			a85 = base64.a85encode(i.encode())
			print("\033[0;32mencode is: \033[0;34m",a85)
		try:
			if jj == "2":
				g = input("\033[0;33mdecode text ====> :\033[0;29m")
				print("\033[0;32mdecode is :\033[0;34m",base64.a85decode(g))
			if jj != "1":
				if jj != "2":
					print("\033[0;31mpleas enter 1 or 2")
		except:
			print("\033[0;31mpleas enter text shifre vrai")
	if awa == "help":
		print("\033[1;33mbase64 enter :1 | encode : 1 ,decode : 2")
		print("base85 enter :2 | encode : 1 ,decode : 2")
		print("base32 enter :3 | encode : 1 ,decode : 2")
		print("base16 enter :4 | encode : 1 ,decode : 2")
		print("a85 enter    :5 | encode : 1 ,decode : 2")
	if awa == "exit":
		break;