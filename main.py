from flask import Flask, render_template, request, redirect, url_for
import pymysql

# connect database
conn = pymysql.Connect(
    host='localhost',
    user='root',
    passwd='13938241242',
    db='covid-19',
    port=3306,
    charset='utf8',
)

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

# get input
@app.route('/search', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        #result = request.form
        country = request.values.get("Country")
        date = request.values.get("Date")
        data = request.values.getlist("data type")

        # fixed option
        if country == '' and data != []:
            return render_template('search.html', result = [['Must select country']])

        cursor = conn.cursor()

        have_date = False

        # def SELECT
        sql_select = 'SELECT '
        if country:
            sql_select += country
        else:
            sql_select = sql_select + '*'

        # def WHERE date
        sql_where_date = 'WHERE date='
        if date:
            sql_where_date += '\'' + date + '\''
        else:
            sql_where_date = ''

        sql = []

        # set all sql code
        if data:
            for d in data:
                if d == 'Confirm':
                    sql.append(sql_select + ' FROM world_confirm_date ' + sql_where_date + ';')
                elif d == 'Vaccinated':
                    sql.append(sql_select + ' FROM world_vaccinated_date ' + sql_where_date + ';')
                else:
                    sql.append(sql_select + ' FROM world_death_date ' + sql_where_date + ';')
        else:
            data = ['Confirm', 'Vaccinated', 'Death']
            sql.append(sql_select + ' FROM world_confirm_date ' + sql_where_date + ';')
            sql.append(sql_select + ' FROM world_vaccinated_date ' + sql_where_date + ';')
            sql.append(sql_select + ' FROM world_death_date ' + sql_where_date + ';')

        #print(sql)

        # get data from database, save in sqlResult
        sqlResult = []
        for s in sql:
            cursor.execute(s)
            sqlResult.append(cursor.fetchall())

        cursor.close()
        #print(sqlResult[0][0])

        # get all date, save in dateResult
        time_sql = 'SELECT Date FROM world_confirm_date;'
        cursor = conn.cursor()
        cursor.execute(time_sql)
        dateResult = cursor.fetchall()
        cursor.close()


        # change data format
        newResult = []
        if have_date:
            for i in range(len(sqlResult)):
                cur = []
                if sqlResult[i] == ():
                    cur.append(data[i] + ': ' + date + ': No data')
                else:
                    for j in range(len(sqlResult[0])):
                        #print(sqlResult[i][j][0])
                        #print(data[i] + ': ' + date + ': ' + str(sqlResult[i][j][0]))
                        cur.append(data[i] + ': ' + date + ': ' + str(sqlResult[i][j][0]))
                newResult.append(cur)
        else:
            for i in range(len(sqlResult)):
                cur = []
                for j in range(len(sqlResult[0])):
                    #print(f"date : {dateResult[j][0]} ")
                    cur.append(data[i] + ': ' + str(dateResult[j][0]) + ': ' + str(sqlResult[i][j][0]))
                    #print(f"cur : {cur}")
                newResult.append(cur)

        return render_template('search.html', result = newResult)

# set gender search
@app.route('/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        
        country = request.values.get("Country")
        gender = request.values.get("Gender")
        data_type = request.values.get("Data")

        # define SELECT
        sql_select = ''

        if gender == 'male':
            if data_type == 'Confirm':
                sql_select = 'Select confirm_male, date FROM world_date_gender '
            if data_type == 'Death':
                sql_select = 'Select death_male, date FROM world_date_gender '
        else:
            if data_type == 'Confirm':
                sql_select = 'Select confirm_female, date FROM world_date_gender '
            if data_type == 'Death':
                sql_select = 'Select death_femal, date FROM world_date_gender '

        # def WHERE
        sql_where = 'WHERE country=' + '\'' + country  + '\'' + ';'

        cursor = conn.cursor()

        cursor.execute(sql_select + sql_where)
        sqlResult = cursor.fetchall()

        cursor.close()

        newResult = []

        for d in sqlResult:
            newResult.append(str(d[1]) + ':' +str(d[0]))
        
        #print(newResult)

        return render_template('gender.html', result = newResult)

@app.route('/sql_search', methods=['GET', 'POST'])
def sqlSearch():
    if request.method == 'POST':

        sql_code = request.values.get('SQL')

        cursor = conn.cursor()

        try:
            cursor.execute(sql_code)
            cursor.close()
            sqlResult = cursor.fetchall()

            cursor.close()
            return render_template('gender.html', result = sqlResult)
        except Exception as e:
            return render_template('gender.html', result = ["Change a SQL code"])


# set canned search
@app.route('/all', methods=['GET', 'POST'])
def all():
    if request.method == 'POST':

        cannedId = request.values.get("canned querry")
        cursor = conn.cursor()


        value = "country_confirm_data"
        if cannedId == 'world_data':
            sql = 'SELECT * FROM world_data;'
        elif cannedId == 'country_vaccine':
            sql = 'SELECT * FROM world_vaccine'
        # else:
        #     sql = 'SELECT * FROM country_confirm_data'

        cursor.execute(sql)
        sqlResult = cursor.fetchall()

        cursor.close()
        return render_template('all.html', result = sqlResult)

if __name__ == '__main__':
    app.run(debug=True)