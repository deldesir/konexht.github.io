#!/bin/bash
set -e

echo "🚀 Building KonexHT Brand Portal (Standard Jekyll Engine)..."

# 1. Container-Style Isolation
unset GEM_HOME
unset GEM_PATH
unset RUBYLIB

export ROOT_DIR=$(pwd)
export GEM_HOME="$ROOT_DIR/_local_gems"
export PATH="$GEM_HOME/bin:$PATH"

# 2. Bootstrap Bundler
if ! command -v bundle &> /dev/null; then
    echo "📦 Bootstrapping Bundler..."
    gem install bundler --no-document
fi

# 3. Configure Bundler
mkdir -p .bundle
cat > .bundle/config <<EOF
---
BUNDLE_PATH: "vendor/bundle"
BUNDLE_DISABLE_SHARED_GEMS: "true"
EOF

# 4. Install Dependencies
echo "📥 Installing standard gems..."
bundle install

# 5. Generate Solution Pages
echo "📄 Generating Solution Pages..."
ruby generate_pages.rb

# 6. Build
echo "🏗️  Jekyll Build..."
bundle exec jekyll build --destination _site --trace

# 6. Update preview symlink
rm -rf /tmp/konexht_preview
ln -s "$(pwd)/_site" /tmp/konexht_preview

echo "✅ Build Complete!"
echo "📂 Site generated in: $(pwd)/_site"
echo "🔗 Symlinked to: /tmp/konexht_preview"
echo "👉 View locally at: http://localhost:8000/factory/"
