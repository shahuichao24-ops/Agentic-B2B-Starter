import sys
import uvicorn
from scripts.reset_db import reset_database

if __name__ == "__main__":
    if "--reset-db" in sys.argv:
        reset_database()
        
    print("=" * 60)
    print("🚀 B2B SaaS Backend starting on http://localhost:8000")
    print("📖 Swagger Docs available at http://localhost:8000/docs")
    print("💡 提示: 执行 python run.py --reset-db 可一键重建最新表结构与种子")
    print("=" * 60)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
