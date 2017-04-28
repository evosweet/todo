import cherrypy
import sqlite3
import json
import os
conn = sqlite3.connect('todo.db', check_same_thread=False)





class toDO(object):
    
    def index(self):
        return open("index.html")
    index.exposed = True

    def all(self):
        all_todo = []
        cursor = conn.execute('select * from todo_table')
        for x in cursor:
            all_todo.append({'id':x[0],'name':x[1],'status':x[2]})
        return json.dumps(all_todo) 
    all.exposed = True

    def addNew(self,item_name):
        conn.execute("INSERT INTO todo_table VALUES (NULL,?,?)",(item_name ,0));
        conn.commit()
    addNew.exposed = True

    def delTask(self,task_id):
        print task_id
        conn.execute("delete from todo_table where id = ?",(task_id,))
        conn.commit()
    delTask.exposed = True


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))

    conf = {'/css':{'tools.staticdir.on': True,'tools.staticdir.dir': os.path.join(current_dir, 'css')},
    '/script':{'tools.staticdir.on': True,'tools.staticdir.dir': os.path.join(current_dir, 'script')}}
    cherrypy.quickstart(toDO(), '/', conf)