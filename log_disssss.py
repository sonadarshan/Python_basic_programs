import os.path, time
while True:
     print(time.ctime(os.path.getmtime("C:/Users/sogangadhara/PycharmProjects/untitled/temp.txt")))
     time.sleep(30)