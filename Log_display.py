# getmtime and getctime

import os.path, time
old_date_time = ""
while True:
    new_date_time = time.ctime(os.path.getmtime("C:/Users/sogangadhara/PycharmProjects/untitled/temp.txt"))

    if old_date_time != new_date_time:
        old_date_time = new_date_time
        f = open("C:/Users/sogangadhara/PycharmProjects/untitled/temp.txt", "w+")
        lines = f.readlines()
        for l in lines:
            print(l)


