from flask import Flask, render_template, request
import MySQLdb as mdb

app = Flask(__name__)
    
@app.route('/youtube')
def metrics():
    
    con = mdb.connect(host = 'localhost', 
                  user = 'root',
                  database = 'Youtube_Trending',
                  passwd = 'enter_password', 
                  charset='utf8', use_unicode=True);
    
    cur = con.cursor(mdb.cursors.DictCursor)
    query = ''' SELECT video_id, 
                publish_date, 
                title, 
                category, 
                channel_id, 
                channel_title 
                FROM Descriptions'''
    cur.execute(query)
    descriptions = cur.fetchall()
    cur.close()
    con.close()

    return render_template('descriptions.html', descriptions = descriptions)

@app.route('/metrics')    
def descriptions():
    
    video_id = request.args.get('video_id')
    
    con = mdb.connect(host = 'localhost', 
                  user = 'root',
                  database = 'Youtube_Trending',
                  passwd = 'dwdstudent2015', 
                  charset='utf8', use_unicode=True);
    
    cur = con.cursor(mdb.cursors.DictCursor)
    query = ''' SELECT video_id, 
                last_reported_date, 
                views, 
                likes_count, 
                dislikes_count, 
                comments_count 
                FROM Metrics
                WHERE video_id = %s ORDER BY last_reported_date DESC'''
    cur.execute(query, (video_id,) )
    metrics = cur.fetchall()
    cur.close()
    con.close()

    return render_template('metrics.html', video_id = video_id, metrics=metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    
   