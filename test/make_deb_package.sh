#!/bin/bash

# 创建必要的目录结构
mkdir -p package/DEBIAN
mkdir -p package/usr/local/bin

# 创建控制文件
cat <<EOF > package/DEBIAN/control
Package: mypackage
Version: 1.0-1
Section: base
Priority: optional
Architecture: all
Depends: bash
Maintainer: Your Name <your.email@example.com>
Description: A simple package
 A longer description of the package.
EOF

# 创建一个示例文件
echo "echo Hello, World!" > package/usr/local/bin/helloworld
chmod +x package/usr/local/bin/helloworld

# 构建 DEB 文件
dpkg-deb --build package

# 将 DEB 文件移动到输出目录
mv package.deb /workdir/mypackage.deb