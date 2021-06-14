# DjangoExchange

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fchayandatta%2FDjangoExchange&count_bg=%2379C83D&title_bg=%23555555&icon=django.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


POST Request to search StackExchange:

```
 curl -X POST --location "http://localhost:8000/api/v1/search/"
    -H "Content-Type: application/x-www-form-urlencoded"
    -d "page=1&pagesize=15&fromdate=&todate=&min=&max=&order=&sort=&q=&accepted=&answers=&body=&closed=&migrated=&notice=&nottagged=&tagged=&title=&user=&url=&views=&wiki="
```
