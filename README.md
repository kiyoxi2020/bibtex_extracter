# python批量从google scholar导入bibtex

## 1. 安装selenium

- 运行以下命令即可

```cpp
>> pip install selenium
```

## 2. 安装chrome driver

- 参考：[https://blog.csdn.net/weixin_43746433/article/details/95237254?spm=1001.2014.3001.5506](https://blog.csdn.net/weixin_43746433/article/details/95237254?spm=1001.2014.3001.5506)
1. chrome浏览器中输入”chrome://version/“，查看chrome版本
2. **[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)** 选择合适版本下载
3. 将下载后的驱动解压到某个目录，比如”D:\chromedriver.exe”

## 3. 编写代码并运行
```
>> python main.py
```
## 4. 注意事项

- google scholar会弹出人机身份认证，需要在代码中添加断点，人工处理，然后就可以继续运行，基本认证一次之后，后续的文献能够自动查询
