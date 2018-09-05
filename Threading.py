import threading

def thread_job():   #線程工作內容
    print('Test threading job')

def thread_job2():
    print('Test threading job2')

def main():
   thread1 = threading.Thread(target=thread_job)#設定工作位置
   thread1.start()
   thread2 = threading.Thread(target=thread_job2)  # 設定工作位置
   thread2.start()
if __name__ == '__main__':
    main()

