from datetime import date, datetime, timedelta

import psycopg2
import psycopg2.extras


class postLoad:
    def __init__(self, delta=0):
        self.delta = delta

    delta = 0
    dblist = {}
    conn = psycopg2.connect(
        dbname="strength", user="postgres", password="postgres", host="localhost"
    )
    data = datetime.now() + timedelta(days=delta)
    selsqlall = "SELECT public.tasks.title , id_task, created_at, plan_date, is_done FROM public.queue_tasks join public.tasks on (public.queue_tasks.id_task = public.tasks.id) where plan_date ='{}';".format(
        data.strftime("%Y-%m-%d")
    )
    selsql = "SELECT public.tasks.title , id_task, plan_date, is_done FROM public.queue_tasks join public.tasks on (public.queue_tasks.id_task = public.tasks.id) where plan_date ='{}';".format(
        data.strftime("%Y-%m-%d")
    )

    seltaskssql = "SELECT * FROM tasks order by title"

    def getTasks(self):
        conn = psycopg2.connect(
            dbname="strength", user="postgres", password="postgres", host="localhost"
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(self.seltaskssql)
        records = cursor.fetchall()
        db = {}
        for row in records:
            db[row["title"]] = dict(title=row["title"], id=row["id"])
        conn.close()
        cursor.close()
        return list(db)

    def getData(self):
        conn = psycopg2.connect(
            dbname="strength", user="postgres", password="postgres", host="localhost"
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(self.selsql)
        records = cursor.fetchall()
        conn.close()
        cursor.close()
        return records

    def setSelsql(self, sql):
        self.selsql = sql

    def setDictFromDb(self):
        conn = psycopg2.connect(
            dbname="strength", user="postgres", password="postgres", host="localhost"
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(self.selsql)
        records = cursor.fetchall()
        # return records
        tmpdict = {}
        for row in records:
            tmpdict[row["title"]] = dict(
                id_task=row["id_task"],
                plan_date=row["plan_date"],
                is_done=row["is_done"],
                title=row["title"],
            )
        conn.close()
        cursor.close()

        return tmpdict

    def setListFromDb(self):
        conn = psycopg2.connect(
            dbname="strength", user="postgres", password="postgres", host="localhost"
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(self.selsql)
        records = cursor.fetchall()
        # return records
        tmpdict = {}
        for row in records:
            tmpdict[row["title"]] = dict(
                id_task=row["id_task"],
                plan_date=row["plan_date"],
                is_done=row["is_done"],
                title=row["title"],
            )
        tmplist = []
        for row in tmpdict:
            pd = tmpdict[row]["plan_date"].strftime("%d.%m.%Y")
            title = tmpdict[row]["plan_date"]
            i_d = tmpdict[row]["is_done"]
            tmplist.append((f"{title}", f"{pd}", f"{i_d}"))
        conn.close()
        cursor.close()
        return tmplist
