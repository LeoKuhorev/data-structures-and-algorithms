def valid_binary_tree(root) -> bool:
    is_valid = True
    
    def traverse(node) -> int:
        if not node:
            return 0
        
        L = traverse(node.left)
        R = traverse(node.right)
        
        nonlocal is_valid
        if abs(L - R) > 1:
            is_valid = False
        
        return 1 + max(L, R)
    
    traverse(root)
    
    return is_valid
    