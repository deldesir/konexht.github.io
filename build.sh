#!/bin/bash
set -e

echo "🚀 Building KonexHT Brand Portal (High-Fidelity Local Engine)..."

# 1. Prepare assets
mkdir -p _site/assets
if [ -d "assets" ]; then
    cp -r assets/* _site/assets/
fi

# 2. Run Python Generator (Mimics Jekyll Build)
python3 preview_generator.py

# 3. Update preview symlink
rm -rf /tmp/konexht_preview
ln -s $(pwd)/_site /tmp/konexht_preview

echo "✅ Build Complete!"
echo "📂 Site generated in: $(pwd)/_site"
echo "🔗 Symlinked to: /tmp/konexht_preview"
echo "👉 View locally at: http://localhost:8000/konexht_preview/"
