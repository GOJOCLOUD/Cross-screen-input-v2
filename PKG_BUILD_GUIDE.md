# 跨屏输入 - Mac PKG打包指南

## 📦 PKG安装包说明

本项目使用 **PKG** 格式进行Mac应用分发，相比DMG有以下优势：
- ✅ 自动配置系统权限
- ✅ 自动安装到Applications目录
- ✅ 支持安装前/后脚本
- ✅ 更好的用户体验
- ✅ 支持卸载功能

## 🚀 本地打包

### 前置要求

```bash
# 安装PyInstaller
pip install pyinstaller

# 确保已安装所有依赖
cd backend
pip install -r requirements.txt
```

### 打包步骤

```bash
# 1. 使用PyInstaller构建应用
cd backend
pyinstaller 跨屏输入.spec --clean --noconfirm

# 2. 创建PKG安装包
cd ..
mkdir -p build-root
cp -R backend/dist/跨屏输入.app build-root/

pkgbuild \
  --install-location /Applications \
  --component build-root/跨屏输入.app \
  --scripts pkg/scripts \
  --identifier com.gojocloud.crossscreeninput \
  --version 1.0.0 \
  build/PKG.pkg

productbuild \
  --distribution pkg/distribution.xml \
  --package-path build \
  --resources pkg/resources \
  跨屏输入-1.0.0.pkg
```

### 打包产物

- `跨屏输入-1.0.0.pkg` - 最终安装包

## 📁 PKG结构

```
pkg/
├── distribution.xml          # 安装程序配置
├── scripts/                 # 安装脚本
│   ├── preinstall          # 安装前脚本
│   ├── postinstall         # 安装后脚本
│   └── uninstall          # 卸载脚本
└── resources/              # 安装资源
    ├── welcome.html        # 欢迎页面
    ├── conclusion.html     # 完成页面
    ├── license.txt        # 许可协议
    └── icon.png          # 图标
```

## 🔐 权限配置

PKG安装包会自动配置以下权限：

### 1. 辅助功能权限
- **用途**: 键盘和鼠标控制
- **配置**: 自动添加到TCC数据库
- **手动**: 系统设置 > 隐私与安全性 > 辅助功能

### 2. 完全磁盘访问权限
- **用途**: 剪贴板操作
- **配置**: 自动添加到TCC数据库
- **手动**: 系统设置 > 隐私与安全性 > 完全磁盘访问

### 3. 网络访问权限
- **用途**: 跨屏通信
- **配置**: 自动授予本地网络访问

## 📋 安装脚本说明

### preinstall
- 检查并关闭正在运行的实例
- 备份旧版本

### postinstall
- 配置系统权限
- 设置自动启动
- 打开系统设置引导用户

### uninstall
- 停止应用
- 移除自动启动
- 删除应用文件
- 询问是否删除用户数据

## 🌐 GitHub Actions自动打包

项目已配置GitHub Actions工作流，推送代码后自动构建PKG：

```bash
# 推送代码触发自动构建
git add .
git commit -m "update"
git push origin main
```

构建完成后，PKG文件会作为artifact上传，可在Actions页面下载。

## 📦 分发

### GitHub Release
1. 创建新标签：`git tag v1.0.0`
2. 推送标签：`git push origin v1.0.0`
3. GitHub Actions自动创建Release并上传PKG

### 手动分发
- 将PKG文件上传到任何文件分享服务
- 用户双击PKG文件即可安装

## ⚙️ 自定义配置

### 修改应用名称
编辑以下文件中的名称：
- `backend/跨屏输入.spec`
- `pkg/distribution.xml`
- `pkg/scripts/postinstall`
- `pkg/scripts/uninstall`

### 修改版本号
统一修改以下位置：
- `pkg/distribution.xml`: `<key>CFBundleVersion</key>`
- `pkg/scripts/postinstall`: `--version 1.0.0`
- 打包命令中的版本号

### 修改图标
替换以下文件：
- `images/AppIcon.icns`
- `pkg/resources/icon.png`

## 🔍 故障排除

### PKG无法打开
```bash
# 检查签名
codesign -dv 跨屏输入-1.0.0.pkg

# 重新签名
codesign --force --sign - 跨屏输入-1.0.0.pkg
```

### 权限未授予
1. 打开系统设置 > 隐私与安全性
2. 手动找到"跨屏输入"并授权
3. 重启应用

### 安装失败
1. 检查磁盘空间
2. 查看安装日志：`/var/log/install.log`
3. 尝试使用sudo安装

## 📝 开发建议

1. **测试安装**：每次修改后先在虚拟机测试
2. **版本管理**：使用语义化版本号（major.minor.patch）
3. **签名**：发布前使用开发者证书签名
4. **公证**：macOS需要公证才能在未签名系统运行

## 📞 技术支持

如有问题，请访问：https://github.com/GOJOCLOUD/Cross-screen-input-v2/issues
