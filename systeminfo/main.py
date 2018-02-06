'''
Created on 25 Jan 2018

@author: aoifeosullivan
'''
import platform
import shutil

def main():
    print("The platform is", platform.platform())
    total, used, free = shutil.disk_usage(__file__)
    print ("total, used, free: ", total, used, free)	
	return
if __name__ == '__main__':
    main()

