#!/bin/bash
# ==============================================================================
# Agentic B2B SaaS Instant Project Generator
# Usage: ./create-saas-project.sh <target_project_path>
# Example: ./create-saas-project.sh ~/projects/my-new-saas
# ==============================================================================

set -e

if [ -z "$1" ]; then
  echo "❌ Error: Please specify the target path for the new project!"
  echo "Usage: $0 <new_project_path>"
  echo "Example: $0 ~/projects/my-new-saas"
  exit 1
fi

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$1"

if [ -d "$TARGET_DIR" ]; then
  echo "⚠️ Warning: Target directory already exists: $TARGET_DIR"
  read -p "Do you want to overwrite / merge files? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operation cancelled."
    exit 1
  fi
fi

mkdir -p "$TARGET_DIR"
echo "📦 Copying frontend and backend architectures from master starter..."

# 1. Copy Frontend (exclude heavy node_modules and build artifacts)
mkdir -p "$TARGET_DIR/frontend"
rsync -av --exclude="node_modules" --exclude="dist" --exclude=".git" "$SOURCE_DIR/frontend/" "$TARGET_DIR/frontend/" > /dev/null

# 2. Copy Backend (exclude virtualenvs, caches, and db binaries)
mkdir -p "$TARGET_DIR/backend"
rsync -av --exclude=".venv" --exclude="__pycache__" --exclude="app.db" --exclude=".git" "$SOURCE_DIR/backend/" "$TARGET_DIR/backend/" > /dev/null

# 3. Copy Specifications, Rules, Licenses, and Docs
cp "$SOURCE_DIR/README.md" "$TARGET_DIR/" 2>/dev/null || true
cp "$SOURCE_DIR/README.zh-CN.md" "$TARGET_DIR/" 2>/dev/null || true
cp "$SOURCE_DIR/AGENTS.md" "$TARGET_DIR/" 2>/dev/null || true
cp "$SOURCE_DIR/AGENTS.zh-CN.md" "$TARGET_DIR/" 2>/dev/null || true
cp "$SOURCE_DIR/AGENTS.md" "$TARGET_DIR/.cursorrules" 2>/dev/null || true
cp "$SOURCE_DIR/.gitignore" "$TARGET_DIR/" 2>/dev/null || true
cp "$SOURCE_DIR/LICENSE" "$TARGET_DIR/" 2>/dev/null || true
cp -r "$SOURCE_DIR/docs" "$TARGET_DIR/" 2>/dev/null || true

echo "✅ New project created successfully at: $TARGET_DIR"
echo "--------------------------------------------------"
echo "🚀 Getting Started:"
echo "1. Start Backend API:"
echo "   cd \"$TARGET_DIR/backend\""
echo "   uv venv && uv pip install -e ."
echo "   python run.py  # Open http://localhost:8000/docs"
echo ""
echo "2. Start Frontend Dashboard:"
echo "   cd \"$TARGET_DIR/frontend\""
echo "   pnpm install"
echo "   pnpm dev      # Open http://localhost:5173"
echo "--------------------------------------------------"
