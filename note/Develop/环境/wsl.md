## 命令行补全
### 安装zsh与git

```bash
sudo apt install zsh git -y
```
### 安装 oh my zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 安装自动提示与语法高亮插件

```bash
# 自动提示插件
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 语法高亮插件
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 启用插件
1.   打开 `.zshrc` 文件
```bash
vim ~/.zshrc   
```
2. 找到插件配置位置，添加以下配置
```text
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```
3. 保存配置，并让配置生效
```bash
source ~/.zshrc
```

### 字体
为了防止出现乱码，可以去[Nerd Fonts](https://www.nerdfonts.com/font-downloads)下载字体
1. 下载对应字体
2. 解压后右键`.ttf`文件安装
3. 在 Terminal 中应用打开 Windows Terminal 的“设置” -> “配置文件” -> 选择你的 Ubuntu -> “外观” -> “字体”，将字体face改为 下载的字体

### 问题
#### 安装了oh my zsh后发现之前安装的部分命令不可用，出现了“zsh: command not found: claude”命令没找的的错误
**解决方法**：在`~/.zshrc` 文件的末尾将 `~/.bashrc`中配置的环境变量重新加上去，还需要将`/home/Zeng/.local/bin` 目录加入到环境变量中