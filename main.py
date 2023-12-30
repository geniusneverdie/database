import pymysql
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template, request, redirect, url_for
import os

# 连接数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='4239692', db='work1', charset='utf8')
# 创建游标对象
cursor = connection.cursor()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/team_league_player_view/<string:teamname>', methods=['GET','POST'])
def sel(teamname):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM team_league_player_view WHERE teamname=%s", (teamname,))
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM team WHERE teamname=%s", (teamname,))
        team = cursor.fetchone()
    return render_template('sel.html', data=data,team=team)

@app.route('/coach', methods=['GET'])
def coach():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coach")
        coachs = cursor.fetchall()
    return render_template('coach.html', coachs=coachs)
@app.route('/coach/add', methods=['GET', 'POST'])
def add_coach():
    if request.method == 'POST':
        coachnumber = request.form.get('coachnumber')
        coachname = request.form.get('coachname')
        position = request.form.get('position')
        age = request.form.get('age')
        teamname = request.form.get('teamname')
        with connection.cursor() as cursor:
            sql = "INSERT INTO coach (coachnumber,coachname,position,age,teamname) VALUES (%s,'%s','%s','%s','%s')" %(coachnumber,coachname,position,age,teamname)

            print(sql)

            cursor.execute(sql)
            connection.commit()
        return redirect(url_for('coach'))
    else:
        return render_template('add_coach.html')


@app.route('/coach/edit/<int:coachnumber>', methods=['GET', 'POST'])
def edit_coach(coachnumber):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coach WHERE coachnumber=%s", (coachnumber,))
        coach = cursor.fetchone()
    if request.method == 'POST':
        x=coachnumber
        coachnumber = request.form('coachnumber')
        coachname = request.form('coachname')
        position = request.form('position')
        age = request.form('age')
        teamname = request.form('teamname')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE coach SET coachnumber=%s, coachname=%s, position=%s, age=%s, teamname=%s WHERE coachnumber=%s",
                           (coachnumber,coachname,position,age,teamname,x))
            connection.commit()
        return redirect(url_for('coach'))

    return render_template('edit_coach.html', coach=coach)

@app.route('/coach/delete/<int:coachnumber>')
def delete_coach(coachnumber):
    try:
        with connection.cursor() as cursor:
            cursor.execute("START TRANSACTION")
            cursor.execute("DELETE FROM coach WHERE coachnumber = %s", (coachnumber,))
            cursor.execute("COMMIT")
    except Exception as e:
        connection.rollback()
    return redirect(url_for('coach'))


@app.route('/fans', methods=['GET'])
def fans():

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fans")
        fanss = cursor.fetchall()
    return render_template('fans.html', fanss=fanss)
@app.route('/fans/add', methods=['GET', 'POST'])
def add_fans():
    if request.method == 'POST':
        id = request.form.get('id')
        age = request.form.get('age')
        fgender = request.form.get('fgender')
        work = request.form.get('work')
        teamname = request.form.get('teamname')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO fans (id, age,fgender,work,teamname) VALUES (%s, %s,%s,%s,%s)",
                           (id,age,fgender,work,teamname))
            connection.commit()
        return redirect(url_for('fans'))
    else:
        return render_template('add_fans.html')

@app.route('/fans/edit/<int:id>', methods=['GET', 'POST'])
def edit_fans(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fans WHERE id=%s", (id,))
        fans = cursor.fetchone()

    if request.method == 'POST':
        id = request.form.get('id')
        age = request.form.get('age')
        fgender = request.form.get('fgender')
        work = request.form.get('work')
        teamname = request.form.get('teamname')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE fans  WHERE id=%s",
                           (age,fgender,work,teamname, id))
            connection.commit()
        return redirect(url_for('fans'))

    return render_template('edit_fans.html', fans=fans)
@app.route('/fans/delete/<int:id>')
def delete_fans(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fans WHERE id=%s", (id,))
        connection.commit()
    return redirect(url_for('fans'))

# 商品列表
@app.route('/player', methods=['GET'])
def player():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM player")
        players = cursor.fetchall()
    return render_template('player.html', players=players)

@app.route('/player/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        playername=request.form.get('playername')
        playnumber = request.form.get('playnumber')
        status = request.form.get('status')
        age = request.form.get('age')
        usedfoot = request.form.get('usedfoot')
        height = request.form.get('height')
        weight = request.form.get('weight')
        teamname = request.form.get('teamname')
        goals = request.form.get('goals')
        assists = request.form.get('assists')
        appearances = request.form.get('appearances')
        startings = request.form.get('startings')
        nogoaltimes = request.form.get('nogoaltimes')
        averagecomments = request.form.get('averagecomments')
        playposition = request.form.get('playposition')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO player (playername,playnumber,status,age,usedfoot,height,weight,teamname,goals,"
                           "assists,appearances,startings,nogoaltimes,averagecomments,playposition)"
                           " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (playername,playnumber,status,age,usedfoot,height,weight,teamname,goals,assists,
                            appearances,startings,nogoaltimes,averagecomments,playposition))
            connection.commit()
        return redirect(url_for('player'))
    else:
        return render_template('add_player.html')

@app.route('/player/edit/<string:playername>', methods=['GET', 'POST'])
def edit_player(playername):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM player WHERE playername=%s", (playername,))
        player = cursor.fetchone()
    if request.method == 'POST':
        x=playername
        playername = request.form.get('playername')
        playnumber = request.form.get('playnumber')
        status = request.form.get('status')
        age = request.form.get('age')
        usedfoot = request.form.get('usedfoot')
        height = request.form.get('height')
        weight = request.form.get('weight')
        teamname = request.form.get('teamname')
        goals = request.form.get('goals')
        assists = request.form.get('assists')
        appearances = request.form.get('appearances')
        startings = request.form.get('startings')
        nogoaltimes = request.form.get('nogoaltimes')
        averagecomments = request.form.get('averagecomments')
        playposition = request.form.get('playposition')

        with connection.cursor() as cursor:
            cursor.execute("UPDATE player SET playername=%s, playnumber=%s, status=%s, age=%s, usedfoot=%s, "
                           "height=%s, weight=%s, teamname=%s, goals=%s, assists=%s, appearances=%s, startings=%s, nogoaltimes=%s, "
                           "averagecomments=%s,teamname=%s, WHERE playername=%s",
                           (playername,playnumber,status,age,usedfoot,height,weight,teamname,goals,assists,
                            appearances,startings,nogoaltimes,averagecomments,playposition,x))
            connection.commit()
        return redirect(url_for('player'))

    return render_template('edit_player.html', player=player)

@app.route('/player/delete/<string:playername>')
def delete_player(playername):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM player WHERE playername=%s", (playername,))
    return redirect(url_for('player'))

# team
@app.route('/team', methods=['GET'])
def team():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `team`")
        teams = cursor.fetchall()
    return render_template('team.html', teams=teams)

@app.route('/team/add', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        teamname = request.form.get('teamname')
        scores = request.form.get('scores')
        fame = request.form.get('fame')
        homecount = request.form.get('homecount')
        profit = request.form.get('profit')
        ranking = request.form.get('ranking')
        leaguename = request.form.get('leaguename')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO `team` (teamname, scores,fame,homecount,profit,ranking,leaguename) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                           (teamname, scores,fame,homecount,profit,ranking,leaguename))
            connection.commit()
        return redirect(url_for('team'))
    else:
        return render_template('add_team.html')

@app.route('/team/edit/<string:teamname>', methods=['GET', 'POST'])
def edit_team(teamname):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `team` WHERE teamname=%s", teamname)
        team = cursor.fetchone()
    if request.method == 'POST':
        x=teamname
        teamname = request.form.get('teamname')
        scores = request.form.get('scores')
        fame = request.form.get('fame')
        homecount = request.form.get('homecount')
        profit = request.form.get('profit')
        ranking = request.form.get('ranking')
        leaguename = request.form.get('leaguename')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE `team` SET teamname=%s,scores=%s, fame=%s, homecount=%s, profit=%s, ranking=%s,"
                           "leaguename=%s WHERE teamname=%s", (teamname, scores,fame,homecount,profit,ranking,leaguename,x))
            connection.commit()
        return redirect(url_for('team'))

    return render_template('edit_team.html', team=team)

@app.route('/team/delete/<string:teamname>')
def delete_team(teamname):

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `team` WHERE teamname=%s", teamname)
        cursor.execute("DELETE FROM `coach` WHERE teamname=%s", teamname)
        cursor.execute("DELETE FROM `player` WHERE teamname=%s", teamname)
        cursor.execute("DELETE FROM `fans` WHERE teamname=%s", teamname)
        connection.commit()
    return redirect(url_for('team'))

# game
@app.route('/game', methods=['GET'])
def game():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM game")
        games = cursor.fetchall()
    return render_template('game.html', games=games)

@app.route('/game/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        gamenumber=request.form.get('gamenumber')
        time = request.form.get('time')
        location = request.form.get('location')
        gamescore = request.form.get('gamescore')
        leaguename = request.form.get('leaguename')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO game (gamenumber,time,location,gamescore,leaguename) VALUES (%s,%s,%s,%s,%s)",
                           (gamenumber,time,location,gamescore,leaguename))
            #cursor.callproc("AddToCart", (cart_id, user_id,product_id, quantity))
            connection.commit()
        return redirect(url_for('gamenumber'))
    else:
        return render_template('add_game.html')

@app.route('/game/edit/<int:gamenumber>', methods=['GET', 'POST'])
def edit_game(gamenumber):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM game WHERE gamenumber=%s", gamenumber)
        game = cursor.fetchone()
    if request.method == 'POST':
        x=gamenumber
        #p=cart[2]
        gamenumber = request.form.get('gamenumber')
        time = request.form.get('time')
        location = request.form.get('location')
        gamescore = request.form.get('gamescore')
        leaguename = request.form.get('leaguename')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE `game` SET gamenumber=%s,time=%s, location=%s, gamescore=%s, leaguename=%s WHERE teamname=%s",
                           (gamenumber,time,location,gamescore,leaguename, x))
            connection.commit()
        return redirect(url_for('game'))
    return render_template('edit_game.html', game=game)

@app.route('/game/delete/<int:gamenumber>', methods=['POST'])
def delete_game(gamenumber):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM game WHERE gamenumber=%s", gamenumber)
        connection.commit()
    return redirect(url_for('game'))

# 支付列表
@app.route('/league', methods=['GET'])
def league():

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM league")
        leagues = cursor.fetchall()
    return render_template('league.html', leagues=leagues)

@app.route('/league/add', methods=['GET', 'POST'])
def add_league():
    if request.method == 'POST':
        leaguename = request.form.get('leaguename')
        level= request.form.get('level')
        nation = request.form.get('nation')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO league (leaguename,level,nation) VALUES (%s,%s,%s)", (leaguename,level,nation))
            connection.commit()
        return redirect(url_for('league'))
    else:
        return render_template('add_league.html')

@app.route('/league/edit/<string:leaguename>', methods=['GET', 'POST'])
def edit_league(leaguename):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM league WHERE leaguename=%s", leaguename)
        league = cursor.fetchone()
    if request.method == 'POST':
        x=payment_id
        leaguename = request.form.get('leaguename')
        level = request.form.get('level')
        nation = request.form.get('nation')

        with connection.cursor() as cursor:
            cursor.execute("UPDATE payment SET leaguename=%s ,level=%s ,nation=%s  WHERE leaguename=%s", (leaguename,level,nation,x))
            connection.commit()
        return redirect(url_for('league'))
    return render_template('edit_league.html', league=league)

@app.route('/league/delete/&lt;string:leaguename&gt;', methods=['POST'])
def delete_league(leaguename):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM league WHERE leaguename=%s", leaguename)
        cursor.execute("DELETE FROM game WHERE leaguename=%s", leaguename)
        cursor.execute("DELETE FROM team WHERE leaguename=%s", leaguename)
        connection.commit()
    return redirect(url_for('league'))


if __name__ == '__main__':
    app.run(debug=True)


# 关闭游标和数据库连接
cursor.close()
connection.close()
