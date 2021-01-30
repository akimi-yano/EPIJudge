from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    arr = path.split("/")
    ans = []
    head = ""

    if path[0] == "/":
        head = "/"
        
    for elem in arr:
        if elem == "..":
            if ans and ans[-1] != "..":
                ans.pop()
            else:
                ans.append(elem)
        elif elem.isalnum():
            ans.append(elem)

    return  head + "/".join(ans) 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
