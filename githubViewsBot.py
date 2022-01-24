import requests as r
import threading
threadAmount = 10
threadLimit = 300

def ping():
    for i in range(threadLimit):
        r.get("https://camo.githubusercontent.com/366baf4f51992f1e0fd18ae9c34e2bc19159b5d1a3db86dc976b7aa9b8ac8715/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d62617272756c696b")
        print("gotcha")

threads = []
for i in range(threadAmount):
    threads.append(threading.Thread(target=ping))

for i in range(threadAmount):
    threads[i].start()

for i in range(threadAmount):
    threads[i].join()
