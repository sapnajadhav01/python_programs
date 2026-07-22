from threading import Thread
import time
class SingleThred(Thread):
    def task1(self):
        print("Preaparing Tea Using Single Thread \n")
        print("Task 1: Boil Milk with tea powder")
        time.sleep(10)
        print("Task 1 completed \n")
    def task2(self):
        print("Task 2: Add Sugar and boil")
        time.sleep(5)
        print("Task 2: Completed \n")    
    def task3(self):
        print("task 3: Filter and Serve Tea")
        time.sleep(2)
        print("Tea is Ready")
    def run(self):
        self.task1()
        self.task2()
        self.task3()
t1=SingleThred()
t1.start()        
