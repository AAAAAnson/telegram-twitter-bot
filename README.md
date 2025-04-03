# Telegram Twitter 视频下载机器人

这是一个简单的 Telegram Bot，用于下载 Twitter 视频并发送回 Telegram 聊天。

## 使用步骤

1. 克隆本项目或下载源码
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 将 `bot.py` 中的 `BOT_TOKEN` 替换为你自己的 BotFather Token
4. 运行：
   ```bash
   python bot.py
   ```

## 功能

- 自动识别用户发送的 Twitter 链接
- 使用 `yt-dlp` 下载最佳质量的视频
- 支持将视频发送回 Telegram 聊天

## 注意事项

- 建议部署在 Linux VPS 上
- 支持使用 `tmux` 或 `screen` 保持后台运行
- 不支持私密推文视频下载

---

Made with ❤️