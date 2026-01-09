# ================================================================
# OSINT Tool by Gallego-Dev | https://github.com/Gallego-Dev
# Username & IP investigation system | Use responsibly
# ================================================================

import requests
import time
import os

# LISTA DE URLs BASE PARA BUSCA DE USERNAMES
urls_base = [
    # Redes Sociais
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://twitter.com/",
    "https://www.tiktok.com/@",
    "https://www.linkedin.com/in/",
    "https://www.youtube.com/@",
    "https://www.reddit.com/user/",
    "https://www.pinterest.com/",
    "https://www.snapchat.com/add/",

    # Desenvolvimento e TI
    "https://github.com/",
    "https://gitlab.com/",
    "https://bitbucket.org/",
    "https://stackoverflow.com/users/",
    "https://dev.to/",
    "https://codepen.io/",

    # Entretenimento
    "https://www.twitch.tv/",
    "https://steamcommunity.com/id/",
    "https://open.spotify.com/user/",
    "https://soundcloud.com/",
    "https://www.behance.net/",
    "https://dribbble.com/",

    # Fóruns e Comunidades
    "https://www.quora.com/profile/",
    "https://www.flickr.com/people/",
    "https://vk.com/",
    "https://www.patreon.com/",

    # Blogs
    "https://wordpress.com/",
    "https://blogspot.com/",

    # Outros
    "https://keybase.io/",
    "https://www.wikipedia.org/wiki/User:",
    "https://www.tradingview.com/u/",
    "https://imgur.com/user/",
    "https://www.deviantart.com/",
    "https://www.roblox.com/user.aspx?username=",
]

time.sleep(2)

def limpar_msg():
    os.system('cls' if os.name == 'nt' else 'clear')
msg = (r"""##################################################################
# 🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃 - GALLEGO-DEV                                #
# -------------------------------------------------------------- #
# Sistema de análise de usernames e endereços IP                 #
# Autor: Gallego-Dev (https://github.com/Gallego-Dev)            #
# Uso: Pesquisa OSINT legítima apenas                            #
# Versão: 1.0.0 | 2025                                           #
##################################################################""")
print(msg)
time.sleep(4)
limpar_msg()

while True:
    print(r"""                            .__               
   ____  __ _______  ___  __|__| ____   ______
  / ___\|  |  \__  \ \  \/  /  |/    \ /  ___/
 / /_/  >  |  // __ \_>    <|  |   |  \\___ \ 
 \___  /|____/(____  /__/\_ \__|___|  /____  >
/_____/            \/      \/       \/     \/ 
                     .__        __            
          ____  _____|__| _____/  |_          
         /  _ \/  ___/  |/    \   __\         
        (  <_> )___ \|  |   |  \  |           
         \____/____  >__|___|  /__|           
                   \/        \/               
                   """)
    def limpar_menu():
        os.system('cls' if os.name == 'nt' else 'clear')
    menu = (r"""========================================================================
                         🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃 - GALLEGO-DEV
========================================================================

[1] 🔍  BUSCAR USERNAMES
[2] 🌐  INFORMAÇÕES DE IP
[3] 📄  SOBRE A FERRAMENTA
[4] 🚪  SAIR

========================================================================
""")
    print(menu)
    def mensagem():
        print('Escolha uma opção valida!')
    def temp():
        time.sleep(1)

    def buscar_usernames():
        print("=" * 40)
        print("       BUSCA DE USERNAMES       ")
        print("=" * 40)

    def buscar_ip():
        print("=" * 50)
        print("=          ANÁLISE DE ENDEREÇO IP      =")
        print("=" * 50)
        print()
        print(" Formato aceito: IPv4 ou IPv6")
        print(" Exemplos:")
        print("   • 192.168.1.1")
        print("   • 8.8.8.8")
        print("   • 2001:0db8:85a3::1")
        print("=" * 50)

    def sobre_ferramenta():
            print("=" * 40)
            print("=           SOBRE A FERRAMENTA          =")
            print("=" * 40)
            print("=  Nome: 🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃        =")
            print("=  Autor: Gallego-Dev                  =")
            print("=  GitHub: github.com/Gallego-Dev      =")
            print("=                                      =")
            print("=  Descrição:                          =")
            print("=  Ferramenta para análise de         =")
            print("=  usernames e endereços IP.          =")
            print("=                                      =")
            print("=  Uso ético apenas.                  =")
            print("=  Versão: 1.0 | 2024                 =")
            print("=" * 40)
            input("=  Enter para voltar...               =\n" + "=" * 40)
    try:
        opc = int(input('🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃>:'))
    except:
        mensagem()
        temp()
        continue


    if opc == 1:
        limpar_menu()
        temp()
        buscar_usernames()
        user = input('🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃>:')
        print('teste')


    elif opc == 2:
        limpar_menu()
        temp()
        buscar_ip()
        ip = input('🅶🆄🅰🆇🅸🅽🆂-🅾🆂🅸🅽🆃>:')
        continue


    elif opc == 3:
        limpar_menu()
        temp()
        sobre_ferramenta()
        continue


    elif opc == 4:
        limpar_menu()
        break


    else:
        mensagem()
        temp()
        continue




