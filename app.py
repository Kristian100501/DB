from flask import Flask
from flaskext.mysql import MySQL
app = Flask("GTS Backend")
mysql = MySQL()
app.config['MYSQL_USER'] = 'test'
app.config[' MYSQL_ROOT_PASSWORD'] = 'pass'
app.config[' MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE'] = 'projectdata'
mysql.init_app(app)
try:
    conn = mysql.connect()
    cursor = conn.cursor()
    print("connected")
except:
    print("I am unable to connect to the database")


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/t_Name')
def t_namen():
    cursor.execute("SELECT id,Vorname,Nachanme from Kunde")
    data = cursor.fetchall()
    return render_template('t_Namen.html', data=data)

@app.route('/t_Adressen')
def t_adressen():
    cursor.execute("SELECT Strasse,Hausnummer,PLZ,Ort from Kunde")
    data = cursor.fetchall()
    return render_template('t_Adressen.html', data=data)

@app.route('/kundenbelange')
def t_belange():
    cursor.execute("SELECT Datum,Vorname,Nachanme,Bemerkung,Prio FROM Kunden_belange KB left outer join prioritaet P on KB.prioritaet=P.id left outer join Kunde K on K.Id=KB.kd_id order by datum desc")
    data = cursor.fetchall()
    return render_template('kundenbelange.html', data=data)

if __name__ == '__main__':
    app.run()
