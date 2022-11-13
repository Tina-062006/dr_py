[comment]: <> (#### 🚀dr模板的python实现🚀)
<div align="center">
<h4>🚀第二派-dr模板的python实现🚀</h4>
  <a href="https://alist.nn.ci"><img height="100px" alt="logo" src="https://gitcode.net/qq_32394351/dr_py/-/raw/1fe0e082b1ceacc4469d7f175a605cc2edf0bab0/static/img/icon.png"/></a>
  <p><em>🗂️A webServer convert web and x5 movie sites to cms api data</em></p>
  <a href="https://gitcode.net/qq_32394351/dr_py/-/releases">
    <img src="https://img.shields.io/badge/version-3.9.0-blue" alt="latest version" />
  </a>
  <a href="https://gitcode.net/qq_32394351/dr_py/-/issues">
    <img src="https://img.shields.io/badge/discussions-2-orange" alt="discussions" />
  </a>

  <a href="https://gitcode.net/qq_32394351/dr_py/-/releases">
    <img src="https://img.shields.io/badge/downloads-5329-blue" alt="Downloads" />
  </a>


<a href="https://wwi.lanzoup.com/igPCG0dlqouf">
    <img src="https://img.shields.io/badge/蓝奏云下载-3.9.0-blue" alt="Downloads" />
  </a>



<a href="https://hub.docker.com/repository/docker/hjdhnx/drpy">
    <img src="https://img.shields.io/badge/docker镜像主页-drpy-blue" alt="Downloads" />
  </a>

  <a href="https://gitcode.net/qq_32394351/dr_py/-/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-AGPL3.0-orange" alt="License" />
  </a>

<a href="https://gitcode.net/qq_32394351/dr_py">
    <img src="https://img.shields.io/badge/coverage-99.9%25-yellowgreen" alt="License" />
  </a>
</div>  

##### python3.6-3.8完美运行(3.9以上不支持linux进程启动)
<a href="./安卓本地搭建说明.md" alt="install">
<img src="https://img.shields.io/badge/install support-termux|windows|ubuntu|python3.6~python3.8-yellowgreen" />
</a>

[JS引擎的选择](./python最强js引擎.md)  
[搭建教程](./安卓本地搭建说明.md) | [install_help](https://jason-ray.notion.site/jason-ray/Pluto-TVB-706da08332804a19ab012b4f8385df64)  |[goorm](./道长乱说.md) |[大佬地盘](./大佬友链.md)   
[dr项目QQ官群](https://qm.qq.com/cgi-bin/qm/qr?k=H2KwcXrMdiR5M2blHR5gjZzPfN_S3N_C&jump_from=webapi)  
[参考T4](https://github.com/sec-an/TV_Spider/blob/main/spider/sp360.py)  
[golang最好的js引擎-otto](https://github.com/robertkrimen/otto)   
[dockerfile教程](https://blog.csdn.net/qq_46158060/article/details/125718218)   
[获取本地设备信息](https://blog.csdn.net/cui_yonghua/article/details/125508991)   
[获取本地设备信息](https://m.jb51.net/article/140716.htm)
###### 2022/11/08
- [X] 海盗听书js0空白是触发了网页的cloudfare5秒盾了,暂时无解
- [X] 3.9.20beta7 修复豆瓣
###### 2022/11/04
- [X] 增加了 /lives?path=txt/lives/18fm.txt 和 /lives?path=txt/lives/月光.txt
###### 2022/11/03
- [X] 更换jar,支持海阔二级推送到tvbox
###### 2022/11/02
- [X] 合并小雅代码,未来功能完善解析管理,可正常拖拽排序
###### 2022/10/30
- [X] 3.9.18beta4 修复lives?path=接口漏洞,修复js0设置密码后播放解析没自动带密码Bug
###### 2022/10/28
- [X] 3.9.18beta1 未来功能排序优化,设置中心增加js0防盗用和禁用功能
###### 2022/10/27
- [X] v3.9.18 js1 增加 预处理:, 可以在预处理里写js代码实现操作rule变量和 rule_fetch_params 变量  
比如 rule_fetch_params.headers.Cookie = 'xxxx'; 当然这个cookie是通过js代码获取到的
###### 2022/10/25
- [X] v3.9.17beta1 增加海盗听书源
###### 2022/10/24
- [X] v3.9.17
- [X] drpy(道长) 服务端聚搜支持自动排除未来功能里隐藏的源  
- [X] 未来功能增加源置顶和置底功能 测试性增加排序功能(指定输入数字)
###### 2022/10/23
- [X] 新增几个源 包括虎牙直播
- [X] 设置中心增加仙人模式开关(自动识别不同设备返回不同的drpy接口,关闭的话只会走drpy.min.js)
- [X] 3.9.15beta5 修复后台管理无法进入的bug,规定js源必须包含 var rule字符,不然不识别。中间仅有一个空格
- [X] 3.9.16 增加源属性:图片来源 荐片源图片带上图片来源(目前仅爱佬版tvb可用)
- [X] 优化饭团源,增加其他几个飞机源
###### 2022/10/22
- [X] 新增几个直播源
- [X] 优化没有二级的情况自动带入一级图片和标题 @@分割
- [X] 修复 JRKAN直播 二级智能拼接链接不正常的问题
- [X] 学生录像一级用js重写(urljoin没毛病.网址结构有问题,只能如此了,仅支持js1)
- [X] 完善荐片源的筛选
- [X] 3.9.15beta2 优化jrkan直播二级 学生直播二级 新增 爱车MV
###### 2022/10/21
- [X] 源新增了play_json属性和与之对应的哔哩直播,jrs看直播等源
- [X] 修复俊版无法搜索问题(还需要壳子彻底解决console.log函数问题,无法打印大数据)
- [X] 升级至3.9.14,drpy.js代码中开始记录版本号
- [X] 升级至3.9.14beta2 json优化并增加荐片源
###### 2022/10/20
- [X] 新增了几个源
- [X] 修复乐猪TV源并记录已知问题
- [X] 升级版本至:3.9.12 二级增加新特性 tab_text:'body&&Text',list_text:'body&&Text',list_url:'a&&href'
- [X] drpy.js增加post方法,优化调用逻辑,修复奇优搜索
- [X] 新增gaze源,只完成了推荐和一级
- [X] 3.9.13 修复部分源历史记录异常问题
- [X] 3.9.13beta1 增加了3个新源
###### 2022/10/19
- [X] 源增加 filter_def 属性用于指定不同分类下的默认筛选条件
- [X] 修改搭建文档给出armv7设备的drpy运行兼容方案
- [X] 增加厂长资源,just live等多个源,其中just live这个源用到了新特性 filter_def
- [X] 版本更新至 3.9.11
###### 2022/10/18
- [ ] 没有二级只有一级的情况下想办法把标题和图片带进去二级。(这个想法实现难度太大了,直接放弃,不要瞎搞了)
- [X] 3.9.10 (修复js模式1搜索不到结果,修复js模式0二级选集和线路异常,优化drpy聚搜)
- [X] 源增加属性 模板,可用作模板继承
###### 2022/10/17
- [X] 3.9.8beta2 全局关闭https对应的ssl证书验证
- [X] 3.9.9 增加新特性,简写快看源,修复小品网推荐显示
- [X] 新增 推荐和搜索支持用*替代继承一级对应位置的列表,标题,图片,描述,详情,内容等定位
- [X] drpy豆瓣推荐支持本地js
- [X] 3.9.9beta2 修复指定分类第一页后无法翻页的问题
###### 2022/10/16
- [X] 3.9.8 完成ddys选集播放和免嗅(可惜我刚弄完没播放俩个剧就被封ip了)
- [X] 3.9.8beta1 增加了俩自建js解析
###### 2022/10/15
- [X] beta2 修复dealJson导致的兔小贝一级分类无数据
- [X] beta6 尝试完善低端影视,增加tabs和lists支持js:写法(js模式0和模式1同步测试)
###### 2022/10/14
- [X] todo:推荐支持* 自动集成一级定位
- [X] todo:辅助嗅探
- [X] done:推荐支持* 自动继承一级定位(参考短视频.js)
- [X] done:drpy.js优化,drpy.ym.js完美支持pythonbox及俊版tvb
- [X] 升级版本至3.9.7
- [X] 3.9.7beta1 更新py和js的酷云77搜索
###### 2022/10/13
- [X] 3.9.5修复凌云影视源并增加短视模板
- [X] 增加秋霞影视,ddys等半成品(优化代码兼容取style属性的情况自动提取链接)
- [X] 更新drpy.js,drpy.min.js等本地js运行支持库
- [X] 3.9.6修复drpy的一个严重bug(pdfh死循环)
###### 2022/10/12
- [X] js模式2动态配置链接支持多种壳子
- [X] 增加/lives?path=base/live.txt路由
###### 2022/10/11
- [X] 增加自建解析加密示例
- [X] 发布3.9.0镜像,重大升级，优化js装载速度
- [X] 需要执行命令: pip install quickjs ujson
###### 2022/10/09
- [X] 1.v3.8.2 本地drpy.js抄了一下影魔代码实现了base64加解密和md5加密并且引入全局的CryptoJS对象
- [X] 2.v3.8.3 本地drpy.js抄了一下影魔代码不用import模板改成init加载模板解决换源冲突问题
- [X] 3.v3.8.4 抄了影魔最新的代码并更新版本
###### 2022/10/08
- [X] 1.v3.8.1 本地drpy.js优化优酷兼容,已全部完善
###### 2022/10/07
- [X] 1.v3.8.0 本地drpy.js除优酷不支持外已全部完善
###### 2022/09/27
- [X] 1.v3.7.17 增加真不卡源
###### 2022/09/26
- [X] 1.v3.7.16 芒果增加少儿分类,直播源更新修复
###### 2022/09/25
- [X] 1.v3.7.10 增加了自定义解析功能,解析.conf支持变量{{host}}
- [X] 2.新增了 jiexi/无名.js作为示例,接受vipUrl返回realUrl
- [X] 3.修复腾云驾雾并增加通用筛选
- [X] 4.自建解析增加重定向方法,方便明面上隐藏真实来源的解析地址
- [X] 5.自建js文件自动解析到配置
- [X] 6.增加百忙无果源
###### 2022/09/23
- [X] 1.v3.7.5 优化了首图2模板的搜索定位以及几个相关的源
- [X] 2.二级渲染功能拆分,js单独调用
- [X] 3.v3.7.6 新增优酷源(pluto专用)
- [X] 4.v3.7.7 新增酷云77源(pluto专用),新增猫了个咪源,优化request等方法的post参数传递,增加rc函数
- [X] 5.v3.7.8 增加单一搜索无匹配关键字自动打印源码,注释进入二级详情页的日志打印
- [X] 6.v3.7.9 增加了用户解析合并功能并处理了几个坏的解析(准备跑路,原因是感觉海阔又牛逼了)
###### 2022/09/22
- [X] 1.v3.7.3修复静态文件阿里token没渲染的bug,修复数据库升级bug,优化app.py
- [X] 2.v3.7.4修复自定义drives合并配置报错问题
###### 2022/09/21
- [X] 1.未来功能增加显示和隐藏多选规则的实际逻辑，增加顺序字段等待有缘人
- [X] 2.版本升级至3.7.0
- [X] 3.版本升级至3.7.1,修复/js目录的内置源会被缓存的问题
- [X] 4.修复鸭奈飞,牛马tv内置源
###### 2022/09/19
- [X] 1.增加20多个缓存源,需要在custom.conf文件自定义添加
- [X] 2.修复缓存js播放免嗅问题
###### 2022/09/17
- [X] 1.pluto1.5.1最新beta版支持drpy首页推荐点击跳drpy内部聚搜(原理同T4)
- [X] 2.pluto1.5.1最新beta版支持searchable为2的源忽略参与聚搜,正常单一搜索
- [X] 3.drpy源增加内部聚搜进入二级详情页的简介签名备注真实来源规则名
###### 2022/09/16
- [X] 1.规则headers合并优化
- [X] 2.基础js功能修复,如pdfh,request,Object.keys
- [X] 3.菜狗改为PC_UA
- [X] 4.增加drpy首页源,实现T4相同功能
- [X] 5.增加多源模式,聚搜超时等后台设置中心
- [X] 6.增加豆瓣首页插件以及详情评分功能,可以custom自定义
- [X] 7.增加嗅探配置,可自定义
- [X] 8.版本升级 至3.6.9
- [X] 9.版本升级 至3.7.10,优化drpy搜索必定成功
###### 2022/09/15
- [X] 1.修复生成配置文件中静态文件链接对应的配置文本爬虫地址渲染异常问题
- [X] 2.删除custom里的xb、xp源
- [X] 3.未来功能页面设置为管理员登录后可见
- [X] 4.修复局域网ip可能会获取成网关地址问题
- [X] 5.设置中心增加自定义进程管理地址(可用于goorm等设备绑定快捷方式)
- [X] 6.直播文件目录迁移
- [X] 7.增加py_gitcafe.py和其他几个js首图2模板源
- [X] 8.版本号更新至3.6.6
- [X] 9.增加了start.sh脚本(感谢Antod提供),配置模板增加leshi的flag
###### 2022/09/14
- [X] 1.升级至3.6.2,增加了一些解析
- [X] 2.升级至3.6.5,修复菜狗部分源解析失败问题(url参数有+号被自动变空格导致的)
###### 2022/09/13
- [X] 1.升级至3.5.8
- [X] 2.迁移alist.conf文件,修改默认模板,增加模板url参数支持fyfilter变量从此支持更多筛选场景
- [X] 3.升级至3.5.9,修复重大bug:模板继承导致的自动生成配置的搜索开关异常问题
- [X] 4.增加菜狗热搜
- [X] 5.修复菜狗源纪录片和综艺
###### 2022/09/12
###### 特别说明:仅pluto 1.4.2以上版本支持此项目的筛选及自定义播放免嗅
- [X] 1.升级至3.5.7
- [X] 2.爱奇艺增加了筛选,修复搜索错误,修复json:表达式取不到数据问题
- [X] 3.尝试增加升级过滤txt目录下通过一键生成的配置文件
- [X] 4.主页增加静态配置文件的链接
- [X] 5.生成静态配置文件也会自动合并自定义配置了
- [ ] 6.拖拽排序源(无限延期,有空再说)
- [ ] 7.隐藏显示源(无限延期,有空再说)
###### 2022/09/11
- [X] 1.升级至3.5.2.后台管理增加设置中心 (可能会存在bug)
- [X] 2.升级至3.5.3.增加菜狗源(筛选及解析播放暂未解决)
- [X] 3.升级至3.5.4 (此版本+pluto1.4.1以上版本支持filter,源示例:菜狗.js)
- [X] 4.升级至3.5.5 (菜狗播放返回json)
###### 2022/09/10
- [X] 1.升级至3.4.4.增加小强迷源,增加二级重定向属性(提供重定向后的源码,让代码重新取重定向过后的线路和播放列表)
- [X] 2.升级至3.4.5.增加兔小贝儿歌源,优化json:细节处理以及详情页拼接细节
- [X] 3.升级至3.4.7 后台管理增加了py源开关
- [X] 4.升级至3.4.8 转移数据库到base目录防止被覆盖,增加js源的tab_exclude属性(线路名称过滤)
- [X] 5.v3.4.8 三架构镜像已发布
###### 2022/09/09
- [X] 1.增加西瓜源,修复一级不支持lazy的bug
- [X] 2.兄弟们dockerhub没法push镜像不知道咋回事,3.4.1的镜像自己用docker目录下的文件build吧
- [X] 3.版本升至3.4.2,增加py源支持,放txt/py目录即可,特别鸣谢Pyramid开发者及xiaoya liu提供的技术和源
- [X] 4.版本升至3.4.3,增加了强制升级功能(本地增量覆盖大法)
###### 2022/09/08
- [X] 1.升级到3.2.9,支持自动合并自定义用户配置(内置t4测试源)
- [X] 2.升级到3.3.0,增加奇珍异兽源
- [X] 3.升级到3.3.2,增加自定义本地文件路由: {{ host }}/files/文件名和{{ host }}/txt/文件名 比如 {{ host }}/files/custom_spider.jar
- [X] 4.升级到3.3.4,修改了默认爬虫jar方案,支持轮询和并发json解析,新增用户自定义解析配置
- [ ] 5.待开发搜索支持js写法(后续再考虑首页推荐支持json双模式+js)
- [X] 6.版本升级3.3.5.搜索支持js写法,并修复了360影视搜索问题(搜索定位标题支持||多个分开合并,解决猫壳自动过滤搜索结果问题,比如月升沧海改名了会被猫壳过滤)
###### 2022/09/07
- [X] 1.优化后台管理登录界面,升级更新脚本
- [X] 2.增加了镜像合并脚本(三合一直接拉 hjdhnx/drpy 即可)
- [X] 3.js源增加cate_exlude参数
- [X] 4.增加腾云驾雾源(二级暂未完善,后面再说)
- [X] 5.完善腾云驾雾源,修复直播下载乱码,修复网站强制证书验证
- [X] 6.升级到3.2.8,增加两套模板和多个对应源
###### 2022/09/06
- [X] 1.增加了后台管理界面在线检测升级系统功能
- [X] 2.增加了后台管理界面修改直播源地址和同步直播源
- [X] 3.首页推荐内容不限制数量(新版pluto牛逼!!!)
- [X] 4.增加lsg配置模型和缓存
- [X] 5.增加了默认alist挂载
- [X] 6.升级到3.2.0,进行了全面后端重构用了蓝图写法,app.py文件以后尽量不动
- [X] 7.后台管理界面显示美化-感谢蓝莓果酱
- [X] 8.打包升级后的三平台镜像(v3.2.1)
- [X] 9.首页美化,升级版本号(v3.2.2)
###### 2022/09/05
- [X] 1.内置jar修复了原本tv_box无法播放直播的问题
- [X] 2.重新构建了三种平台的镜像 amd64,armv7,arm64
- [X] 3.优化日志打印wlan信息
###### 2022/09/04
- [X] 1.增加了dockerfile
- [X] 2.基于dockerfile构建的镜像并上传至dockerhub,小白可以一键运行.参考[搭建教程](./安卓本地搭建说明.md)
###### 2022/09/03
- [X] 1.增加了json定位支持(需要升级依赖),写法为 字符串以json:开头,二级的话含is_json:true
- [X] 2.研究正版线路对接解析(摸索出type1与4的区别，但是不知道1怎么走解析)
- [X] 3.调整linux进程配置自动识别(自动去除https)
- [X] 4.搞定360影视和解析播放
- [X] 5.新增二级支持js写法(参考360影视)
###### 2022/09/02
- [X] 1.优化了免嗅探的注入变量,封装了fetch_params变量
- [X] 2.一定程度兼容python3高版本,支持termux直装(高于3.9版本首页推荐无法获取)
- [X] 3.准备弃坑,基本完结撒花
- [X] 4.增加自定义配置直播外网地址
###### 2022/09/01
- [X] 1.增加动态分类排除配置
- [X] 2.优化pdfh,pdfa,pd等函数,支持多个&&写法,自动取第一个
- [X] 3.增加vfed规则模板
###### 2022/08/31
- [X] 1.增加管理员登录功能
- [X] 2.增加管理员上传和删除内置规则功能
- [X] 3.增加上传文件校验(仅支持pydr的js规则并且100kb以内)
###### 2022/08/30
- [X] 1.增加动态局域网ip获取
- [X] 2.增加js规则热加载(增删改不用重启)
- [X] 3.增加视界的加密库
- [X] 4.增加蓝莓影视免嗅探
- [X] 5.增加免嗅耗时毫秒数统计
- [X] 6.增加自动装载配置
- [X] 7.增加js里单独设置某个源是否可搜索
- [X] 8.增加外网免嗅(自定义config.py里面改)
- [X] 9.增加错误处理和首页单个详情获取
- [X] 10.增加本地直播地址自定义
- [X] 11.增加数据库迁移,[新版教程](https://www.cjavapy.com/article/1977/)  [旧版教程](https://www.cnblogs.com/LoveMoney-MrLi/articles/15765985.html)
- [X] 12.自动ocr识别过搜索验证码
###### 2022/08/29
- [X] 1.更换js引擎,速度更快性能更好
- [X] 2.新版js支持与python互动,后期可能支持js免嗅(lazy:'js:xxx')
- [X] 3.支持了js免嗅和常用的fetch,post方法
- [X] 4.配置uglifyjs可以把js代码压缩到一行(es5不支持多行js)
###### 2022/08/28
- [X] 1.增加linux进程启动,命令 supervisord -c manager.conf
- [X] 2.转移文本文件到txt目录
- [X] 3.增加服务器解析播放(全局配置和js分别配置.后期可以针对性运行解析)
- [X] 4.增加自定义免嗅(基于道长任务仓库核心逻辑实现云函数)
- [X] 5.增加模板继承,优化免嗅参数二
###### 2022/08/27
- [X] 1.增加PC_UA变量
- [X] 2.首页增加更多功能按钮  
- [X] 3.增加猫配置自动生成，分别有本地配置，局域网配置，在线配置
- [X] 4.修复默认网站的favicon图标问题
- [X] 5.增加 flask-sqlalchemy 用于驱动sqlite3数据库
- [X] 6.引入sqlite3数据进行缓存分类定位到的标签
- [ ] 7.增加filter一键爬取和入库(filter_name,filter_url,filter_parse)
- [X] 8.使用gevent作为服务,提升大量性能
###### 2022/08/26
- [X] 1.支持首页推荐功能,模板属性增加limit参数  
- [X] 2.支持纯一级的功能(比如车车网没二级)  
- [X] 3.解决配置首页报错和嗅探播放报错问题
- [X] 4.支持分类第一页独立链接,直接在链接后面加[第一页的独立链接]
- [X] 5.增加headers参数,可以传ua和cookie，此方法解决555影视搜索问题
- [X] 6.增加homeUrl和host参数,以及class_parse参数,可以动态定位分类标签
- [X] 7.获取二级详情函数增加了线程池的使用
- [ ] 8.模板自定义filter过滤
- [X] 9.网页端显示缓存的规则以及提供点击清除缓存操作
- [X] 10.增加本地配置文件，增加指定编码。
- [X] 11.待开发模板渲染器,一键生成猫配置文件。
######  特性说明
1. 参考了海阔视界dr模板设计思路
2. 参考tv_box的t4项目思路重新设计了cms接口

######  本地搭建
1. 安装zero termux
2. 在termux里安装tome 虚拟机
3. tome 虚拟机 里安装ubuntu1804容器
4. ubuntu1804容器里安装python3-pip,nodejs
5. pip3换源并安装requirements.txt(pip3 install -r requirements.txt)
6. python3 app.py运行项目(也可以其他方式nohup或者 supervisord -c manager.conf)
7. 访问地址加/index查看dr_py主页

#### 测试地址
[sqlite3使用教程](https://m.yisu.com/zixun/375448.html)  
[远程网站](http://cms.nokia.press/index)  
[本地网站](http://192.168.10.99:5705/index)  
[gevent下载地址](https://pypi.org/project/gevent/#files)
[aarch64的cp310](http://pan.nokia.press/d/hiker/whl/gevent-21.12.0-cp310-cp310-linux_aarch64.whl)

[comment]: <> ([需要安装nodejs]&#40;https://registry.npmmirror.com/binary.html?path=node/latest-v14.x/&#41;)
[本地服务配置地址](http://localhost:5705/config/0)  
[远程服务配置地址](http://cms.nokia.press/config/2)  

### 配置相关
直接复制对应的三种地址就行了，不需要生成本地文件(下面教程不要了)  
~~本地地址  clan://localhost/pycms_local.json  
推荐把文件放到  /storage/emulated/0/PlutoPlayer/pycms_local.json  
并且pluto要自己切换路径为PlutoPlayer~~

### 相关教程
[pyquery定位](https://blog.csdn.net/Arise007/article/details/79513094)

### 模板规则说明
所有相关属性说明
```javascript
var rule = {
    title:'',//规则标题,没有实际作用,但是可以作为cms类名称依据
    编码:'',//不填就默认utf-8
    host:'',//网页的域名根,包含http头如 https://www,baidu.com
    homeUrl:'/latest/',//网站的首页链接,可以是完整路径或者相对路径,用于分类获取和推荐获取 fyclass是分类标签 fypage是页数
    url:'/fyclass/fypage.html[/fyclass/]',//网站的分类页面链接
    detailUrl:'https://yanetflix.com/voddetail/fyid.html',//非必填,二级详情拼接链接,感觉没啥卵用
    searchUrl:'',//搜索链接 可以是完整路径或者相对路径,用于分类获取和推荐获取 **代表搜索词 fypage代表页数
    searchable:0,//是否启用全局搜索,
    quickSearch:0,//是否启用快速搜索,
    filterable:0,//是否启用筛选,
    filter:{},// 筛选条件字典
    // 默认筛选条件字典(不同分类可以指定同样筛选参数的不同默认值)
    filter_def:{
        douyu:{
        area:'一起看',
        other:'..'
        },
        huya:{
        area:'影音馆',
        other:'..'
        }
    }, 
    // 筛选网站传参,会自动传到分类链接下(本示例中的url参数)-url里参数为fyfilter,可参考蓝莓影视.js
    filter_url:'style={{fl.style}}&zone={{fl.zone}}&year={{fl.year}}&fee={{fl.fee}}&order={{fl.order}}',
    // 注意,由于猫有配置缓存,搜索配置没法热加载，修改了js不需要重启服务器
    // 但是需要tv_box进设置里换源使配置重新装载
    headers:{//网站的请求头,完整支持所有的,常带ua和cookies
        'User-Agent':'MOBILE_UA',
        "Cookie": "searchneed=ok"
    },
    timeout:5000,//网站的全局请求超时,默认是3000毫秒
    class_name:'电影&电视剧&动漫&综艺',//静态分类名称拼接
    class_url:'1&2&3&4',//静态分类标识拼接
    //动态分类获取 列表;标题;链接;正则提取 不需要正则的时候后面别加分号
    class_parse:'#side-menu:lt(1) li;a&&Text;a&&href;com/(.*?)/',
    // 除开全局过滤之外还需要过滤哪些标题不视为分类
    cate_exclude:'',
    // 除开全局动态线路名过滤之外还需要过滤哪些线路名标题不视为线路
    tab_exclude:'',
    // 服务器解析播放
    play_parse:true,
    // play_json　传数组或者　类　true/false 比如 0,1 如果不传会内部默认处理 不传和传0可能效果不同
    // 效果等同说明: play_json:[{re:'*', json:{jx:0, parse:1}}], 等同于 play_json:0,
    play_json:[{
        re:'*',
        json:{
            jx:1,
            parse:1,
        },
    }],
    // 自定义免嗅
    lazy:'',
    // 首页推荐显示数量
    limit:6,
    double:true,//是否双层列表定位,默认false
    // 对图片加了referer验证的有效,海阔专用,普通规则请勿填写此键值
    图片来源:'@Referer=http://www.jianpianapp.com@User-Agent=jianpian-version350',
    
    // js写法，仅js模式1有效.可以用于代码动态获取全局cookie之类的
    // 可操作变量有 rule_fetch_params,rule,以及基础的网页访问request,post等操作
    预处理:'rule_fetch_params.headers.Cookie = "xxxx";',
    // 类似海阔一级 列表;标题;图片;描述;链接;详情 其中最后一个参数选填
    // 如果是双层定位的话,推荐的第2段分号代码也是第2层定位列表代码
    推荐:'.col-sm-6;h3&&Text;img&&data-src;.date&&Text;a&&href',
    // 类似海阔一级 列表;标题;图片;描述;链接;详情 其中最后一个参数选填
    一级:'.col-sm-6;h3&&Text;img&&data-src;.date&&Text;a&&href',
    // 二级可以是*,表示规则无二级,直接拿一级的链接进行嗅探
    // 二级 title: 片名;类型
    // 二级 desc: 主要信息;年代;地区;演员;导演
    // 或者 {title:'',img:'',desc:'',content:'',tabs:'',lists:'',tab_text:'body&&Text',list_text:'body&&Text',list_url:'a&&href'} 同海阔dr二级
    二级:'*',
    // 搜索可以是*,集成一级，或者跟一级一样的写法 列表;标题;图片;描述;链接;详情
    搜索:'*',
}
```
模板继承写法
```javascript
var rule = Object.assign(muban.mxpro,{
title:'鸭奈飞',
host:'https://yanetflix.com',
url:'/index.php/vod/show/id/fyclass/page/fypage.html',
class_parse:'.navbar-items li:gt(1):lt(6);a&&Text;a&&href;.*/(.*?).html',
});
```
模板继承写法(新)
```javascript
var rule = {
title:'cokemv',
模板:'mxpro',
host:'https://cokemv.me',
class_parse:'.navbar-items li:gt(1):lt(7);a&&Text;a&&href;/(\\d+).html',
}
```
js:内置变量
input,html,VODS,VOD,TABS,LISTS