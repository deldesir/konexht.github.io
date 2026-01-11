#!/bin/bash
# Robust local build script for KonexHT
# Uses isolated _gems directory to avoid system Ruby conflicts

set -e

# 1. Set up TOTALLY isolated environment
export GEM_HOME=$(pwd)/_gems
export GEM_PATH=$GEM_HOME # Stop looking at system gems!
export PATH=$GEM_HOME/bin:$PATH
export JEKYLL_NO_BUNDLER_REQUIRE=true

# 2. Hide Gemfile explicitly (The Nuclear Option against Bundler)
# This prevents Jekyll from auto-loading Bundler even if environment variables fail
if [ -f Gemfile ]; then
    mv Gemfile Gemfile.build_temp
fi

# Ensure Gemfile is restored even if build fails
trap "if [ -f Gemfile.build_temp ]; then mv Gemfile.build_temp Gemfile; fi" EXIT

# 3. Build the site
echo "🚀 Building KonexHT Brand Portal (Isolated Mode)..."
jekyll build --destination _site --trace

# 4. Update preview symlink
rm -rf /tmp/konexht_preview
ln -s $(pwd)/_site /tmp/konexht_preview

echo "✅ Build Complete!"
echo "📂 Site generated in: $(pwd)/_site"
echo "🔗 Symlinked to: /tmp/konexht_preview"
echo "👉 View locally at: http://localhost:8000/konexht_preview/"
