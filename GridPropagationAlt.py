def main():
    # Question: Given multiple servers arranged in a rows-by-columns grid
    #   Each server can be in one of two states: updated or out-of-date (1 or 0 respectively)
    #   Every day, each updated server can push its software upate to an adjacent server (up, down, left or right)
    #   Goal: find the minimum number of days for all servers on the grid to be up-to-date.

    # Test Case:
    rows = 5
    columns = 4
    
    grid = [
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
    
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

    # create another 2d-array to keep track if a server is visited or not
    visited = [[0 for j in range(columns)] for i in range(rows)]

    # create an int to keep track of the number of days it takes to propagate the update to all servers
    days = 0

    # create a bool to keep track of if a server was updated this iteration
    # due to how the problem is structured, an update must occur every iteration,
    # if not, then the entire grid must be already updated.
    serverWasUpdated = True

    while serverWasUpdated == True:
        serverWasUpdated, grid, visited = doDailyServerUpdates(rows, columns, grid, visited)
        days += 1

        # TODO: remove below
        # print("Day {0} Grid: ".format(days))
        # printGrid(grid)

    # minus 1 because the last iteration did not have any updates
    return days - 1

def doDailyServerUpdates(rows, columns, grid, visited):
    
    # create a bool to keep track of if a server was updated this iteration
    serverWasUpdated = False

    # create a list to keep track of which servers were updated this iteration
    # [(row, column)]
    indices = []

    for i in range(rows):
        for j in range(columns):
            if visited[i][j] == 0 and grid[i][j] == 1:
                indices.extend(tryServerUpdatePropagation(i, j, rows, columns, grid))
                visited[i][j] = 1

    if indices:
        serverWasUpdated = True
        for indice in indices:
            grid[indice[0]][indice[1]] = 1

    return serverWasUpdated, grid, visited

def tryServerUpdatePropagation(i, j, rows, cols, grid):
    # create a list to keep track of which servers were updated this propagation
    indices = []

    if (i != 0 and grid[i-1][j] == 0): indices.append((i-1, j))
    if (j != 0 and grid[i][j-1] == 0): indices.append((i, j-1))
    if (i != rows-1 and grid[i+1][j] == 0): indices.append((i+1, j))
    if (j != cols-1 and grid[i][j+1] == 0): indices.append((i, j+1))

    return indices

def printGrid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    main()