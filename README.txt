prerequisite(python should be installed)

1.open console 

2. install selenium
                     pip install selenium


3.chromedriver and the excel file should be in the same folder as the script(i.e 5.py)

4.Paste all the numbers you want to send messages to in the excel sheet in the first column

5.open the console window and navigate it to the script file. 
               eg:- cd C:\Users\USER\Desktop\intern proj

6.in the console window run the script and enter the excel file name in the next line
               
               python 5.py "(message here)"
               excelname.xlsx
               
               eg:- python 5.py "Greetings, you have been shortlisted"
                    no1.xlsx

7. After the file execution another chrome window open and navigates by itself

8. Wait for the web.whatsapp.com to open and ask for login through QR code scan

9. Login into whatsapp web through your mobile. After this step no further actions needed. 

10. The message will be sent to all the mobile no. listed in the excel sheet.
NOTE: If there is an error with the chrome driver you can install the latest version from 
         (https://chromedriver.chromium.org/downloads)and replace it with the orignal. 
