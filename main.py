import numpy as np 
import matplotlib.pyplot as plt
import math
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
    

        index_to_plot = [0,100,200,300,400,500,600,700,800,900]
        

        print("\n\n\nand then ...")


        
        for k in range(len(index_to_plot)):

            #find unique values in our data array according to our index
            index_t = index_to_plot[k]
            print("printing index ",index_t)
            vals3 = np.unique(data[index_t, :, :1])

            #creating a temp array to store our y values from the unique x's on the given index
            temp = []

            #where we are storing y mins and max values correspoinding to therr X values (X, y_min, y_max)
            min_max = np.zeros((len(vals3),3))
            count = 0
            for i in range(len(vals3)):
                temp = []
                for j in range(len(data[k])):
                    if vals3[i] == data[k][j][0]:
                        temp.append(data[k][j][1])
                if( len(temp)!= 0):
                    ymin = min(temp)
                    ymax = max(temp)
                    min_max[count][0] = vals3[i]
                    min_max[count][1]= ymin
                    min_max[count][2] = ymax
                    count += 1
        
        
            #removing zeros from the array 
          
            #fill our x and y values so that we can calculate r for x ymin and x ymax
            fill = len(min_max) * 2 
            x = [0] * fill
            y = [0] * fill
          
          
            count3 = 0
            for i in range(len(min_max)):
                for j in range(2):
                    x[count3] =  min_max[i][0]
                    y[count3] = min_max[i][j + 1]
                    # sum_sq = x[count3] **2 + y[count3] ** 2
                    # r[count3] = np.sqrt(sum_sq)
                    count3 += 1


    

            #convert to array instead of list
            x_p = np.array(x)
            y_p = np.array(y)
        
            #finding all the Rs 
            r = np.sqrt(x_p **2 + y_p ** 2)
            #finding thats 
            thetas = np.arctan2(y_p, x_p) 

            #plotting the graphs 
            plt.scatter(thetas,r)
            plt.title("Plot for index " + str(index_to_plot[k]), va = 'bottom')
            plt.show()
            plt.savefig("pic " + str(k), format ='eps', dpi=1000)
            plt.close()
        