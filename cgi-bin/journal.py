import pandas as pd

print("Content-type: text/html\n\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Журнал</title>
    <link href="../main.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="div-menu">
        <ul class="menu">
          <li class="../current"><a href="index.html">Главная</a></li>
          <li><a href="../diagnosis.html">Диагностика</a></li>
          <li><a href="cgi-bin/journal.py">Журнал</a></li>
        </ul>
    </div>
    <div>
        <div class="div-title">
            Список пациентов
        </div>
        <table class="journal-table">
            <tr style="background: #F7C7C7;">
                <td width="50">№</td>
                <td width="100">IP (min)</td>
                <td width="100">IP (avg)</td>
                <td width="100">RP (min)</td>
                <td width="100">RP (avg)</td>
                <td width="100">Пол</td>
                <td width="70">Возраст</td>
                <td width="150">Курение</td>
                <td width="150">Диагноз</td>
            </tr></table>""")
df = pd.read_csv('../journal.txt', sep=",", header=None)
n = 1
for i in range(len(df)):
    print(df[0][i], df[1][i], df[2][i], df[3][i], df[4][i], df[5][i], df[6][i], df[7][i])
    print("<tr>")
    print("<td>{}</td>".format(n))
    print("<td>{}</td>".format(df[0][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td>{}</td>".format(df[1][i]))
    print("<td style='background: #BC3333; color: #FFF;'>{}</td>".format(df[1][i]))
    print("</tr>")
    n = n+1
print("""
        <p style="margin-left: 50px; margin-top: 30px;">
            <b>* COPD</b> - амбулаторные и госпитализированные пациенты с хроническим заболеванием легких без острой респираторной инфекции.<br>
            <b>* Asthma</b> - амбулаторные и госпитализированные пациенты с астмой без острых респираторныех инфекций.<br>
            <b>* Infected</b> - пациенты с респираторными инфекциями, но без хронических заболеваний легких и астмы.<br>
            <b>* HC</b> - Здоровые пациенты.
        </p>
    </div>
</body>
</html>""")

