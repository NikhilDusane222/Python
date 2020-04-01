import time

time_start_input=input("Press enter key to start the time!!")
start=time.time()

time_start_output=input("Press enter key to end the time!!")
end=time.time()

#calculate total time
total_time=end-start
#convert total time into seconds
inSec=total_time%60
print(f"Total time is: ",inSec , "sec")