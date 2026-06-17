/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    void invert_helper(TreeNode* curr){
        if (curr == nullptr){
            return;
        }
        TreeNode* temp = curr->left;
        curr->left = curr->right;
        curr->right = temp;

        invert_helper(curr->left);
        invert_helper(curr->right);
    }
    TreeNode* invertTree(TreeNode* root) {
        invert_helper(root);
        return root;
    }
};
