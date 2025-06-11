from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from config.database import Base


class SysTableSetting(Base):
    """表格个性化设置表"""

    __tablename__ = 'sys_table_setting'

    setting_id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    user_id = Column(Integer, comment='用户ID')
    page = Column(String(255), comment='页面路径')
    setting = Column(Text, comment='表格设置JSON')
    create_by = Column(String(64), default='', comment='创建者')
    create_time = Column(DateTime, default=datetime.now(), comment='创建时间')
    update_by = Column(String(64), default='', comment='更新者')
    update_time = Column(DateTime, default=datetime.now(), comment='更新时间')
