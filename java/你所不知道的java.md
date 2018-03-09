# 你所不知道的Java

标签（空格分隔）： java

---

##字符串处理
 - valueof(X xx)
Returns the string representation of the X argument.
 -

##运算符
**~ X 异或运算符：** 这个运算符是单元运算符，它的功能是X加1且符号位取反 比如~1 = -2、~-1 = 0；
提示：**X必须是整型数据**
**X << Y 左移运算符：** 这个运算符是二元运算符，它的功能是X左移Y位 [移动的位数是基于X的二进制 任何形式的变量或常量在底层都是二进制储存 补0]
**X >> Y 右移运算符：**
这个运算符是二元运算符，它的功能是X右移Y位 （对于左边移出的空位，如果是正数空位补0,若为负数，坑补0也可能补1，取决于所用的计算机系统。）

##反射的基本使用

```java
Class<?>clazz = Class.forName("android.app.Activity",false,mContext.getClassLoader());
Class[] paramsType = {Bundle.class};
Method onCreate = clazz.getDeclaredMethod("onCreate", paramsType);
onCreate.setAccessible(true);
Activity activity = null;
Bundle bundle = null;
Object obj = onCreate.invoke(activity,bundle);
```

##Java原子操作类
根据修改的数据类型，可以将JUC包中的原子操作类可以分为4类。

1. 基本类型: AtomicInteger, AtomicLong, AtomicBoolean ;
2. 数组类型: AtomicIntegerArray, AtomicLongArray, AtomicReferenceArray ;
3. 引用类型: AtomicReference, AtomicStampedRerence, AtomicMarkableReference ;
4. 对象的属性修改类型: AtomicIntegerFieldUpdater, AtomicLongFieldUpdater, AtomicReferenceFieldUpdater 。

**这些类存在的目的是对相应的数据进行原子操作。所谓原子操作，是指操作过程不会被中断，保证数据操作是以原子方式进行的。**
