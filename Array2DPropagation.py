import copy

def main():
    # Question: Given multiple servers arranged in a rows-by-columns grid
    #   Each server can be in one of two states: updated or out-of-date (1 or 0 respectively)
    #   Every day, each updated server can push its software upate to an adjacent server (up, down, left or right)
    #   Goal: find the minimum number of days for all servers on the grid to be up-to-date.

    # Test Case:
    rows = 5
    columns = 4
    
    grid = [
        [1, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 1]]
    
    # My logic: instead of looking for an already updated server and letting it push its updates to its adjacent neightbours
    #   find out-of-date servers and have them look actively look for software updates.

    print("Day 0 Grid: ")
    printGrid(grid)
    print("Minimum Number of Days: {0}".format(minimumDays(rows, columns, grid)))

def minimumDays(rows, columns, grid):
    # rows -> int; number of rows
    # columns -> int; number of columns
    # grid -> [[]] of int; a 2d array representing the status of each server
    #   0 -> software out of date
    #   1 -> software updated
    
    # create an int to keep track of the number of days it took
    days = 0
    # create a bool to keep track of if a server was updated or not
    serverUpdate = True
    
    while serverUpdate == True:
        serverUpdate, grid = doDailySoftwareUpdate(rows, columns, grid)
        days += 1

        # TODO: remove below
        # print("Day {0} Grid: ".format(days))
        # printGrid(grid)
        
    # minus 1 b/c no updates happened for the last day
    return days - 1
    
def doDailySoftwareUpdate(rows, columns, grid):
    serverUpdate = False
    
    # create a list of tuples (row, column) for keeping track of which servers were updated
    indices = []
    
    # for each grid item, if software not updated, try to update self
    for i in range(rows):
        for j in range(columns):
            if (grid[i][j] == 0):
                update = tryUpdateSelf(i, j, rows, columns, grid)
                if update != None:
                    indices.append(update)

    # populate newly updated servers to grid
    if len(indices) > 0:
        serverUpdate = True
    
        for indice in indices:
            grid[indice[0]][indice[1]] = 1
    
    return serverUpdate, grid


def tryUpdateSelf(i, j, rows, columns, grid):
    
    # peek up, down, left, right to see if any adjacent servers are up-to-date
    # if so, then self, at position (i, j), is updatable
    if ((i != 0 and grid[i-1][j] == 1) or (i != rows-1 and grid[i+1][j] == 1) or 
    (j != 0 and grid[i][j-1] == 1) or (j != columns-1 and grid[i][j+1] == 1)):
        return (i, j)
    else:
        return None

def printGrid(grid):
    for row in grid:
        print(row)


if __name__ == "__main__":
    main()