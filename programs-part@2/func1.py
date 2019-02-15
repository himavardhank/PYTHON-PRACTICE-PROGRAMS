import cx_Oracle
con=cx_Oracle.connect("system","manager","localhost:1521/xe")
cur=con.cursor()
res=cur.callfunc('f1',cx_Oracle.NUMBER,(20,))
print(res)
cur.close()
con.close()
