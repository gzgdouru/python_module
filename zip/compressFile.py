import os
import zipfile

def zip_file(dirName, zipFileName):
    fileList = []
    if os.path.isfile(dirName):
        fileList.append(dirName)
    else:
        for root, dirs, files in os.walk(dirName):
           [fileList.append(os.path.join(root, name)) for name in files]
    zf = zipfile.ZipFile(zipFileName, "w", zipfile.zlib.DEFLATED)
    for tar in fileList:
        zf.write(tar)
    zf.close()

def unzip_file(zipFileName, unzipDir):
    if not os.path.exists(unzipDir): os.mkdir(unzipDir)
    zf = zipfile.ZipFile(zipFileName)
    for name in zf.namelist():
        if name.endswith("/"):
            os.mkdir(os.path.join(unzipDir, name))
        else:
            ext_fileName = os.path.join(unzipDir, name)
            ext_dir = os.path.dirname(ext_fileName)
            if not os.path.exists(ext_dir): os.makedirs(ext_dir)
            outFile = open(ext_fileName, "wb")
            outFile.write(zf.read(name))
            outFile.close()

def addFileToZip(zipFileName, fileName):
    zf = zipfile.ZipFile(zipFileName, "a", zipfile.zlib.DEFLATED)
    zf.write(fileName)
    zf.close()

def getFileFromZip(zipFileName, unzipDir, fileName):
    if not os.path.exists(unzipDir): os.makedirs(unzipDir)
    zf = zipfile.ZipFile(zipFileName, "r")
    name = os.path.basename(fileName)
    fileObj = open(os.path.join(unzipDir, name), "wb")
    fileObj.write(zf.read(fileName))
    fileObj.close()

def addDirToZip(zipFileName, dirName):
    zf = zipfile.ZipFile(zipFileName, "a", zipfile.zlib.DEFLATED)
    for root, dirs, files in  os.walk(dirName):
        for fileName in files:
            zf.write(os.path.join(root, fileName))
    zf.close()

def getDirFromZip(zipFileName, dirName, unzipDir):
    if not os.path.exists(unzipDir): os.makedirs(unzipDir)
    zf = zipfile.ZipFile(zipFileName, "r")
    for fileName in zf.namelist():
        dirPath = os.path.dirname(fileName)
        dirPath = os.path.normpath(dirPath)
        dirName = os.path.normpath(dirName)
        if dirPath[:len(dirName)] == dirName:
            name = os.path.join(unzipDir, fileName)
            dirPath = os.path.dirname(name)
            if not os.path.exists(dirPath): os.makedirs(dirPath)
            fileObj = open(fileName, "wb")
            fileObj.write(zf.read(fileName))
            fileObj.close()
    zf.close()

if __name__ == "__main__":
    # dirName = r"F:\python"
    # zipFileName = "test.zip"
    # zip_file(dirName, zipFileName)

    # zipFileName = "test.zip"
    # unzipDir = r"F:\python\module\zip\unzip"
    # unzip_file(zipFileName, unzipDir)

    # addFileToZip("test.zip", "compressFile.py")

    # getFileFromZip("test.zip", "F:/", "compressFile.py")

    #addDirToZip("test.zip", r"F:\c11")

    getDirFromZip("test.zip", "c11\c2011\lambda\Debug", "./")

