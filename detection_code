#Import the needed packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
from tkinter import *
import sys
from threading import Thread

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#Import the unknown support file from the same directory
import unknown_support
    
#Prepare the variables for the webnav() function
password_entered = False
runtime_menu_clicked = False
restart_runtime_clicked = False
run_all_clicked = False
code_page_loaded = False
mount_button_clicked= False
connect_button_clicked = False
runtime_loaded = False
drive_fully_mounted = False
focus_switched_to_output = False
number_of_people = ""
continue_restart = False

global driver
#As this app uses firefox in RPi, the webdriver is changed
driver = webdriver.Firefox()


#This function creates the GUI making use of the class mainLevel defined later
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = mainLevel (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None

#Creates the mainLevel window
def create_mainLevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_mainLevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = mainLevel (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

#Destroys the mainLevel window
def destroy_mainLevel():
    global w
    w.destroy()
w = None
 
#Webnav function, exact same as Appendix C but the variables are now global
def webnav():
    
    global password_entered 
    global runtime_menu_clicked 
    global restart_runtime_clicked
    global run_all_clicked 
    global code_page_loaded 
    global mount_button_clicked
    global connect_button_clicked 
    global runtime_loaded 
    global drive_fully_mounted  
    global number_of_people
    global focus_switched_to_output
    global continue_restart
    global driver
        
#Selenium uses the web driver to open the browser at the URL specified. This URL takes the browser through a sign-in process
#That then redirects to the Google Colab page, which eases the process.
driver.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://colab.research.google.com/drive/1K2HZv3Cm-0X5QPTzdHTIKAU6GbdcJsfS#scrollTo=AqgpW9DnwbLf")

#As soon as the first page is fully loaded, the application looks for the username input box, and once it's found it will input
#the correct credentials and continue
username = driver.find_element_by_name("identifier")
username.clear()
username.send_keys("lopezrui.ethan@gmail.com", Keys.ENTER)

    
#This and every other while loop ensures that the page is fully loaded (i.e. the correct elements within a website are found)
#before carrying on with the code. 
while password_entered == False:
    try:
        #The password box is searched, and if found the correct credentials are input and then the system will continue
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("ENGR300lopezrui")
        password.send_keys(Keys.ENTER)
        #If the application has been successful in finding the element and finished processing it, the application then
        #exits the while loop and continues
        password_entered = True
    except:
        #If the system throws an error (i.e. the element hasn't been found) the variable stays false and the applications 
        #attempts to look for the element again, until it has been found.
        password_entered = False     

while code_page_loaded == False:
    try:
        #Once the file tab button is available to be clicked, the application knows that the page has been loaded and it attempts
        #to open the tab.
        files_button = driver.find_element_by_xpath("/html/body/div[7]/div[2]/colab-left-pane/div/paper-listbox/paper-item[3]/paper-icon-button")
        files_button.click()
        code_page_loaded = True
    except:
        code_page_loaded = False

while runtime_loaded == False:
    try:
        #Application looks for the text inside the Mount Drive button to figure out if the Drive has been mounted or not
        drive_mounted_text = driver.find_element_by_xpath("/html/body/div[7]/div[2]/colab-left-pane/colab-resizer/div[1]/iron-pages/colab-file-browser/colab-file-tree/div[1]/div/colab-toolbar-button[3]/span").text
        runtime_loaded = True
    except:
        runtime_loaded = False

#As the Drive isn't mounted by default usually, it is important that the system checks if it has been mounted or not before proceeding     
if drive_mounted_text == "Mount Drive":
    #The mount drive button is clicked
    while mount_button_clicked == False:
        try:
            mount_drive_button = driver.find_element_by_xpath("/html/body/div[7]/div[2]/colab-left-pane/colab-resizer/div[1]/iron-pages/colab-file-browser/colab-file-tree/div[1]/div/colab-toolbar-button[3]")
            mount_drive_button.click()
            mount_button_clicked = True
        except:
            mount_button_clicked = False

    #A pop up comes up to confirm, the confirm button is clicked
    while connect_button_clicked == False:
        try:
            connect_button = driver.find_element_by_xpath("/html/body/colab-dialog/paper-dialog/div[2]/paper-button[2]")
            connect_button.click()
            connect_button_clicked = True
        except:
            connect_button_clicked = False

    #The system then checks that the drive has been mounted successfully before proceeding by checking that the 'drive' folder is in the 
    #file browser in the file tab. 
    while drive_fully_mounted == False:
        try:
            drive_confirmation = driver.find_element_by_xpath("/html/body/div[7]/div[2]/colab-left-pane/colab-resizer/div[1]/iron-pages/colab-file-browser/colab-file-tree/div[3]/colab-file-view/div/colab-file-view[1]")
            if drive_confirmation.text == "drive":
                drive_fully_mounted = True   
        except:
            drive_fully_mounted = False

#The application then opens the 'Runtime' tab at the top to prepare for the next click, as the button must be on show to be clicked
while runtime_menu_clicked == False:
    try:
        runtime_menu = driver.find_element_by_id("runtime-menu-button")
        runtime_menu.click()
        runtime_menu_clicked = True
    except:
        runtime_menu_clicked = False

#The 'Run all' button is clicked
while run_all_clicked == False:
    try:
        run_all = driver.find_element_by_id(":1t")
        run_all.click()
        run_all_clicked = True
    except:
        run_all_clicked = False



#The mainLevel class defines every widget within the root level and the main window itself
class mainLevel:
    def __init__(self, top=None): 

        
        global numberLabel
        global activateWebscraping
        global activateLivestream

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Dominican} -size 24 -weight bold"
        font9 = "-family {Dominican} -size 14 -weight bold"

        #the top level features are set
        top.geometry("1920x1080")
        top.minsize(232, 1)
        top.maxsize(11524, 3859)
        top.resizable(0, 0)
        top.title("Video Detection Software")
        top.configure(background="#2D142C")
        top.configure(highlightbackground="#f0f0f0f0f0f0")

        #This label simply tells the user where the number is 
        dummyLabel = tk.Label(top)
        dummyLabel.place(relx=0.115, rely=0.111, height=80, width=639)
        dummyLabel.configure(background="#2D142C")
        dummyLabel.configure(cursor="fleur")
        dummyLabel.configure(disabledforeground="#000000")
        dummyLabel.configure(font=font9)
        dummyLabel.configure(foreground="#EE4540")
        dummyLabel.configure(text='''Number of people within sight:''')
        
        #This label is the number that updates constantly with the extract from Google Colab
        numberLabel = tk.Label(top)
        numberLabel.place(relx=0.115, rely=0.241, height=642, width=639)
        numberLabel.configure(background="#2D142C")
        numberLabel.configure(disabledforeground="#a3a3a3")
        numberLabel.configure(font=font10)
        numberLabel.configure(foreground="#C72C41")
        numberLabel.configure(text='''0''')
        numberLabel.configure(wraplength="600")   
        
        #This button activates the extraction of information
        activateWebscraping = tk.Button(top)
        activateWebscraping.place(relx=0.552, rely=0.611, height=120
                , width=640)
        activateWebscraping.configure(activebackground="#ececec")
        activateWebscraping.configure(activeforeground="#000000")
        activateWebscraping.configure(background="#C72C41")
        activateWebscraping.configure(cursor="fleur")
        activateWebscraping.configure(disabledforeground="#a3a3a3")
        activateWebscraping.configure(font=font9)
        activateWebscraping.configure(foreground="#510A32")
        activateWebscraping.configure(highlightbackground="#d9d9d9")
        activateWebscraping.configure(highlightcolor="black")
        activateWebscraping.configure(pady="0")
        activateWebscraping.configure(text='''Activate Webscraping''')
        #This line assigns the function to the button
        activateWebscraping.configure(command=activate_webscraping)
      
#This function extracts the information constantly from the Google colab webpage (same as Appendix D)
def activate_webscraping():
    
    global initialised
    webscrape_on = True
    global driver
    initialised = False
        
    while webscrape_on == True:
        try:
            driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/div/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe"))
            output_number = driver.find_element_by_xpath("/html/body/div/div/div/div/pre")
            number_of_people = output_number.text
            if number_of_people[0].isdigit():
                print(number_of_people)
                initialised = True
                numberLabel.configure(text=str(number_of_people))
            else:
                break
        except:
            if initialised == False:
                numberLabel.configure(text="Loading...")
            elif initialised == True:
                numberLabel.configure(text=str(number_of_people))
            else:
                True
        #These two lines were added to ensure reliability and update the GUI respectively
        driver.switch_to.default_content()
        numberLabel.update()
            

#The two functions are running in parallel using multithreading
if __name__ == '__main__':
    Thread(target = webnav).start()
    Thread(target = vp_start_gui).start()




