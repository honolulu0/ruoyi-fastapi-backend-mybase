from config.database import async_engine, AsyncSessionLocal, Base
from utils.log_util import logger
from sqlalchemy import text
from config.env import DataBaseConfig


async def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接

    :return:
    """
    async with AsyncSessionLocal() as current_db:
        yield current_db


async def init_create_table():
    """
    应用启动时初始化数据库连接

    :return:
    """
    logger.info('初始化数据库连接...')
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        async def add_column_if_not_exists(table: str, column: str, column_def: str):
            """在表中添加缺失字段"""
            if DataBaseConfig.db_type == 'postgresql':
                await conn.execute(
                    text(
                        f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {column} {column_def}"
                    )
                )
            else:
                result = await conn.execute(
                    text(
                        "SELECT COUNT(*) FROM information_schema.columns "
                        "WHERE table_schema=:schema AND table_name=:table AND column_name=:column"
                    ),
                    {
                        "schema": DataBaseConfig.db_database,
                        "table": table,
                        "column": column,
                    },
                )
                if result.scalar() == 0:
                    await conn.execute(
                        text(
                            f"ALTER TABLE {table} ADD COLUMN {column} {column_def}"
                        )
                    )

        await add_column_if_not_exists(
            "gen_table_column", "relation_table", "varchar(200) default ''"
        )
        await add_column_if_not_exists(
            "gen_table_column", "relation_column", "varchar(200) default ''"
        )
        await add_column_if_not_exists(
            "gen_table_column", "relation_type", "varchar(50) default ''"
        )
        await add_column_if_not_exists(
            "gen_table_column", "table_name", "varchar(200) default ''"
        )
        await add_column_if_not_exists(
            "gen_table_column", "column_alias", "varchar(200) default ''"
        )
    logger.info('数据库连接成功')
