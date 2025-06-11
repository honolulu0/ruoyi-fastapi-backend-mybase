from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from module_admin.entity.do.table_setting_do import SysTableSetting


class TableSettingDao:
    """表格设置DAO"""

    @classmethod
    async def get_setting(cls, db: AsyncSession, user_id: int, page: str):
        query = select(SysTableSetting).where(
            SysTableSetting.user_id == user_id,
            SysTableSetting.page == page,
        )
        return (await db.execute(query)).scalars().first()

    @classmethod
    async def save_setting(cls, db: AsyncSession, user_id: int, page: str, setting: str, user_name: str):
        obj = await cls.get_setting(db, user_id, page)
        if obj:
            obj.setting = setting
            obj.update_by = user_name
            obj.update_time = datetime.now()
        else:
            obj = SysTableSetting(
                user_id=user_id,
                page=page,
                setting=setting,
                create_by=user_name,
                create_time=datetime.now(),
                update_by=user_name,
                update_time=datetime.now(),
            )
            db.add(obj)
        await db.commit()
