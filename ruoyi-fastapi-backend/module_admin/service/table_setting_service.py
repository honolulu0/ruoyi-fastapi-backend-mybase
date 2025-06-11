from sqlalchemy.ext.asyncio import AsyncSession
from module_admin.dao.table_setting_dao import TableSettingDao
from module_admin.entity.vo.common_vo import CrudResponseModel
import json


class TableSettingService:
    """表格设置服务层"""

    @classmethod
    async def get_setting_services(cls, query_db: AsyncSession, user_id: int, page: str):
        setting = await TableSettingDao.get_setting(query_db, user_id, page)
        if setting and setting.setting:
            try:
                return json.loads(setting.setting)
            except Exception:
                return []
        return []

    @classmethod
    async def save_setting_services(
        cls,
        query_db: AsyncSession,
        user_id: int,
        page: str,
        setting,
        user_name: str,
    ) -> CrudResponseModel:
        setting_str = setting
        if not isinstance(setting, str):
            setting_str = json.dumps(setting, ensure_ascii=False)
        await TableSettingDao.save_setting(query_db, user_id, page, setting_str, user_name)
        return CrudResponseModel(is_success=True, message='保存成功')
