# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')