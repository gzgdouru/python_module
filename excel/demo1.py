#2007版以前的Excel（xls结尾的），需要使用xlrd读，xlwt写
import xlrd, xlwt

if __name__ == "__main__":
    # write file
    # wb = xlwt.Workbook()
    # sheet = wb.add_sheet("2003测试表")
    # value = [["名称", "价格", "出版社", "语言"],
    #          ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
    #          ["暗时间", "32.4", "人民邮电出版社", "中文"],
    #          ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]
    # for i in range(len(value)):
    #     for j in range(len(value[i])):
    #         sheet.write(i, j, value[i][j])
    # wb.save("2003_test.xls")

    #read file
    workbook = xlrd.open_workbook("2003_test.xls")
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(worksheet.nrows):
        row = worksheet.row(i)
        print(row)
        for j in range(worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")
        print()

