import numpy
import scipy.special

class neuralNetwork:

    # инициализировать нейронную суть
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # задать количество узлов во входном, скрытом и выходном слое
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # матрицы весовых коэффициентов связей wih и who
        # весовые коэффициенты связей связей между узлом i и узлом j
        # следующего слое обозначены как w_i_j
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))   
        # коффициерт обучения     
        self.onodes = learningrate
        # функция активации
        self.activation_function = lambda x: scipy.special.expit(x)
        pass
        # тренировка сети
    def train(self, inputs_list, targets_list):
        # приоброзование значение в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T;
        targets = numpy.array(targets_list, ndmin=2).T;

        # рассчитать исходящие данные скрытого слоя
        hidden_inputs = numpy.dot(self.wih, input);
        # рассчитать входные данные скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs);

        # рассчитать входные данные выходного слоя
        final_inputs = numpy.dot(self.wih, hidden_outputs);
        # рассчитать исходящие данные выходного слоя
        final_outputs = self.activation_function(final_inputs);
        pass

    # опрос нейроной сети
    def query(self, input_list):
        # преабразовать список входных значений
        # в двухмерный массив
        inputs = numpy.array(input_list, ndmin=2).T
        
        # рассчитать входные данные скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        print(hidden_inputs);
        # рассчитать исходящие данные скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)

        # рассчитать входные данные выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # рассчитать исходящие данные выходного слоя
        final_outputs = self.activation_function(final_inputs)
        return final_outputs