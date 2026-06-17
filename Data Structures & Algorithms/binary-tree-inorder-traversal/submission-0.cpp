class Solution {
public:
    vector<int> results;

    void inorder(TreeNode* root) {
        if (root == nullptr) return;
        inorder(root->left);
        results.push_back(root->val);
        inorder(root->right);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return results;
    }
};