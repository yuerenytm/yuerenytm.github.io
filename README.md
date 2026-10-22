# 宅兹浙江

七山二水一分田的历史与人间。这是一个个人长期维护的浙江地方研究档案，不是旅游介绍，也不是技术博客。站点发布在 GitHub Pages：<https://yuerenytm.github.io/>

## 本地预览

需要 Ruby 和 Bundler。在仓库根目录执行：

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 <http://127.0.0.1:4000/>。

不要在仓库里添加 `.nojekyll`。加上之后，GitHub Pages 会跳过 Jekyll，Markdown 和布局都不会再生效。

## 部署

仓库 `yuerenytm/yuerenytm.github.io` 是用户站点，页面在域名根路径。`_config.yml` 里的 `baseurl` 因此留空。

GitHub Pages 使用仓库自带的 Jekyll，不需要本仓库声明插件。建议的设置：

- Source：Deploy from a branch
- Branch：`main`
- Folder：`/ (root)`

推送到 `main` 之后，等 Pages 构建完成再查看线上页面。构建失败时，线上仍会是上一次成功的版本。

## 目录

```text
_config.yml                 站点名称、语言、集合
_data/navigation.yml        导航
_data/media.yml             首页西湖封面与视频开关
_data/reference_types.yml   参考资料的类型
_layouts/                   页面骨架
_includes/                  页眉、页脚、首屏、目录
_regions/                   地区条目（Markdown）
_field_notes/               田野记录（Markdown）
_references/                参考资料（Markdown）
assets/css/main.css         样式
assets/js/hero.js           首页视频的播放与回退
assets/media/west-lake/     首页封面，以及将来的视频
assets/images/              正文图片
about.md                    项目说明
regions/index.md            地区索引
field-notes/index.md        田野记录索引
references/index.md         参考资料索引
```

以底线开头的模板文件只放在仓库里，不会变成网页。

## 增加一篇记录

正文用 Markdown，版式放在布局里。新增条目时不必改公共模板。

地区、田野和文献都使用这些可选字段，方便以后做分类、标签或时间筛选：

- 地区：`title`、`summary`、`status`、`tags`
- 田野：`title`、`date`、`place`、`region`、`tags`、`summary`、`images`
- 文献：`title`、`type`、`year`、`authors`、`source`、`link`、`note`

`type` 只能用 `_data/reference_types.yml` 里已有的 id。

### 地区

把 `_regions/_template.md` 复制为 `_regions/一个稳定的短名.md`。文件名不要以底线开头。删掉 `published: false` 和 `listed: false`，写上真实标题和正文。页面会出现在 `/regions/` 下，并进入地区索引。

地区分类还没有定。不要一次生成全省行政区划。

### 田野记录

复制 `_field_notes/example.md`，改掉文件名，删掉 `example: true`，把日期改成走访日期，把地点和正文换成实录。示例页可以在有了正式记录之后删除。

### 参考资料

复制 `_references/_template.md`，同样去掉文件名里的底线，以及 `published` / `listed`。只著录核对过、并且在档案里使用过的材料。

### 图片

图片集中放在 `assets/images/`，不要嵌进 Markdown 的大段二进制里。建议的文件名：

```text
assets/images/{主题短名}/{yyyy-mm-dd}-{简短说明}.jpg
```

主题短名用稳定的英文或拼音短横线，避免空格。在条目开头这样引用：

```yaml
images:
  - path: /assets/images/west-lake/2026-10-21-mist.jpg
    alt: 替代文本，说明画面里有什么
    caption: 拍摄者，日期，地点，授权
```

没有授权、不能公开的照片不要放上来。

## 首页的西湖画面

首屏是一个全屏背景组件：有视频时缓慢循环，没有视频、视频失败、浏览器禁止自动播放，或系统偏好减少动态时，回到封面照片。窄带或开启省流时也不请求视频。

相关文件：

- 组件：`_includes/hero.html`、`assets/js/hero.js`
- 开关和署名：`_data/media.yml`
- 封面：`assets/media/west-lake/hero-poster.jpg`
- 预留的视频路径：`assets/media/west-lake/hero.mp4`

### 现在用的封面

封面是 Wikimedia Commons 上的摄影原件，未作裁切或调色。

- 作品：Sunrise at Xihu, Westlake
- 作者：Carsten Ullrich
- 许可：CC BY-SA 2.0，<https://creativecommons.org/licenses/by-sa/2.0/>
- 文件页：<https://commons.wikimedia.org/wiki/File:Sunrise_at_Xihu_(Westlake),_Hangzhou_105.jpg>
- 作者主页：<https://www.flickr.com/people/7926008@N08>
- Flickr 原帖：<https://www.flickr.com/photos/ullrich/3079135059/>
- SHA-256：`9ce7ae4df0057664ea48c098a9e767e8b7cfb53cdf965950160b4b1cc4dc18e5`

画面是清晨薄雾中的西湖，有湖面、远山和岸边的树。原图 1600×1200。若以后有同一场景、分辨率更高的授权照片，可以替换这个文件，并在 `_data/media.yml` 里改署名。

首页和仓库说明都保留了作者、许可和来源。这张照片本身仍是 CC BY-SA 2.0，网站的文字并不因此改用同一许可。

### 为什么还没有视频

动态背景的播放、封面和失败回退已经接好，但仓库里故意没有放入视频文件。查过、并且许可清楚的西湖影像，目前都不适合做这一屏：

- Commons《西湖 北山街旁的西湖与荷花》为 CC BY-SA 4.0，只有约 12 秒，画面是游人很多的湖滨步道。循环时人物会跳回原位，也不符合首屏要的安静。
- Commons 上另一条西湖船行影像为 CC BY 3.0，长约 14 分钟。原始文件约 2.9 GB，公开转码只到 480p，体积仍超过 150 MB。这里不能可靠地截出一段稳定、清晰的短片，因此没有收进仓库。

没有用搜索引擎上来历不明的文件，也没有用与西湖无关的画面充数。

### 以后放入视频

1. 把文件放到 `assets/media/west-lake/hero.mp4`。
2. 在 `_data/media.yml` 把 `video_ready` 改为 `true`。
3. 在 `credits` 里另起一项，写明角色（例如「背景影像」）、作者、许可链接、来源，以及是否剪辑、消音或压缩。

建议规格：

- 内容：真实的西湖。清晨或薄雾，湖面、远山、柳树；历史建筑可以入画，但不要游人拥挤的宣传片。
- 拍摄：机位稳定，或只有很慢的移动。时长大约 20 到 40 秒，便于循环，避免硬切和明显的来回跳变。
- 文件：H.264 MP4，yuv420p，可以没有音轨。1280×720 或 1920×1080。尽量小于 8 MB。
- 封面：与视频同一场景的 JPEG。若替换现有封面，宽度最好不少于 1920 像素。
- 许可：必须允许在公开网站播放。署名写进 `credits`。不要把远程地址当作长期资源，也不要把视频做成 Base64 嵌进页面。

`video_ready` 仍为 `false`，或视频加载失败时，首屏继续显示封面。封面也缺失时，背景是深绿色，标题仍可读。

## 以后可以加、现在不做的事

全文检索、按地区或标签筛选，都可以后接。条目的日期、地区、类型和标签已经留在文首，不必为了这些功能先改已发布的正文。当前不引入额外的构建工具。

## 写作约定

没有去过，就不写田野。没有核对，就不写进参考资料。示例页面必须看得出是示例。改正旧文时，在那一页末尾记下日期和改了什么。
