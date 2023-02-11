import os
import csv
import MySQLdb
import time
import collections
import re
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


def get_type(s):
	# try integer type
	try:
		v = int(s)
	except ValueError:
		pass
	else:
		if abs(v) > 2147483647:
			return 'bigint'
		else:
			return 'int'
	# try float type
	try:
		float(s)
	except ValueError:
		pass
	else:
		return 'double'
	
	# check for timestamp
	dt_formats = (
		('%Y-%m-%d %H:%M:%S', 'datetime'),
		('%Y-%m-%d %H:%M:%S.%f', 'datetime'),
		('%Y-%m-%d', 'date'),
		('%H:%M:%S', 'time'),
	)
	for dt_format, dt_type in dt_formats:
		try:
			time.strptime(s, dt_format)
		except ValueError:
			pass
		else:
			return dt_type
	
	# text type
	if len(s) > 255:
		return 'text'
	else:
		return 'varchar(255)'

def most_common(l, default='varchar(255)'):
	if l:
		for dt_type in ('text', 'bigint'):
			if dt_type in l:
				return dt_type
		return max(l, key=l.count)
	return default

def get_col_types(input_file, max_rows=1000):
	csv_types = collections.defaultdict(list)
	reader = csv.reader(open(input_file))
    # test first 1000 rows for csv data
	for row_i, row in enumerate(reader):
		if row_i == 0:
			header = row
		else:
			for col_i, s in enumerate(row):
				data_type = get_type(s)
				csv_types[header[col_i]].append(data_type)
				
		if row_i == max_rows:
			break

    # take the most common data type for each row
	return [most_common(csv_types[col]) for col in header]

def upload_csv_db(file_dir):
	mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")
	mydb.set_character_set('utf8')
	cursor = mydb.cursor()

	table_name = os.path.basename(file_dir)
	csv_data = csv.reader(open(file_dir, 'r'))
	csv_header = next(csv_data, None)
	num_columns = len(csv_header)
	col_types = get_col_types(file_dir)

	table_name2 = table_name.split('.')
	table = table_name2[0]
	#print (table)
	#print (csv_header)
	table_columns = '('
	for i, col_type in zip(csv_header, col_types):
		i = re.sub(r"[^a-zA-Z0-9]+", ' ', i)
		i = i.replace(" ", "_")
		table_columns += '%s %s, ' % (i, col_type)
	table_columns = table_columns[:-2]
	table_columns += ');'
	#print (table_columns)
	cursor.execute('DROP TABLE IF EXISTS ' + table + ';')
	cursor.execute('CREATE TABLE ' + table + ' ' +  table_columns)

	if num_columns > 0:
		placeholders = (num_columns-1) * "%s, " + "%s"
		query = ("INSERT INTO %s" % table) + (" VALUES (%s)" % placeholders)
    
		for row in csv_data:
			if len(row) == num_columns:
				print (row)
				cursor.execute(query, row)

	#close the connection to the database.
	mydb.commit()
	cursor.close()
	print ("Done")

@app.route("/")
@app.route("/main")
def index():
	return render_template("main.html")


@app.route("/show", methods=["POST", "GET"])
def show():
	if request.method == 'GET':
		mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")
		mydb.set_character_set('utf8')
		cursor = mydb.cursor()
		cursor.execute("SELECT table_name FROM information_schema.tables where table_schema='CSV';")
		res = cursor.fetchall()
		return render_template("show.html", result1=res, content_type='application/json')
	elif request.method == 'POST':
		option = request.form.get("option")
		mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")
		mydb.set_character_set('utf8')
		cursor = mydb.cursor()
		cursor.execute("SELECT table_name FROM information_schema.tables where table_schema='CSV';")
		res = cursor.fetchall()
		cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='CSV' AND `TABLE_NAME`='"+option+"';")
		res2 = cursor.fetchall()
		select_cols = ""
		for i in res2:
			select_cols += i[0]
			select_cols += ", "
		select_cols = select_cols[:-2]
		cursor.execute("SELECT " + select_cols + " FROM " + option + " LIMIT 50;")
		res3 = cursor.fetchall()
		cols_list = [tup[0] for tup in res2]
		cols_list_len = len(res2)
		#for i in range(len(res3)):
		#	for j in range(len(res3[i])):
		#		print (res3[i][j],i,j)
		#print (len(res3))
		print (option)
		return render_template("show.html", result1=res, len_list=cols_list_len, opt=option, len1=len(res3), len2=len(res3[0]), result2=cols_list, result3=res3 , content_type='application/json')


@app.route("/fuzzyfunction", methods=["POST", "GET"])
def fuzzyfunction():
	if request.method == 'GET':
		option = request.form.get("option")
		mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")
		mydb.set_character_set('utf8')
		cursor = mydb.cursor()
		cursor.execute("SELECT table_name FROM information_schema.tables where table_schema='CSV';")
		res = cursor.fetchall()
		return render_template("fuzzyfunction.html", result1=res, opt=option)
	if request.method == 'POST':
		option = request.form.get("option")
		mydb = MySQLdb.connect(host="localhost", port=3306, user='root',passwd='',db='CSV',unix_socket="/opt/lampp/var/mysql/mysql.sock")
		mydb.set_character_set('utf8')
		cursor = mydb.cursor()
		cursor.execute("SELECT table_name FROM information_schema.tables where table_schema='CSV';")
		res = cursor.fetchall()
		return render_template("fuzzyfunction.html", result1=res, opt=option)

@app.route("/upload")
@app.route("/upload", methods=["POST", "GET"])
def upload():
	if request.method == 'GET':
		return render_template("upload.html")

	if request.method == 'POST':
		if not os.path.isdir('./upload'):
			os.mkdir('./upload')
		print(request.files.getlist("file"))
		for upload in request.files.getlist("file"):
			print(upload)
			print("{} is the file name".format(upload.filename))
			filename = upload.filename
			# This is to verify files are supported
			ext = os.path.splitext(filename)[1]
			if (ext == ".csv"):
				print("File supported moving on...")
			else:
				return render_template("main.html")
			destination = "/".join(['./upload', filename])
			print("Accept incoming file:", filename)
			print("Save it to:", destination)
			if (upload.save(destination)==None):
				upload_csv_db(destination)
		
		return render_template("main.html")


if __name__ == "__main__":
	app.run(port=4555, debug=True)
