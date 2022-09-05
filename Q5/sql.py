import pymysql
pymysql.install_as_MySQLdb()

# MySQL DATABASE CONNECTION
mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='sade_yazılım_task'
)

# TO see DUPLICATE USERS
query_for_dublicates = '''
	SELECT 
		TCKN, AD, COUNT(*) AS CNT
	FROM
		tc_dublicate_found
	GROUP BY TCKN, AD
	HAVING COUNT(*) > 1;
'''

# TO see TCKN and COUNT of users
query_for_same_tc_diff_person = '''
	SELECT 
		TCKN, COUNT(*) AS CNT
	FROM
		tc_dublicate_found
	GROUP BY TCKN
	HAVING COUNT(*) > 1;
'''

# To See TCKN and AD
query_for_same_tc_diff_person_names = '''
	SELECT 
		*
	FROM
		tc_dublicate_found
	WHERE
		TCKN = (SELECT 
				T.TCKN
			FROM
				(SELECT 
					TCKN, COUNT(*) AS CNT
				FROM
					tc_dublicate_found
				GROUP BY TCKN
				HAVING COUNT(*) > 1) AS T)
'''

mycursor = mydb.cursor()

# EXECUTE ONE OF SQL QUEY
mycursor.execute(query_for_same_tc_diff_person_names)

# FETCH THE RESULT OF QUERY 
result = mycursor.fetchall()

print(result)




# print(f"\n\n\\[INFO]---------- ' : {result[0][0]}\n\n")