from django.test.runner import DiscoverRunner

from mongoengine.connection import get_connection, get_db


class MongoUnittestTestRunner(DiscoverRunner):
    def setup_databases(self, **kwangs):
        db_alias = 'test'
        db_name = get_db(db_alias).name

        self.conn = get_connection(db_alias)
        print("Creating mongo '{0}' database for alias '{1}'...".format(db_name, db_alias))

        return db_alias

    def teardown_databases(self, db_alias, **kwargs):
        db_name = get_db(db_alias).name
        self.conn.drop_database(db_name)
        print("\n\nDestroying mongo '{0}' database for alias '{1}'...".format(db_name, db_alias))



