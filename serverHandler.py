'''
Python script for server to make Video SR.
Run shell file in here.
'''

import os

def superResolution(type):
    if (type == 'YUVESRGAN'):
        os.system('sh BasicSR/EXEC_YUVESRGAN.sh')
    else:
        print(f'Undefined model')


def checkServer():

    exist = False # default set as False

    print(f'Check storage server if there are videos to be handled.')
    print(f'Return True when exist, else False')

    '''
    Check server
    ...
    '''

    return exist


if __name__ == '__main__':

    # Check if there are photos/videos
    if (checkServer == True):
        superResolution('YUVESRGAN')
    else:
        # keep waiting
        print(f'There are nothing to be handled')
