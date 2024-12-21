def ArrayChallenge(strArr):
    from collections import defaultdict  # Import defaultdict to simplify dictionary operations

    # Parse the input to get child-parent relationships
    edges = []  # Initialize a list to store the edges (child-parent pairs)
    for pair in strArr:  # Loop through each pair in the input
        pair = pair.strip("()")  # Strip parentheses around each pair
        child, parent = map(int, pair.split(","))  # Split the string by ',' and convert to integers
        edges.append((child, parent))  # Append the tuple (child, parent) to the edges list
    
    # Initialize a dictionary to map each parent to their children
    parent_to_children = defaultdict(list)  # Using defaultdict for automatic list creation
    all_nodes = set()  # A set to store all nodes (both children and parents)
    child_nodes = set()  # A set to store only child nodes

    # Build the parent-child relationship
    for child, parent in edges:  # Loop through each edge (child, parent) in the list
        parent_to_children[parent].append(child)  # Add the child to the parent's list in the dictionary
        all_nodes.update([child, parent])  # Add both the child and parent to the set of all nodes
        child_nodes.add(child)  # Add the child to the set of child nodes

        # Ensure no parent has more than two children
        if len(parent_to_children[parent]) > 2:  # If a parent has more than two children
            return "false"  # Return false because the tree structure is invalid (binary tree rule)

    # Identify the root node
    # Root is the node that doesn't appear as a child (not in child_nodes)
    root_candidates = all_nodes - child_nodes  # Find all nodes that are not in child_nodes
    if len(root_candidates) != 1:  # If there isn't exactly one root node, it's invalid
        return "false"
    root = root_candidates.pop()  # Pop the root node from the set (since we are guaranteed only one)

    # Perform a DFS to ensure there are no cycles and all nodes are reachable
    visited = set()  # A set to keep track of visited nodes to detect cycles

    # DFS function to visit nodes recursively
    def dfs(node):
        if node in visited:  # If the node has already been visited, it means there's a cycle
            return False
        visited.add(node)  # Mark the current node as visited
        for child in parent_to_children[node]:  # For each child of the current node
            if not dfs(child):  # Recursively visit each child
                return False  # If any child causes a cycle or invalidity, return false
        return True  # Return true if no cycles are found in the subtree

    # Start DFS from the root node
    if not dfs(root):  # If DFS returns False, there's a cycle or other issue
        return "false"
    
    # Ensure all nodes are reachable from the root node
    if len(visited) != len(all_nodes):  # If not all nodes were visited, the tree is disconnected
        return "false"

    # If all checks passed, return "true" indicating the structure is a valid tree
    return "true"

# Example usage
print(ArrayChallenge(input().split(", ")))  # Read input, split by ", ", and pass to ArrayChallenge
