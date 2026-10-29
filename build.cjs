const fs = require('fs');
const path = require('path');

const dist = path.join(__dirname, 'dist');
if (!fs.existsSync(dist)) {
  fs.mkdirSync(dist, { recursive: true });
}

// 1. Copy index.html to dist
fs.copyFileSync(path.join(__dirname, 'index.html'), path.join(dist, 'index.html'));
console.log('✓ Copied index.html to dist');

// 2. Copy assets directory recursively to dist/assets
function copyDir(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

const assetsSrc = path.join(__dirname, 'assets');
const assetsDest = path.join(dist, 'assets');
if (fs.existsSync(assetsSrc)) {
  copyDir(assetsSrc, assetsDest);
  console.log('✓ Copied assets to dist/assets');
}

// 3. Copy README.md if present
if (fs.existsSync(path.join(__dirname, 'README.md'))) {
  fs.copyFileSync(path.join(__dirname, 'README.md'), path.join(dist, 'README.md'));
}

console.log('Build completed successfully: dist folder prepared for deployment.');
