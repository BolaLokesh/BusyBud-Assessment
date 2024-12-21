def SearchingChallenge(strArr):
    # Convert input list of strings into a 2D grid of integers
    grid = [list(map(int, row)) for row in strArr]
    rows, cols = len(grid), len(grid[0])
    
    # Initialize a visited grid to keep track of explored cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        # If out of bounds or the cell is blocked (1) or already visited, return
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 1 or visited[r][c]:
            return
        # Mark the current cell as visited
        visited[r][c] = True
        # Explore all four directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    hole_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                hole_count += 1
                dfs(r, c)  # Start DFS to mark the whole connected hole

    return hole_count

# Example usage with input parsing
input_data = ["101", "010", "101"]  # Example input grid
print(SearchingChallenge(input_data))  # Expected output: 1
