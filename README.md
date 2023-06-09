# autoproxy
  此脚本主要通过 GitHub actions 定时 自动拉取[gfwlist](https://github.com/gfwlist/gfwlist)并加入 `personal_rules.txt`  最后合并成 `autoproxy.txt` 并`push`代码和自动发布`release`
## autoproxy.txt
可供 `SwitchyOmega` 情景模式更新，避免因为情景模式过大导致`Chrome/Edge` 下无法自动同步插件情景模式数据



# 基本规则
## 正则表达式
例如就是常规的正则表达式，前后各加一撇。正则表达式规则的前面会有一个感叹号注明。
```
/regexp.com/
```

不过，扩展内部常数级时间复杂度的算法无法支持正则表达式。出于效率考虑，一般不用正则式。宁愿多写几条普通的规则。

## 普通的规则，通配符 ＊
就是把需要代理的网址写进去。比如：
```
youtube.com
```
可以在需要的地方加通配符，但是首尾的地方不需要，因为首尾的通配符是默认的。也就是说，youtube.com 跟 ＊youtube.com＊ 是一个意思。

## 仅仅是 IP 被墙
如果某网站仅仅是 IP 被墙而不是关键词, 可以用 || 来限定, 例如
```
||tumblr.com
```

# http/https 协议指定
如果希望将规则限定在某种协议, 如 http/https 下则可以使用 |http:// |https:// 的规则, 例如

```
|http://friendfeed.com 
|https://spreadsheets.google.com
```
## 禁止代理
如果希望在某个网站禁止代理, 将 @@ 加在最前即可, 例如

```
@@|https://autoproxy.org   
@@||www.douban.com  
```
## 其他
autoproxy其实规则核心是adp 1.1，规则写法同adp一样的，可以到adp官网学习，
[撰写 Adblock Plus 过滤规则](https://adblockplus.org/zh_CN/filters)



# 参考
[sunshineplan/autoproxy](https://github.com/sunshineplan/autoproxy)
[AutoProxy代理规则简单写法](http://mydf.github.io/blog/autoproxy/)
[gfwlist/gfwlist](https://github.com/gfwlist/gfwlist)
