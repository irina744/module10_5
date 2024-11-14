import multiprocessing
from datetime import datetime


def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start_time = datetime.now()
    #for name in files:
     #read_info(name)
    #end_time = datetime.now()
    #print(end_time - start_time)

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end_time = datetime.now()
    print(end_time - start_time)
