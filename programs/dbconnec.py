import cx_Oracle
print(cx_Oracle)
con=cx_Oracle.connect("system","manager","localhost:1521/orcl")
print(con)
#print("connection established")
#con.close()
#print("connection closed")
