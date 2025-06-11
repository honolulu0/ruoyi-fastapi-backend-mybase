from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from typing import Optional


class TableSettingModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, from_attributes=True)

    setting_id: Optional[int] = Field(default=None, description='主键')
    user_id: Optional[int] = Field(default=None, description='用户ID')
    page: Optional[str] = Field(default=None, description='页面路径')
    setting: Optional[str] = Field(default=None, description='表格设置JSON')
    create_by: Optional[str] = Field(default=None, description='创建者')
    create_time: Optional[datetime] = Field(default=None, description='创建时间')
    update_by: Optional[str] = Field(default=None, description='更新者')
    update_time: Optional[datetime] = Field(default=None, description='更新时间')
