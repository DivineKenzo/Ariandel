#!/usr/bin/env python3
def main(): 
     import datetime
     import time
     try:
          while True:    
               current_time = datetime.datetime.now()
               print(current_time.strftime(" %H:%M:%S"), end='\r')
               time.sleep(5)
     except KeyboardInterrupt:
          print(" Действие отменено пользователем")

if __name__ == "__main__":
    main()