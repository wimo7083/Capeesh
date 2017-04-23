from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
level_attempt = Table('level_attempt', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('two', Integer),
    Column('three', Integer),
    Column('four', Integer),
    Column('five', Integer),
    Column('six', Integer),
    Column('seven', Integer),
    Column('eight', Integer),
    Column('nine', Integer),
)

words = Table('words', post_meta,
    Column('level', Integer, primary_key=True, nullable=False),
    Column('word', String(length=32)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['level_attempt'].create()
    post_meta.tables['words'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['level_attempt'].drop()
    post_meta.tables['words'].drop()
