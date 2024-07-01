#   html转excel脚本使用说明
### 写在前面:此工具目前只能用作html中有固定格式的标签转化，不具有固定格式的html可能传化失败
-   首先用记事本打开配置文件config.json 注:使用utf-8编码保存打开
-   修改配置文件
-   配置文件长这样:
```json
[
    {
        "colName":"url",
        "lable":"img",
        "className":"",
        "prop":"src"
    },
    {
        "colName":"name",
        "lable":"span",
        "className":"el-tooltip value",
        "prop":"string"
    }
]
```
-   配置注释：
-   colName:转换后该行的列名
-   lable:html标签名，将html的这个标签中的数据转换到excel中
-   className:类名，没有就留空，如果有很多混淆的标签，可以用html的类名来筛选
-   prop:要转化的属性，将该标签的这个属性转化到excel中
-   可以根据个人需求自由添加或筛检配置文件的列配置
-   配置好后，将需要转化的html元素复制到根目录下/input/文件夹的txt文件里，脚本会自动将多个txt文件转化为多个同名xlsx文件
-   最后执行，查看转化结果