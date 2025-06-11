from sqlalchemy.ext.asyncio import AsyncSession
from module_admin.dao.table_setting_dao import TableSettingDao
from module_admin.entity.vo.common_vo import CrudResponseModel


class TableSettingService:
    """表格设置服务层"""

    @classmethod
    async def get_setting_services(cls, query_db: AsyncSession, user_id: int, page: str):
        setting = await TableSettingDao.get_setting(query_db, user_id, page)
        return setting.setting if setting else None

    @classmethod
    async def save_setting_services(
        cls, query_db: AsyncSession, user_id: int, page: str, setting: str, user_name: str
    ) -> CrudResponseModel:
        await TableSettingDao.save_setting(query_db, user_id, page, setting, user_name)
        return CrudResponseModel(is_success=True, message='保存成功')
