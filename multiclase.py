import pandas as pd
import numpy as np
import tkinter.filedialog



class Multiclass:
    
    def __init__(self, learnRate=0.1, epochs=1000):
        self.learnRate=learnRate
        self.epochs=epochs

    def loadFile(self):
        root=tkinter.Tk()
        root.withdraw()
        filePath=tkinter.filedialog.askopenfilename()
        df=pd.read_csv(filePath)
        self.training(df)
        
    """
    Los pesos se calculan segun el numero de capas, en este caso 
    w1 se calcula con hiddenLayer e inputLayer debido a las operaciones de la 
    red neuronal.
    
    Los pesos w1 conectan la capa de entrada con la capa oculta, entonces para conectar
    las capas la matriz de pesos w1 debe tener la forma (hiddenLayer, InputLayer)
    """
    def initializeWeights(self, inputLayer, hiddenLayer, outputLayer):
        w1=np.random.randn(hiddenLayer, inputLayer.shape[1])*0.01
        #Es comun incializar el sesgo en 0, pero puedo dar valores random
        b1=np.zeros((hiddenLayer, 1))
        w2=np.random.randn(outputLayer, hiddenLayer)*0.01
        b2=np.zeros((outputLayer, 1))
        weights={"w1":w1, "b1":b1, "w2":w2,"b2":b2}
        
    def training(self, df):
        numericDf=df.select_dtypes(include=['float64','int64'])
        print(numericDf)        
        
        
#Ejecucion
neuralNetwork=Multiclass(learnRate=0.1, epochs=1000)
neuralNetwork.loadFile()