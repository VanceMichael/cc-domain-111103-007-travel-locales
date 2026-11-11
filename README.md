# 多语言景区目录的语言版本采集

这是一个 Python 数据采集项目。当前代码提供来源材料的基础读取入口，合成输入保存在 fixtures，已有读取行为由 tests 验证。

## 来源材料

zh.json、en.json 和 ko.json 分别保存本地捕获的语言呈现；place_id 可以缺失，alternate 是来源明确给出的语言链接，notice 是页面中的服务公告。place-rules.json 保存样例迁址关系。当前入口检查页面基本字段，场馆名称与文字均为虚构。

上面的样例用于说明来源字段和当前读取边界。项目按原始来源保存材料；同一来源的版本变化和不同来源的同名记录需要分别核对。示例文件只用于本地调试，不代表真实企业、机构或设备数据。

## 本地运行

项目使用 Python 3.12 或更新版本，仅依赖标准库。从项目根目录执行：

```sh
python3 -m app.inspect
python3 -m unittest discover -s tests -v
python3 -m compileall -q app tests
```

示例只使用本地虚构资料。处理结果放在 runtime 目录，源文件应保持只读。若连接真实来源，先按来源方授权范围配置读取权限。
