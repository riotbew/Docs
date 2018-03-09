# 解决引用android-support-v7-appcompat库文件出错的问题

标签（空格分隔）： 转载

---

今天要项目想实现一个ListViewAnimation的功能，网上有个开源的解决方案
https://github.com/nhaarman/ListViewAnimations

这github上的开源项目是最新的代码，本文所用到的是之前的版本的ListViewAnimations
资源地址：http://download.csdn.net/detail/fancylovejava/8493843，可以去免费下载
这个项目解压后然后导入到eclipse中去，需要添加v7-appcompat的库文件，因为有些style的theme属性需要引用到v7的属性，并且一些menu的showAsAction="ifRoom"是在v7中才有的属性

Ok，导入到eclipse中的项目有Library-ListViewAnimations和AnimationActivity两个项目，这个v7的项目是我eclipse之前就有倒入过的，并且android sdk是5.0的，因为更新了最新版本的sdk，导致在v7里的res里面有values-v21的资源文件和一些其它5.0的资源文件。android5.0虽然在国内还没流行，但未来应该迟早会流行起来，具体我也不知道。

反正有了android 5.0的sdk就可以开发适合android 5.0版本的手机app了。
导入的项目中有错误，没办法一步一步修复一下项目……
将Library-ListViewAnimations的v7库文件删除掉，然后refresh下
将ListViewAnimations的demo项目add下v7库文件，然后refrsh下，错误消失

但是，(好像，具体忘记了，反正多看console控制台的提示错误，然后解决)，记得提示了个错误
appcompat_v7\res\values-v21\themes_base.xml:191: 但是项目确没明显错误
然后，run，但是发现还是报错误，说v7找不到什么资源啊
之前导入库文件其实有个需要注意的地方，就是如果项目文件是4.4的，库文件不能超过4.4版本的，但是现在问题来了，v7是5.0的，项目确实4.4的，所以即使添加了库文件，但是仍然会报错。
所以把项目文件的sdk也改成5.0的，然后refresh下，运行，OK
文字描述比较多，但是还算言简意赅了
下次再遇到类似的问题就有了很好的解决方案了，手上一大堆事情，抽空上班写，(fuck)呵(you)呵!!



http://jingyan.baidu.com/article/bea41d439bd6d5b4c41be659.html
Android项目使用support v7时遇到的各种问题
当我们开发android应用需要用到android-support-v7-appcompat.jar这个库时（比方说要在2.2版本上使用actionbar和fragment），在项目中导入v4和v7这两个库之后，新手往往会遇到一些问题。在这里，总结一下可能遇到的问题，以及解决的方法。
工具/原料
需要两个库：android-support-v4.jar，android-support-v7-appcompat.jar
温馨提示：这两个库最好版本一样，否则可能会有一些其他问题产生。
这两个库可以从sdk下的sdk\extras\android\support中获取

##方法/步骤

 - 首先是在项目中导入这两个库

可以通过在项目根目录创建一个libs文件，然后把这两个库拷贝到里面，然后eclipse刷新一下这个项目，eclipse会智能添加这两个库
添加完之后，可能遇到的问题：
一类问题：  values\......No resource found
比方说：
res\values\styles.xml:4: error: Error retrieving parent for item: No resource found that matches the given name 'Theme.AppCompat.Light.DarkActionBar'.
对于values这个地方产生的no resource found问题，说明是没有v7下的资源。

 - 解决方法：

添加资源库，针对上面的例子，AppCompat这个是v7里的，所以缺少的是v7的资源。从sdk去获取，路径是sdk\extras\android\support\v7\appcompat，把这个library通过eclipse导入(import)。然后之前的项目添加该lib，再clean下。这样上面的问题可以搞定。
二类问题：values-v11，values-v21，values-v17等等下的No resource found

比方说：
appcompat\res\values-v21\styles_base.xml:75: error: Error retrieving parent for item: No resource found that matches the given name 'android:Widget.Material.ActionButton'.
appcompat\res\values-v11\themes_base.xml:178: error: Error: No resource found that matches the given name: attr 'android:windowActionBar'.
appcompat\res\values-v14\themes_base.xml:27: error: Error: No resource found that matches the given name: attr 'android:actionModePasteDrawable'.

对于在values-v11这类针对不同android target加载的values下找不到资源的问题，原因还是一样，找不到这个target下的资源。

解决方法：
很简单，把project.properties里的target=android-8或者可能稍微高点，改到target=android-21或者更高（前提是sdk已经下载了该target的库），然后再clean下项目。这样这类问题也就解决了，当然你在Manifest里不要忘记加上uses-sdk，来允许最低版本。
最后附上测试写的actionbar tab加上fragment，在Android2.3.4三星手机上的实现结果
注意事项
android-support-v4.jar，android-support-v7-appcompat.jar这两个库版本最好一样
