import cx_Oracle
con=cx_Oracle.connect("system","manager","localhost:1521/xe")
cur=con.cursor()
cur.execute("desc customers")
#for rec in cur:
print(rec)
cur.close()
con.close()
