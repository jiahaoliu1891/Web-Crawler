"""
Dump data from csv into database
"""
import pymysql
import traceback

def csv2db(csvFile):
    # open database
    db = pymysql.connect("localhost","root","200125","TESTDB" )
    cursor = db.cursor()
    with open(csvFile, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            city, date, temper, weather, windSpeed = line.strip('\n').split(',')
            sql = "INSERT INTO weather(city, date, temper, weather, windSpeed) VALUES "
            sql = sql + "(\"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(city, date, temper, weather, windSpeed)
            print(sql)
            try:
                # 执行SQL语句
                cursor.execute(sql)
                db.commit()
            except:
                traceback.print_exc()
                db.rollback()
                

if __name__ == "__main__":
    csv2db("data/weather.csv")



