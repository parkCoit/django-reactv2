from sqlalchemy import Column, TIMESTAMP as Timestamp, text


class TimestampMixin(object):
    created = Column(Timestamp, nullable=False, server_default=text('current_timestamp'))
    modified = Column(Timestamp, nullable=False, server_default=text('current_timestamp on update current_timestamp'))