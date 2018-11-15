
import pymysql
from bottle import *

@get('/')
def index():
    return template('index')

@route('/donyskra',method='POST')
def nyskra():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vef3_verk7")
    cur = conn.cursor()
    cur.execute("select count(*) from 0901013310_vef3_verk7.users where user = %s",(u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("insert into 0901013310_vef3_verk7.users values(%s,%s,%s)",(u,p,n))

        conn.commit()
        cur.close()
        conn.close()
        return u, "hefur verið skráður <br><a href='/'>heim</a>"
    else:
        return u, "er frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"
    

@route('/doinnskra',method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    
    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,passwd="mypassword",db="0901013310_vef3_verk7")
    cur = conn.cursor()

    cur.execute("select count(*) from 0901013310_vef3_verk7.users where user=%s and pass =%s",(u,p))
    result = cur.fetchone()
    if result[0] == 1:
        cur.close()
        conn.close()
        return template('leyni.tpl',u=u)
    else:
        return template('ekkileyni.tpl')

@route('/members')
def member():
    conn = pymysql.connect(host="tsuts.tskoli.is",user="0901013310",port=3306,password="mypassword",db="0901013310_vef3_verk7")
    c = conn.cursor()
    c.execute('select nafn from 0901013310_vef3_verk7.users')
    result = c.fetchall()
    c.close()
    output = template('members',rows = result)
    return output

try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(host="localhost", port=7000, debug=True)
    #run(debug=True)
