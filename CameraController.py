import cv2
import collections
import threading
import numpy as np
import time

class CameraController(): 
    
    def __init__(self, buf_len):
        self.buf_len = buf_len
        self.m_vFrameBuffer = collections.deque(maxlen=buf_len)

        self.m_inFrameCounter = 0
        self.m_outFrameCounter = 0
        self.m_terminate_producer = None
        self.m_terminate_counter = None
        self.start_time = time.time()

        self.m_mtx_FrameBuffer = threading.Lock()
        self.m_thr_counter = threading.Thread()
        self.m_camera = cv2.VideoCapture(0)
        if (self.m_camera.isOpened() == False):
            print("Can't find a camera\n")
            exit(1)

    def thread_producer(self):
        while self.m_camera.isOpened():
            ret, frame = self.m_camera.read()
            with self.m_mtx_FrameBuffer:
                if (len(self.m_vFrameBuffer) == self.buf_len):
                    print("Frame drop\n")
                else:
                    self.m_vFrameBuffer.append(frame)
            self.m_inFrameCounter += 1;
            time.sleep(0.005)
            if (self.m_terminate_producer):
                break
                
    def thread_counter(self):
        while self.m_camera.isOpened():
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if (elapsed_time >= 1):
                self.start_time = end_time
                print("FPS: in: ", self.m_inFrameCounter, " | out: ", self.m_outFrameCounter)
                self.m_inFrameCounter = 0
                self.m_outFrameCounter = 0
            time.sleep(1)
            if (self.m_terminate_counter):
                break
                       
    def start(self):
        self.m_terminate_producer = False
        self.m_thr_producer = threading.Thread(target=self.thread_producer, args=())
        self.m_thr_producer.start()
        
        self.tickFrequency = cv2.getTickFrequency()
        self.m_terminate_counter = False
        self.m_thr_counter = threading.Thread(target=self.thread_counter, args=())
        self.m_thr_counter.start()
        
    def getFrame(self):
        with self.m_mtx_FrameBuffer:
            if len(self.m_vFrameBuffer) != 0:
                self.res = self.m_vFrameBuffer.pop()
        self.m_outFrameCounter += 1
        return self.res

    def stop(self):
        self.m_terminate_producer = True
        self.m_thr_producer.join()
        
        self.m_terminate_counter = True
        self.m_thr_counter.join()
        self.m_camera.release()