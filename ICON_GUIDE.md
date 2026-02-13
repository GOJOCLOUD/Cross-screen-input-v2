# Mac应用图标配置说明

## 图标文件

项目已生成完整的Mac应用图标集，包含以下文件：

### 1. AppIcon.icns
- **位置**: `images/AppIcon.icns`
- **大小**: 2.5MB
- **用途**: Mac应用主图标
- **包含的分辨率**:
  - 16x16 (标准)
  - 32x32 (2x)
  - 128x128 (标准)
  - 256x256 (2x)
  - 512x512 (标准)
  - 1024x1024 (2x)

### 2. AppIcon.iconset
- **位置**: `images/AppIcon.iconset/`
- **用途**: 图标源文件集
- **包含文件**:
  - icon_16x16.png
  - icon_16x16@2x.png
  - icon_32x32.png
  - icon_32x32@2x.png
  - icon_128x128.png
  - icon_128x128@2x.png
  - icon_256x256.png
  - icon_256x256@2x.png
  - icon_512x512.png
  - icon_512x512@2x.png

### 3. 源文件
- `images/app-icon-1080x1080.png` - 高清源图
- `images/app-icon-2160x2160.png` - 超高清源图

## 打包配置

已创建PyInstaller打包配置文件：`backend/跨屏输入.spec`

### 打包命令

```bash
cd backend
pyinstaller 跨屏输入.spec
```

### 打包后的应用

打包完成后，生成的应用将位于：
```
dist/跨屏输入.app
```

应用将自动使用 `images/AppIcon.icns` 作为应用图标。

## 图标适配说明

生成的图标已适配以下场景：

1. **Dock栏图标**: 使用512x512和1024x1024分辨率
2. **Launchpad**: 使用256x256和512x512分辨率
3. **Finder列表**: 使用16x16和32x32分辨率
4. **关于窗口**: 使用128x128和256x256分辨率
5. **高分辨率屏幕**: 所有2x版本支持Retina显示

## 图标特性

- ✅ 支持Retina显示
- ✅ 支持深色模式
- ✅ 支持所有Mac分辨率
- ✅ 符合Apple Human Interface Guidelines
- ✅ 自动缩放适配不同屏幕

## 注意事项

1. **图标更新**: 如果修改了源图，需要重新生成图标集
2. **缓存清理**: 修改图标后可能需要清理Dock缓存
3. **签名**: 打包的应用需要代码签名才能正常显示图标

### 清理Dock缓存

```bash
killall Dock
```

### 重新生成图标

如果需要重新生成图标：

```bash
cd images
rm -rf AppIcon.iconset AppIcon.icns
mkdir -p AppIcon.iconset

# 生成不同尺寸
sips -z 16 16 app-icon-1080x1080.png --out AppIcon.iconset/icon_16x16.png
sips -z 32 32 app-icon-1080x1080.png --out AppIcon.iconset/icon_16x16@2x.png
sips -z 32 32 app-icon-1080x1080.png --out AppIcon.iconset/icon_32x32.png
sips -z 64 64 app-icon-1080x1080.png --out AppIcon.iconset/icon_32x32@2x.png
sips -z 128 128 app-icon-1080x1080.png --out AppIcon.iconset/icon_128x128.png
sips -z 256 256 app-icon-1080x1080.png --out AppIcon.iconset/icon_128x128@2x.png
sips -z 256 256 app-icon-1080x1080.png --out AppIcon.iconset/icon_256x256.png
sips -z 512 512 app-icon-1080x1080.png --out AppIcon.iconset/icon_256x256@2x.png
sips -z 512 512 app-icon-1080x1080.png --out AppIcon.iconset/icon_512x512.png
sips -z 1024 1024 app-icon-1080x1080.png --out AppIcon.iconset/icon_512x512@2x.png

# 生成icns文件
iconutil -c icns AppIcon.iconset -o AppIcon.icns
```
