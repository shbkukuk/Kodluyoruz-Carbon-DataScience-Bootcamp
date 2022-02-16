from cProfile import label
from itertools import count
from multiprocessing.sharedctypes import Value
from statistics import mean
from collections import Counter

import string
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
def create_data():
    """
        The function create data random array that given size and number between low_value and high_value .

        Returns:
            data : data save as Pandas.DataFrame 
             
        """
    x1 = np.random.randint(0,200,1000)#random create array that given size and number between low_value and high_value
    x2 = np.random.randint(0,200,1000)#random create array that given size and number between low_value and high_value
    counts = Counter()
    for a,b in zip(x1,x2):
        if a < 20:
            counts["<20"] += 1
        if a >= 20 and a < 40:
            counts["20-40"] += 1
        if a >= 40 and a < 60:
            counts["40-60"] += 1
        if a >= 60 and a < 80:
            counts["60-80"] += 1
        if a >= 80:
            counts[">80"] += 1
    data = pd.DataFrame({'x':list(counts.keys()), 'counter': list(counts.values())})
    return data
def create_array(number_of_data:int, low_value:int, high_value:int):
        """
        The function for creating array between low_value and high_value. And categorize array.

        Args : 
            number_of_data (int) : Number of data
            low_value (int) : Minumum value of data
            max_value (int) : Maxiumum value of data
        Returns :
            array : N-dimensional array
        """

        array = []
        for i in range(number_of_data):
            x1 = np.random.randint(low=low_value, high=high_value) #random create array that given size and number between low_value and high_value
            x2 = np.random.randint(low=low_value, high=high_value) #random create array that given size and number between low_value and high_value
            if x1 < high_value//2 and x2 > high_value//2:
                array.append([x1,x2,1])
            elif x1 < high_value//2 and x2 < high_value//2:
                array.append([x1,x2,0])
            elif x1 > high_value//2 and x2 > high_value//2:
                array.append([x1,x2,0])
            else:
                array.append([x1,x2,1])
        array = np.array(array)
        return array
        
class DataOperations():
    '''
    This is a class for data visualisation on data.
    If data is a numpay array, We convert to dataframe and save.
    If data is a string, We check 'json' or 'csv' and save like dataframe.
    If data is a empty, We create random dataframe and save.
    
    Example:
        DataOperations(data='data\\data.json')

    Args:
        data (None): The arg is used for input data which type data 
    
    Attributes:
        data (None): This is where we store data which is type (array,dataframe,path of data or none )
        
    '''
    def __init__(self, data = None):
        self.data = data
        if data is None:
            self.data = create_data()
        elif isinstance(data,str) :
            
            if data.endswith("json"):
                self.data=pd.read_json(data)
            elif data.endswith("csv"):
                self.data= pd.read_csv(data)
            else:
                print("Datatype is not found.Please check data type")
        elif isinstance(data,pd.core.frame.DataFrame) :
            self.data = data 
        elif isinstance(data,np.ndarray) :
            self.data = pd.DataFrame(data,columns=['x','y','label'])
        else:
            raise ("Check Data that is given")
            
 
        
    def data_info(self):
        """
        The function give information about data.

        Returns:
            Table : Contain values type, values count, standard deviation and mean
             
        """
        print("Data Features")
        print(self.data.describe()[:3])
        print("***************************")
        print("Data Informantion")
        return (self.data.info())
    
    def visualisation_array_bar(self):
        """
        The function plot data that type is None

        Returns:
            Figure : Plotting data using with bar categorized. 
        
        """
        self.data.plot.bar(x='x',y='counter',rot=0)
        return plt.show()

        
    def visualisation_path(self):
        """
        The function plot data that format are 'json' or 'csv'

        Returns:
            Figure 1 :  Draw a categorical scatterplot with non-overlapping points. 
            Figure 2 :  Draw a combination of boxplot and kernel density estimate.
        """
        sns.swarmplot(x="national", 
              y="length",
              data=self.data)
        plt.show()
        sns.violinplot(x="length",
               y="sex",
               data=self.data)
        return plt.show()


    def visualisation_dataframe(self):
        """
        The function plot data that format is dataframe

        Returns:
            Figure 1 :  Draw a categorical scatterplot with non-overlapping points. 
            Figure 2 :  Show the counts of observations in each categorical bin using bars.
        """
        sns.swarmplot(x="species", 
              y="petal_length",
              data=self.data)
        plt.show()
        sns.countplot(x='sepal_length',
                    data=self.data)
        return plt.show()

    def visualisation_array(self):
        sns.scatterplot(x="x", 
                        y="y", 
                        hue="label", 
                        data=self.data)
        return plt.show()
        


if __name__ == '__main__':


    MATRIX_ARRAY = create_array(1000,1,250) #creting 3*3 matrix 
    DATAFRAME = sns.load_dataset('iris') #creating dataframe using seaborn libary 
    
    obj = DataOperations() #object is not given data
    obj1 = DataOperations(data='data\\data.json') #object is given data that type 'json'
    obj2 = DataOperations(data='data\\data.csv')  #object is given data that type 'csv'
    obj3 = DataOperations(data=DATAFRAME) #object is given data that type dataframe
    obj4 = DataOperations(data=MATRIX_ARRAY) #object is given data that type array
 
    #Data type is none visualisation and info
    obj.data_info()
    obj.visualisation_array_bar()

    #Data type is 'json' visualisation and info
    obj1.data_info()
    obj1.visualisation_path()

    #Data type is 'csv' visualisation and info
    obj2.data_info()
    obj2.visualisation_path()

    #Data type is dataframe visualisation and info
    obj3.data_info()
    obj3.visualisation_dataframe()
    
    #Data type is array visualisation and info
    obj4.data_info()
    obj4.visualisation_array()

    
    
    
    

    
    
    
    
