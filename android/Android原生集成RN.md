# 如何在现成项目集成RN

## step one

 1. 添加React-Native依赖

```
compile 'com.facebook.react:react-native:0.20.+'
```
 2. 由于调试RN代码如何从node服务器读取代码，所以要开启Internet访问权限

```
<uses-permission android:name="android.permission.INTERNET" />
```

## step two

### 设置ReactInstanceManager
运行RN之前是需要先实例化ReactInstanceManager,启动RN需要用到ReactInstanceManager,没有设置或设置错误都会导致RN启动失败，甚至crash。

```
reactInstanceManager = ReactInstanceManager.builder()
	.setApplicaiton(getApplicaiton())
	.setBundleAssetName("index.android.bundle")
	.setJSMainModuleName("index.android")
	.addPackage(new MainReactPackage())						//这个可以替换自己的
	.setUseDeveloperSupport(BuildConfig.DEBUG)
	.setInitialLifecycleState(LifecycleState.RESUMED)
	.build();
```
 
### 实例化rootview
 
```
rootView = new ReactRootView(context);
rootView.startReactApplication(reactInstanceManager,"AppName", null);
setContentView(rootView);
```
如果是用自定义的Activity来启动RN，还需要设置一些配置(主要是将native activity上的生命周期时间传递到reactinstantManager,reactInstanceManager适合作为一个单例存在Application中)，具体可以参考facebook官方的ReactActivity

##添加JS代码到应用中

 1. 在你的主工程目录执行以下代码

```
$ npm init
$ npm install --save react-native
$ curl -o .flowconfig https://raw.githubusercontent.com/facebook/react-native/master/.flowconfig
```
 2. 上面的代码会创建一个node模块，然后react-native作为npm依赖添加。现在打开新创建的package.json文件然后在scripts字段下添加如下内容：

```
"start": "node_modules/react-native/packager/packager.sh"
```

 3. 在工程根目录添加index.android.js，粘贴下面代码

```
'use strict'

var React = require('react-native');
var {
	Text,
	View,
	StyleSheet,
} = React;

var AppName = React.createClass({
	render:function() {
		return ({
			<View style={styles.container}>
				<Text style={styles.hello}>Hello,World</Text>	  
			</View>
		});
	}
});

var styles = StyleSheet.create({
	container: {
		flex:1,
		justifyContent: 'center',
	},
	hello: {
		fontSize: 20,
		textAlign: 'center',
		margin: 10,
	}
});
```

## run your app

 1. 运行应用前，先启动开发服务器

```
 npm start
```

 2. 构建并运行你的Android应用，启动RN页面，应用就会从服务器拉取代码并渲染出来

