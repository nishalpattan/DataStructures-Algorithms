class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for value in row] for row in grid]
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, visited, i,j)
                    num_of_islands += 1
        return num_of_islands
    def dfs(self, grid, visited, i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(grid, visited, i-1,j)
        self.dfs(grid, visited, i+1,j)
        self.dfs(grid, visited, i,j-1)
        self.dfs(grid, visited, i,j+1)
                    
        
        # Brute Froce Iterative
#         def get_next_nodes(i,j,grid,visited_nodes):
#             next_nodes = list()
#             if i > 0 and not visited_nodes[i-1][j]:
#                 next_nodes.append((i-1,j))
#             if i < len(grid) - 1 and not visited_nodes[i+1][j]:
#                 next_nodes.append((i+1,j))
#             if j > 0 and not visited_nodes[i][j-1]:
#                 next_nodes.append((i,j-1))
#             if j < len(grid[0]) - 1 and not visited_nodes[i][j+1]:
#                 next_nodes.append((i,j+1))
#             return next_nodes
#         def traverse_nodes(i,j,grid,visited_nodes,num_of_islands):
#             curr_size = 0
#             nodes_to_explore = [(i,j)]
#             while len(nodes_to_explore) > 0:
#                 i,j = nodes_to_explore.pop()
#                 if visited_nodes[i][j]:
#                     continue
#                 visited_nodes[i][j] = True
#                 if grid[i][j] == '0':
#                     continue
#                 curr_size += 1
#                 next_nodes_to_visit = get_next_nodes(i,j,grid,visited_nodes)
#                 for next_node in next_nodes_to_visit:
#                     nodes_to_explore.append(next_node)
#             if curr_size > 0:
#                 num_of_islands.append(curr_size)
                
#         visited_nodes = [[ False for value in row] for row in grid]
#         num_of_islands = []
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if visited_nodes[i][j]:
#                     continue
#                 traverse_nodes(i,j,grid,visited_nodes,num_of_islands)
#         return len(num_of_islands)
    
    
    
        
