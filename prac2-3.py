try:
   import os
   file = open ("result.txt",'w')
   def DFS_Dir(path, dirCallback = None, fileCallback = None):
       stack = []
       ret = []
       stack.append(path);
       while len(stack) > 0:
           tmp = stack.pop(len(stack) - 1)
           if(os.path.isdir(tmp)):
               ret.append(tmp)
               for item in os.listdir(tmp):
                   stack.append(os.path.join(tmp, item))
               if dirCallback:
                   dirCallback(tmp)
           elif(os.path.isfile(tmp)):
               ret.append(tmp)
               if fileCallback:
                   fileCallback(tmp)
       return ret

   def printDir(path):
       print ("dir: " + path)
       file.write("dir:  " + path +"\n")

   def printFile(path):
       print ("file: " + path)
       file.write("file:  " + path +"\n")

#b = BFS_Dir(r'C:\tmp', printDir, printFile)
   d = DFS_Dir(r'C:', printDir, printFile)
except:
    pass