#coding:utf-8
import pymysql

config = {
    "host" : "192.168.232.130",
    "port" : 3306,
    "user" : "ouru",
    "passwd" : "123456",
    "db" : "mysql",
    "charset" : "utf8",
    "cursorclass" : pymysql.cursors.DictCursor
}

connection = pymysql.connect(**config)
connection.autocommit(1)
cursor = connection.cursor()

try:
    # 创建数据库
    DB_NAME = "test"
    #cursor.execute("create database  if not exists %s" % DB_NAME)
    connection.select_db(DB_NAME)

    #创建表
    TABLE_NAME = 'user'
    sql = '''
    create table %s(
    id int primary key,
    name varchar(30))
    ''' % TABLE_NAME
    #cursor.execute(sql)

    # 插入单条数据
    sql = 'INSERT INTO user(id, name) values(%d, "%s")' % (1, "jack")
    #cursor.execute(sql)

    # 不建议直接拼接sql，占位符方面可能会出问题，execute提供了直接传值
    value = [2, "John"]
    #cursor.execute('INSERT INTO user values(%s,%s)',value)

    # 批量插入数据
    values = []
    for i in range(3, 20):
        values.append((i, "kk" + str(i)))
    #cursor.executemany('INSERT INTO user values(%s,%s)', values)

    # 查询数据条目
    count = cursor.execute('select * from %s' % TABLE_NAME)
    print 'total records : %d' % count
    print 'total records: ', cursor.rowcount

    # 获取表名信息
    desc = cursor.description
    print "%s %3s" % (desc[0][0], desc[1][0])

    # 查询一条记录
    print 'fetch one record:'
    result = cursor.fetchone()
    print result

    # 查询多条记录
    print 'fetch five record:'
    result = cursor.fetchmany(5)
    print [r for r in result]

    # 查询所有记录
    # 重置游标位置，偏移量:大于0向后移动;小于0向前移动，mode默认是relative
    # relative:表示从当前所在的行开始移动; absolute:表示从第一行开始移动
    cursor.scroll(0, mode="absolute")
    results = cursor.fetchall()
    print [r for r in results]

    cursor.scroll(-2)
    results = cursor.fetchall()
    print [r for r in results]

    # 更新记录
    cursor.execute('update %s set name = "%s" where id = %s' % (TABLE_NAME, "wancaiji", 1))

    #删除记录
    cursor.execute('delete from %s where id = %s' % (TABLE_NAME, 2))

    #如果没有设置自动提交,这里需要手动调用commit
    #connection.commit()
except:
    import traceback
    traceback.print_exc()
    # 发生错误时,如果没设置自动提交则回滚
    connection.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    connection.close()


