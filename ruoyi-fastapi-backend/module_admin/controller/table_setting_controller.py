from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from config.get_db import get_db
from module_admin.entity.vo.user_vo import CurrentUserModel
from module_admin.service.login_service import LoginService
from module_admin.service.table_setting_service import TableSettingService
from utils.response_util import ResponseUtil


tableSettingController = APIRouter(prefix='/system/table-setting', dependencies=[Depends(LoginService.get_current_user)])


@tableSettingController.get('/{page}')
async def get_table_setting(
    request: Request,
    page: str,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    setting = await TableSettingService.get_setting_services(query_db, current_user.user.user_id, page)
    return ResponseUtil.success(data=setting)


@tableSettingController.post('')
async def save_table_setting(
    request: Request,
    data: dict,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    page = data.get('page')
    setting = data.get('setting')
    result = await TableSettingService.save_setting_services(
        query_db,
        current_user.user.user_id,
        page,
        setting,
        current_user.user.user_name,
    )
    return ResponseUtil.success(msg=result.message)
