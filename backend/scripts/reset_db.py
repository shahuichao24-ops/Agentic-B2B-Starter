import os
import sys

# 将项目根目录加入模块搜索路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.core.database import init_db

def reset_database():
    print("🔄 开始重置数据库结构与种子数据...")
    if settings.DATABASE_URL.startswith("sqlite"):
        db_path = settings.DATABASE_URL.replace("sqlite:///", "").replace("./", "")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, db_path)
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"🗑️ 已安全清理旧数据库文件: {full_path}")
    
    # 重新建表与灌入干净种子
    init_db()
    print("✅ 数据库表结构已依据最新模型全量重建，种子数据灌入完成！")

if __name__ == "__main__":
    reset_database()
