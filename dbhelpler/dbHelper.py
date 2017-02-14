import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbhelpler.models import Notice, BaseModel

DB_NAME = os.path.join(os.path.split(os.path.realpath(__file__))[0], "zhengce.db3 ")


@contextmanager
def session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class dbHelper(object):
    def __init__(self):
        engine = create_engine('sqlite:///' + DB_NAME, echo=True)

        print('sqlite:///' + DB_NAME)

        BaseModel.metadata.create_all(engine)

        self.Session = sessionmaker(bind=engine)

    def save(self, item):

        if (self.isCrawled(item['href'])):
            n = Notice(title=item["title"],
                       url=item['href'],
                       source=item['source'],
                       publisher=item['publisher'],
                       published_time=item['publish_date'],
                       content=item['content']
                       )

            with session_scope(self.Session) as session:
                session.add(n)
        else:
            print("该网址已存在")

    def isCrawled(self, url):
        session = self.Session()
        query = session.query(Notice).filter(Notice.url == url).count()
        print(query)
        return query < 1

    def allUrls(self):
        session = self.Session()
        urls = session.query(Notice.url).all()
        return urls

    def lately_notice(self, day, source=None):
        session = self.Session()
        if source is None:
            query = session.execute('''select title,url,source,published_time from notices
                                where julianday('now')-julianday(published_time)<%d
                                order BY  published_time desc''' % (int(day))).fetchall()
        else:
            query = session.execute('''select title,url,source,published_time from notices
                                where julianday('now')-julianday(published_time)<%d
                                and source='%s' order BY  published_time desc''' % (int(day), source)).fetchall()

        items = []
        for row in query:
            items.append({"title": row[0],
                          "url": row[1],
                          "source": row[2],
                          "published_date": row[3]})

        return items
