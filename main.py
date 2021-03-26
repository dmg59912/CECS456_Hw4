import numpy as np 
import h5py



if __name__ == '__main__':

    arr = np.random.randn(1000)
  
# creating a file

    with h5py.File('ellipse_data.hdf5','r') as hdf:
        #transform our file data in to a list with given keys  
        ls = list(hdf.keys())
        print('List of datasets in this file: \n', ls)
        #getting our data from the list 
        dataset = hdf.get('data')
        #save data into our array 
        data = np.array(dataset)
        print('Shape of data:\n', data.shape)
      
        count = 0
        for i in range(len(data)):

            for j in range(len(data[0])):
                print(data[i][j][0])
                if( data[i][j][0] == .1):
                #print(data[0][i][0])
                    count += 1
       # print(count)
      
        print(count)
        print(data[0][1])
        