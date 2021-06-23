#!/usr/bin/env python3
import cgi
import pickle

form = cgi.FieldStorage()
ip_min = form.getfirst("ip_min")
ip_avg = form.getfirst("ip_avg")
rp_min = form.getfirst("rp_min")
rp_avg = form.getfirst("rp_avg")
sex = form.getfirst("sex")
age = form.getfirst("age")
smoking = form.getfirst("smoking")

filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

x = [[ip_min, ip_avg, rp_min, rp_avg, sex, age, smoking]]
y = model.predict(x)

file = open('journal.txt', 'a')
result_diag = ip_min+','+ip_avg+','+rp_min+','+rp_avg+','+sex+','+age+','+smoking+','+y[0]+'\n'
file.write(result_diag)
file.close


print("Content-type: text/html\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Модель</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
        outline: none;
        font-family: Arial;
    }
    ul {
        list-style: none; /*убираем маркеры списка*/
        margin: 0; /*убираем верхнее и нижнее поле, равное 1em*/
        padding-left: 0; /*убираем левый отступ, равный 40px*/
    }
    a { text-decoration: none; }
    .menu {
        list-style: none;
        text-align: center;
        text-transform: uppercase;
        font-weight: bold;
    }
    .menu li {
        display: inline-block;
        color: #FFF;
        width: 200px;
        border-right: 2px solid #FFF;
        text-align: center;
        margin-left: -5px;
    }
    .menu li:last-child{border: none;}
    .menu li a {
        color: #FFF;
        display:block;
    }
    .menu li a:hover{
        background: #FFF;
        color: #000;
    }
    table{
        margin: auto;
        text-align: center;
        border-collapse: collapse;
    }
    td,th{
        border: 2px solid #BC3333;
        padding: 7px;
    }
   </style>
</head>
<body>
            <div style="width: 100%; height: 40px; background: #A34A4A; line-height: 40px;">
                <ul class="menu">
                  <li><a href="../index.html">Главная</a></li>
                  <li><a href="../diagnosis.html">Диагностика</a></li>
                  <li><a href="../journal.html">Журнал</a></li>
                </ul>
            </div>
            <div style='width: 100%; height: 100px; text-align: center; font-size: 25px; line-height: 100px;'>
                Диагностика респираторных инфекций
            </div>
            <div style="text-align: center; margin-top: 50px;">
                <table>""")
print("<tr style='background: #F7C7C7;'><td width='100'>IP (min)</td>")
print("<td width='100'>IP (avg)</td>")
print("<td width='100'>RP (min)</td>")
print("<td width='100'>RP (avg)</td>")
print("<td width='100'>Пол</td>")
print("<td width='70'>Возраст</td>")
print("<td width='150'>Курение</td></tr>")
print("<tr><td>{}</td>".format(ip_min))
print("<td>{}</td>".format(ip_avg))
print("<td>{}</td>".format(rp_min))
print("<td>{}</td>".format(rp_avg))
if sex == 0:
    print("<td>Женский</td>")
else:
    print("<td>Мужской</td>")
print("<td>{}</td>".format(age))
if smoking == 1:
    print("<td>Некурящий</td>")
else:
    if smoking == 2:
        print("<td>Экс-курильщик</td>")
    else:
        print("<td>Активный курильщик</td>")
print("""</tr>
                </table>""")
print("<p style='margin-top: 50px; font-size: 16px;'>Данный пациент относится к группе <b>{}</b>.</p>".format(y[0]))
print("""
    </body>
    </html>""")
