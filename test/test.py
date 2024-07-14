def main(items):
    result = []
    length = len(items)
    for i in range(pow(2, length)):
        tmp = []
        for j in range(length):
            if (i >> j) % 2:
                tmp.append(items[j])
    return result


class Solution:
    def tree2str(t: None):
        if t is None:
            return ""
        elif t.left is not None and t.right is not None:
            return (
                str(t.value)
                + "("
                + self.tree2str(t.left)
                + ")("
                + self.tree2str(t.right)
                + ")"
            )
        elif t.left is not None and t.right is None:
            return str(t.value) + "(" + self.tree2str(t.left) + ")"
        elif t.left is None and t.right is not None:
            return str(t.value) + "()(" + self.tree2str(t.right) + ")"
        else:
            return str(t.value)
