# %%
class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result_col = {}
        res_dict = {}

        if root == None:
            return []
        queue=[(root, 0)]
        while (queue!=[]):
            queue2 = []
            for item in queue:
                node = item[0]
                col = item[1]

                res_dict[col] = res_dict.get(col, []) + [node.val]

                if node.left != None:
                    queue2.append((item[0].left, col-1))
                if node.right != None:
                    queue2.append((item[0].right, col+1))
            queue = queue2

        # sort the keys array and index the dict with that array
        return [res_dict[x] for x in sorted(res_dict.keys())]



    def verticalOrder_1(self, root: Optional[TreeNode]) -> List[List[int]]:

        def traverse(root):
            if root == None:
                return {}
            results_dict = {}
            queue = [(root, 0)]
            while(queue != []):
                new_queue = []
                for qp in queue:
                    current, current_depth = qp
                    if current_depth not in results_dict:
                        results_dict[current_depth] = [current.val]
                    else:
                        results_dict[current_depth].append(current.val)
                    if current.left != None:
                        new_queue.append((current.left, current_depth-1))
                    if current.right != None:
                        new_queue.append((current.right, current_depth+1))
                queue = new_queue

            return results_dict

        results_dict = traverse(root)
        if results_dict=={}:
            return []
        min_value = min(results_dict.keys())
        max_value = max(results_dict.keys())
        results_arr = []
        for r in range(min_value, max_value+1):
            results_arr.append(results_dict[r])
        return results_arr
