/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    
    // inf=1/0
    
    
    
    var helper = function(minv,root,maxv){
        
        if(root===null){
            return true;
        }

        if(root.val>minv && root.val<maxv){
            return (helper(minv,root.left,root.val) && helper(root.val,root.right,maxv));
        }
        else{
            return false;
        }
    };
    
    
    return helper(Number.MIN_SAFE_INTEGER,root,Number.MAX_SAFE_INTEGER);
};
