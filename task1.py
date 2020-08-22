import os
import pyttsx3
print('================================================================================================================================================')
print('                                                                  Chat Bot                                                                      ')
print('================================================================================================================================================')
pyttsx3.speak('Hello User,Please enter your name')
name=input('Enter your name here : ')

pyttsx3.speak('Hey '+name+' , What can I do for you')
command=input('What do you want to do : ')

if(command=='Open Google Chrome'):
    pyttsx3.speak('Enter url which you want to open on chrome')
    chrome=input('Enter the url which you want to open with Google Chrome : ')
    os.system('start chrome '+chrome)

elif(command=='Open Notepad'):
    pyttsx3.speak('Enter file name')
    notepad=input('Enter the filename (with extension) which you want to open with Notepad : ')
    os.system('notepad '+notepad)

elif(command=='Show Date'):
    pyttsx3.speak('You requested for date')
    os.system('date /t')

elif(command=='Show Time'):
    pyttsx3.speak('You requested for time')
    os.system('time /t')

elif(command=='Clear Screen'):
    pyttsx3.speak('Clearing the Screen')
    os.system('cls')

elif(command=='Clear Screen And Run Bot'):
    pyttsx3.speak('You entered Clear Screen And Run Bot ')
    os.system('cls')
    os.system('python task1.py')

elif(command=='Check Internet Connectivity'):
    pyttsx3.speak('Enter valid I P Address')
    ip=input('Enter valid IP Address : ')
    os.system('ping '+ip)
    os.system('cls')
elif(command=='Show Me My IP'):
    pyttsx3.speak('I P will be displayed shortly')
    os.system('ipconfig')
elif(command=='Hard Disk Status'):
    os.system('diskpart')
    """ print('Enter 1 to list all the disks')
    print('Enter 2 to list all the volumes')
    choice=input('Enter Choice :')
    if(choice==1):
        os.system('list disk')
    elif(choice==2):
        os.system('list volumes') """
elif(command=='Sleep System'):
    pyttsx3.speak('Enter Amount of time')
    amt=input('Enter amount of time : ')
    os.system('timeout '+amt)
else:
   print('Wrong Choice')
   pyttsx3.speak('You had entered wrong choice');
    

