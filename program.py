__author__ = 'useruser'
import copy
import time
from random import randint
class Soduku(object):
    def __init__(self, problem):
        self.problem = problem

    def resolve(self):
        solutionStack = [self.problem]
        tmp = self.get_solution_array(self.problem)
        solutionArrayStack = [tmp]
        time_t = 0
        # problem = [[0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0]]
        prev_x = -1
        prev_y = -1
        while 1:
            # time_t += 1
            # fetch the last solution in solution stack
            next_item_cord = {}
            solutionArray = []
            # print 'still ',len(solutionStack),'in stack'
            solutionNow = copy.deepcopy(solutionStack[len(solutionStack) - 1])
            solutionArray = solutionArrayStack[len(solutionArrayStack) - 1]

            flag = self.check_if_need_to_back(solutionNow, solutionArray)
            if flag is True:
                # print 'pop!'
                solutionArrayStack.pop()
                solutionStack.pop()
            else:
                time_t += 1
                # next_item_cord = self.get_first_possible_item(solutionArray,solutionNow=solutionNow)
                next_item_cord = self.get_first_possible_item(solutionArray,solutionNow=solutionNow)
                if next_item_cord == False:
                    break
                # print 'next_item_cord:',next_item_cord
                prev_x = next_item_cord['x']
                prev_y = next_item_cord['y']
                next_item_array = solutionArray[prev_x][prev_y]
                next_item = next_item_array[len(next_item_array)-1]
                # randint(0,len(next_item_array)-1)
                solutionNow[prev_x][prev_y] = next_item

                # solutionArray_tmp = get_solution_array(solutionNow)
                solutionArray_tmp = copy.deepcopy(solutionArray)
                solutionArray_tmp = self.get_resolution_array_new(solutionArray_tmp, prev_x, prev_y,
                                                             next_item)
                if next_item in solutionArray[prev_x][prev_y]:
                    solutionArray[prev_x][prev_y].remove(
                        next_item)
                # print 'next point is ',prev_x,',',prev_y
                solutionStack.append(solutionNow)
                solutionArrayStack.append(solutionArray_tmp)
                # print solutionArrayStack
                # print solutionStack

        for i in range(0, 9, 1):
            print solutionStack[len(solutionStack) - 1][i]
        print 'total forward:',time_t


    def check_if_need_to_back(self,solutionNow, solutionArray):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if len(solutionArray[i][j]) == 0 and solutionNow[i][j] == 0:
                    return True
        return False


    def get_resolution_array_new(self,solutionArray, x, y, value):
        for tmp_j in range(0, 9, 1):
            if value in solutionArray[x][tmp_j]:
                solutionArray[x][tmp_j].remove(value)
        for tmp_i in range(0, 9, 1):
            if value in solutionArray[tmp_i][y]:
                solutionArray[tmp_i][y].remove(value)
        for tmp_i in range(x / 3 * 3, x / 3 * 3 + 3):
            for tmp_j in range(y / 3 * 3, y / 3 * 3 + 3):
                if value in solutionArray[tmp_i][tmp_j]:
                    solutionArray[tmp_i][tmp_j].remove(value)
        return solutionArray


    def get_solution_array(self,problem):
        tmp = []
        for i in range(0, 9, 1):
            tmp_line_array = []
            for j in range(0, 9, 1):
                # print '['+bytes(i)+','+bytes(j)+']: '+ bytes(problem[i][j])
                if problem[i][j] == 0:
                    # no value, get possible value array
                    tmp_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                    # remove the existed value in line
                    for tmp_j in range(0, 9, 1):
                        if problem[i][tmp_j] != 0:
                            if problem[i][tmp_j] in tmp_value:
                                tmp_value.remove(problem[i][tmp_j])

                    # remove the existed value in column
                    for tmp_i in range(0, 9, 1):
                        if problem[tmp_i][j] != 0:
                            if problem[tmp_i][j] in tmp_value:
                                tmp_value.remove(problem[tmp_i][j])

                    # remove the existed value in the rectangle
                    for x in range(i / 3 * 3, i / 3 * 3 + 3):
                        for y in range(j / 3 * 3, j / 3 * 3 + 3):
                            if problem[x][y] != 0:
                                if problem[x][y] in tmp_value:
                                    tmp_value.remove(problem[x][y])

                    tmp_line_array.append(tmp_value)
                else:
                    tmp_line_array.append([])
            tmp.append(tmp_line_array)
            # print tmp_line_array
        # print tmp
        return tmp

    # get first item to be the point of tree
    def get_first_possible_item(self, solution_array, solutionNow = None):
        is_finished = True
        shortest_item_length = 9
        shortest_item_x = 0
        shortest_item_y = 0
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                tmp_length = len(solution_array[i][j])
                if tmp_length != 0:
                    is_finished = False
                    if solutionNow[i][j] != 0:
                        tmp_length += 1
                    if tmp_length < shortest_item_length:
                        shortest_item_length = tmp_length
                        shortest_item_x = i
                        shortest_item_y = j

        # print 'shortest item is:',shortest_item_length,shortest_item_x,shortest_item_y
        if is_finished:
            return False
        else:
            return {'x': shortest_item_x, 'y': shortest_item_y}

    def get_next_possible_item(self, solution_array, prev_x, prev_y, solutionNow = None):
        if prev_x == -1 and prev_y == -1:
            return self.get_first_possible_item(solution_array, solutionNow)
        else:
            is_finished = True
            shortest_item_length = 9
            shortest_item_x = 0
            shortest_item_y = 0
            for tmp_i in range(0, 9, 1):
                tmp_length = len(solution_array[tmp_i][prev_y])
                if tmp_length != 0:
                    is_finished = False
                    if solutionNow[tmp_i][prev_y] != 0:
                        tmp_length += 1
                    if tmp_length < shortest_item_length:
                        shortest_item_length = tmp_length
                        shortest_item_x = tmp_i
                        shortest_item_y = prev_y
                        if tmp_length == 1:
                                return {'x': shortest_item_x, 'y': shortest_item_y}

            for tmp_j in range(0, 9, 1):
                tmp_length = len(solution_array[prev_x][tmp_j])
                if tmp_length != 0:
                    is_finished = False
                    if solutionNow[prev_x][tmp_j] != 0:
                        tmp_length += 1
                    if tmp_length < shortest_item_length:
                        shortest_item_length = tmp_length
                        shortest_item_x = prev_x
                        shortest_item_y = tmp_j
                        if tmp_length == 1:
                                return {'x': shortest_item_x, 'y': shortest_item_y}

            for x in range(prev_x / 3 * 3, prev_x / 3 * 3 + 3):
                for y in range(prev_y / 3 * 3, prev_y / 3 * 3 + 3):
                    tmp_length = len(solution_array[x][y])
                    if tmp_length != 0:
                        is_finished = False
                        if solutionNow[x][y] != 0:
                            tmp_length += 1
                        if tmp_length < shortest_item_length:
                            shortest_item_length = tmp_length
                            shortest_item_x = x
                            shortest_item_y = y
                            if tmp_length == 1:
                                return {'x': shortest_item_x, 'y': shortest_item_y}
            # print 'shortest item is:',shortest_item_length,shortest_item_x,shortest_item_y
            if is_finished:
                return self.get_first_possible_item(solution_array,solutionNow)
            else:
                return {'x': shortest_item_x, 'y': shortest_item_y}
# p = '55502abb2861c75cab261ac3'
# p = ObjectId(p)
# print type(p)
# p = bytes(p)
# print type(p)
# ank = int(119999999999999)
# print ank

problem = \
    [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]

f = Soduku(problem)
startTime=time.time()
f.resolve()
endTime=time.time()
print "Finished! Time consuming: " + "%.4f" % (endTime-startTime) + " Seconds"
