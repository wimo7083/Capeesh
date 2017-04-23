from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
level_mistake = Table('level_mistake', post_meta,
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['level_mistake'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['level_mistake'].drop()
