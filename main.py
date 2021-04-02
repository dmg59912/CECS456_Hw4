import numpy as np 
import matplotlib.pyplot as plt
import h5py



if __name__ == '__main__':

  
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
      
      
        let = len(data) * len(data[0])


        #make a copy of data into trasfer size (943000,2) so that we dont modify data array 
        transfer_arr = np.zeros((let,2))
        #keep tract of our transfer array index with count2
        count2 = 0
        for i in range(len(data)):
            for j in range(len(data[0])):

                transfer_arr[count2][0] = data[i][j][0]
                transfer_arr[count2][1] = data[i][j][1]
                count2 +=1 
        #find unique values in our data array and transfer array
        vals, idxs = np.unique(data, return_index = True)
        vals2, idxs = np.unique(data, return_index = True)
        
        # print(vals)
        # print(vals2)

        # if np.array_equal(vals,vals2):
        #     print("values 1 is the same as values 2")

        #where we are storing y mins and max values correspoinding to therr X values (X, y_min, y_max)
        min_max = np.zeros((let,3))
        
        print("\n\n\nand then ...")

        #to add all our y values before findind min and max


        # temp = []
        # count = 0
        # for i in range(len(vals)):
        #     temp = []
        #     for j in range(len(transfer_arr)):
        #         if vals[i] == transfer_arr[j][0]:
        #             #print(vals[i], ", x", transfer_arr[j][0], ",y", transfer_arr[j][1])
        #             temp.append(transfer_arr[j][1])

        #     if( len(temp)!= 0):
               
        #         ymin = min(temp)
        #         ymax = max(temp)
        #         #print('min', ymin, 'max', ymax)
        #         min_max[count][0] = vals[i]
        #         min_max [count][1] = ymin
        #         min_max[count][2] = ymax
        #         count += 1


       

        # #removing zeros from the array 
        # min_max = min_max[~np.all(min_max ==0, axis= 1)]
        # print(min_max)


        x,y = transfer_arr[:,0], transfer_arr[:,1]
        r = np.sqrt(x **2, y** 2 )
        phi = np.arctan(y, x)

        print(min_max.shape)
        plt.title("Polar transformation of boundary points")
        plt.axes( projection = 'polar')
        plt.polar(phi,r, 'b.')
        plt.show()
        
        #print(transfer_arr)
       # print(len(transfer_arr))
        #print(vals)
        #print(sum(arr))
        #print(min_max.shape)
        #print(len(vals))
        #print(data)
        