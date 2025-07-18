# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Godot 4.3 HTML5 build of "Блоки и точка" (Blocks and Point), ready for deployment on GitHub Pages. The build contains all necessary files for running the game in a web browser.

## Deployment Commands

### GitHub Pages Deployment
```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit the build
git commit -m "Add Godot HTML5 build for GitHub Pages"

# Add GitHub repository as origin (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

# Push to main branch
git push -u origin main

# Or push to gh-pages branch
git checkout -b gh-pages
git push -u origin gh-pages
```

### Local Testing
```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js http-server
npx http-server -p 8000

# Then open http://localhost:8000 in your browser
```

## File Structure

- `index.html` - Main entry point for GitHub Pages (copy of Блоки и точка.html)
- `Блоки и точка.html` - Original Godot HTML export
- `Блоки и точка.js` - Main JavaScript engine file
- `Блоки и точка.pck` - Game data package (403KB)
- `Блоки и точка.wasm` - WebAssembly binary (52MB)
- `Блоки и точка.icon.png` - Game icon
- `Блоки и точка.apple-touch-icon.png` - iOS home screen icon
- `Блоки и точка.png` - Loading splash screen
- `Блоки и точка.audio.*.js` - Audio worklet files
- `.nojekyll` - Prevents Jekyll processing on GitHub Pages

## Important Technical Details

- **Godot Version**: 4.3
- **Threading**: Disabled (GODOT_THREADS_ENABLED = false)
- **Canvas Resize Policy**: 2 (responsive)
- **Cross-Origin Isolation**: Required for proper functionality
- **File Sizes**: 
  - PCK: 403KB
  - WASM: 52MB

## GitHub Pages Configuration

1. Enable GitHub Pages in repository settings
2. Select source branch (main or gh-pages)
3. The game will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/`

## Browser Requirements

The game requires:
- WebAssembly support
- WebGL 2.0 support
- Modern JavaScript features
- Cross-Origin Isolation headers (automatically handled by the game)

## Troubleshooting

If the game fails to load:
1. Check browser console for errors
2. Ensure all files are uploaded correctly
3. Clear browser cache
4. Try a different browser
5. Check that GitHub Pages is enabled and deployed

## Security Notes

- The game uses service workers for cross-origin isolation
- All assets must be served from the same origin
- HTTPS is required for production deployment