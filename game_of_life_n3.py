# modification of script at https://www.tutorialspoint.com/conway-s-game-of-life-using-python

import numpy as np
import matplotlib.pyplot as plt

class GameLifeCalc_n1(object):          # object to calculate the cells that will grow, live or die and then sum total

   def __init__(self, MainArray):          # inherits main_array
        self.main_array = MainArray.main_array

   def apply_count_algorithm_and_filter(self):

        main_array = self.main_array

        # calculate weight of each grid location

        main_n1 = self.main_array
        n1 = (main_n1[0:-2,0:-2] + main_n1[0:-2,1:-1] + main_n1[0:-2,2:] +     # algorithm to weight each grid value
                  main_n1[1:-1,0:-2] + main_n1[1:-1,2:] + main_n1[2:,0:-2] +
                  main_n1[2:,1:-1] + main_n1[2:,2:])


        # filter by weights and position where main_array == 0 or 1

        birth = (n1 == 3) & (main_array[1:-1, 1:-1] == 0)  # where n1 = 3 and main_array[1:-1,1:-1] is equal to 0
        survive = ((n1 == 2) | (n1 == 3)) & (main_array[1:-1, 1:-1] == 1)  # where n1 = 2 or 3 and  main_array[1:-1,1:-1] is equal to 1

        main_array[...] = 0                 # set all of main_array to 0

        main_array[1:-1, 1:-1][birth | survive] = 1        # set where birth or survive occurred to 1

        count_Birth = np.sum(birth)                  # sum each births and survival.
        self.count_Birth = count_Birth
        count_Survive = np.sum(survive)
        self.count_Survive = count_Survive

        return main_array

class MainArray(object):
    def __init__(self, size, seed = 'Random'):
        if seed == 'Random':
            self.main_array = np.random.randint(2, size = size)       # instantiate, create main_array with random integers
        self.calculator = GameLifeCalc_n1(self)                          # extend object with GameLifeCalc_n1
        self.iteration = 0                          # iteration count

    def visualise_array(self):
        i_count = self.iteration
        im = None
        plt.title("Conway's Game of Life")
        while True:        # run until
            if i_count == 0:
                plt.ion()
                im = plt.imshow(self.main_array, vmin=0, vmax=2, cmap=plt.cm.gray)     # first plot
            else:
                im.set_data(self.main_array)  # update data plotted following each game of life calculation
            i_count += 1
            self.calculator.apply_count_algorithm_and_filter()                     # run the function that calculates and counts the grids that survive or are born
            print('Life Cycle: {} Birth: {} Survive: {}'.format(i_count, self.calculator.count_Birth, self.calculator.count_Survive))
            plt.pause(0.01)
            yield self

def main():

   aHeight = 256
   aWidth = 256
   main_array_n1 = MainArray((aHeight,aWidth))   # instantiate main_array_n1
   for _ in main_array_n1.visualise_array():     # run
      pass

if __name__ == '__main__':
   main()