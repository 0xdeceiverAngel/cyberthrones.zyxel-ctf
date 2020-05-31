# 榮耀資戰
## review 
這跟之前打的比賽有點不大一樣
比較偏向實務(?
題目分類 有 reverse log分析 數位鑑識 綜合 密碼 封包分析 病毒分析  應該是這些沒記錯

綜合 應該是把 misc web 都包進去了

我要小小抱怨一下 vpn 連過去 答題平台一直當 

這次我們數位見識那些都不太熟 所以恩..

這次我覺的很多題目都是考運氣 有些題目簡單到我懷疑
# comp1
有點智障 給你一排server 

我是先用nmap 掃一下 80 有開

連進去 翻一下html 發現有 個css有flag 就這樣

這題很純粹 運氣 我覺的
## crypto1
暴力解決 或是 跑字典 都沒有成功
## crypto2
先解base64 然後 rot9 救出來了
## log1
要你分析 前3名被打的port

算sha1給它

就寫的統計的python 
## log2
跟前面差不多 只是要統計ip 
## log3
這題我記得是 他說有人偷下載東西 要你從偷下載的東西中找flag 

就看log 我是找找看關鍵字 有download 然後 有看到 url 跟著下去看 http 

只有一個github的可以連上 下載下來 strings 一下 flag 就出來了
## pack1
這題要找漏洞 是CVE-???

CVE-1999-0532

封包看到關鍵字 zonetransfer

去google 就有了
## pack2

## pack3
這題是要找 駭客是用啥名子登入被害人電腦

> strings pack|grep user

就會噴 `net user he11ow0rld9487 /add`

這樣 
## rev1
其實直接r2 下去看 就會看到output func 裡會噴字串

然後對字串做vigenere cipher 就可以
## rev2
有點智障 就瞎猜 1 2 3 其中一個數 它會噴 字串 解base64 就好
## 