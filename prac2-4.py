try:
    import os


    def BFS_Dir(path, dirCallback=None, fileCallback=None):
        queue = []
        ret = []
        queue.append(path);
        while len(queue) > 0:
            tmp = queue.pop(0)
            if (os.path.isdir(tmp)):
                ret.append(tmp)
                for item in os.listdir(tmp):
                    queue.append(os.path.join(tmp, item))
                if dirCallback:
                    dirCallback(tmp)
            elif (os.path.isfile(tmp)):
                ret.append(tmp)
                if fileCallback:
                    fileCallback(tmp)
        return ret


    def printDir(path):
        print("dir: " + path)


    def printFile(path):
        print("file: " + path)


    BFS_Dir(r'C:', printDir, printFile)
except:
    pass