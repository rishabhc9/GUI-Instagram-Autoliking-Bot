from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def botfunction():
        path='/Users/apple/Downloads/chromedriver'
        driver=webdriver.Chrome(path)
        driver.get('https://www.instagram.com/')
        wait=WebDriverWait(driver,10)
        uname = wait.until(ec.visibility_of_element_located((By.NAME, "username")))
        uname.send_keys(f'{e3.get()}')
        pwd=wait.until(ec.visibility_of_element_located((By.NAME,"password")))
        pwd.send_keys(f'{e4.get()}')
        pwd.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get(f'https://www.instagram.com/explore/tags/{e1.get()}')
        time.sleep(4)
        driver.find_element_by_class_name('_9AhH0').click()
        for i in range(int(e2.get())):
                time.sleep(3)
                driver.find_element_by_class_name('fr66n').click()
                time.sleep(1)
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                i=+1
        time.sleep(2)
        driver.quit()
     
window = Tk()
window.geometry("448x112")
window.title("Rishabh's Instagram Bot")
window['background']='#8c4d5d'
label_text=StringVar()

Label(window,bg='#fec89a',fg='#8c4d5d', text="Hashtag To Search:          ").grid(row=2, sticky=W)
Label(window,bg='#fec89a', fg='#8c4d5d',text="Number Of Posts To Like:").grid(row=3, sticky=W)
Label(window, bg='#fec89a',fg='#8c4d5d',text="Instagram Username:       ").grid(row=0, sticky=W)
Label(window,bg='#fec89a',fg='#8c4d5d', text="Instagram Password:        ").grid(row=1, sticky=W)

e1 = Entry(window,relief=RIDGE,fg='#fec89a',bg='#8c4d5d')
e2 = Entry(window,relief=RIDGE,fg='#fec89a',bg='#8c4d5d')
e3 = Entry(window,relief=RIDGE,fg='#fec89a',bg='#8c4d5d')
e4 = Entry(window,relief=RIDGE,fg='#fec89a',bg='#8c4d5d')

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=0, column=1)
e4.grid(row=1, column=1)
 
b = Button(window, text="Run Bot", command=botfunction, fg='#8c4d5d',relief=RAISED)
b.grid(row=1, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

mainloop()

 