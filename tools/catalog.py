import requests
import time
import colorama
from colorama import Fore
import os

os.system("clear")


colorama.init()


print ("ИЩИ КАТАЛОГИ НА САЙТАХ, В КОНЦЕ URL ДОБАВЬ /")
print ("")
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}



#ok

def search():
    #linux
    url = input("[=]URL>")
    

    adm = [
    'admin',
    'administrator',
    'adminpanel',
    'login',
    'controlpanel',
    'dashboard',
    'manage',
    'backend',
    'panel',
    'wp-admin',
    'user',
    'secure',
    'paneladmin',
    'cpanel',
    'siteadmin',
    'webadmin',
    'auth',
    'access',
    'settings',
    'config',
    'system',
    'backendpanel',
    'management',
    'administratorpanel',
    'useradmin',
    'portal',
    'secureadmin',
    'dashboardpanel',
    'adminarea',
    'settingspanel',
    'usercontrol',
    'adminlogin',
    'adminconsole',
    'sitecontrol',
    'adminzone',
    'backendlogin',
    'control',
    'admininterface',
    'adminhome',
    'systemadmin',
    'configuration',
    'adminroot',
    'controlroom',
    'adminaccess',
    'administration',
    'memberadmin',
    'siteadminpanel',
    'adminsettings',
    'adminspace',
    'userpanel'
]
# rasdel



    kt = [
    'blog',
    'users',
    'settings',
    'content',
    'reports',
    'security',
    'access',
    'logging',
    'support',
    'integrations',
    'monitoring',
    'dashboard',
    'analytics',
    'notifications',
    'roles',
    'permissions',
    'database',
    'backup',
    'restore',
    'performance',
    'activity',
    'api',
    'data',
    'status',
    'updates',
    'customization',
    'themes',
    'plugins',
    'modules',
    'configuration',
    'logs',
    'session',
    'feedback',
    'groups',
    'search',
    'billing',
    'invoices',
    'subscriptions',
    'transactions',
    'reports',
    'visualization',
    'segmentation',
    'testing',
    'settings',
    'sitemap',
    'cache',
    'firewall',
    'certificates',
    'registration',
    'policies',
    'authentication',
    'verification',
    'products',
    'orders',
    'inventory',
    'shipping',
    'payment',
    'discounts',
    'promotions',
    'support',
    'tickets',
    'knowledge',
    'community',
    'feedback',
    'requests',
    'reports',
    'logs',
    'settings',
    'notifications',
    'engagement',
    'integration',
    'metrics',
    'configuration',
    'retention',
    'privacy',
    'terms',
    'consent',
    'compliance',
    'accessibility',
    'mobile',
    'multi-language',
    'scheduling',
    'tutorials',
    'mapping',
    'cleaning',
    'validation',
    'insights',
    'fields',
    'tags',
    'categories',
    'sources',
    'segmentation',
    'metadata',
    'parameters',
    'variables',
    'elements',
    'settings',
    'options',
    'features',
    'modules',
    'components',
    'widgets',
    'dashboard',
    'profiles',
    'roles',
    'permissions',
    'settings'
]

    print ('1. Поиск админ панели')
    print ('2. Поиск других каталогов')
    print (Fore.BLUE + '')

    usvb = input("Выерите значение:")

    

    if usvb == "1":
        for term in adm:
            
            res = requests.get(url + term, headers=headers)
            print (Fore.BLUE + '')
            if (res.status_code) == 200:
                print ("+ Запрос отправлен:", term, Fore.YELLOW + "Успешно найдено")
                
            else:
                print ("+ Запрос отправлен:", term, Fore.RED + "No katalog")
                
    else:
        for ln in kt:
            
            res = requests.get(url + ln, headers=headers)
            print (Fore.BLUE + '')
            if (res.status_code) == 200:
                print ("+ Запрос отправлен:", ln, Fore.YELLOW + "Успешно найдено")
                
            else:
                print ("+ Запрос отправлен:", ln, Fore.RED + "No katalog")






search()
#the end


print ("")
i = input("Нажмите Enter")
#f = open("bs.txt",  "r")
os.system("clear")
os.system("python3 NEXUS.py")



