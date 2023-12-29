import asyncio
import os
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlmodel import SQLModel

from alembic import context

from src.catalogue.models.database import Product, ProductCategory, ProductDiscount, ProductImage, Category, StockRecord , RecommendedProducts , AdditionalProducts
from src.users.models.database import User, UserAddress
from src.company.models.database import Company

postgres_url = os.getenv('POSTGRES__URL')
config = context.config
if config.config_file_name is not None:
fileConfig(config.config_file_name)
target_metadata = SQLModel.metadata
def include_object(object, name, type_, reflected, compare_to):