# Handler的那些事

---

我们在学习一门技术和语言之前，要了解技术和语言是什么？不能盲目地去学习一门语言，因为整个技术和语言实现太多了。我们要将我们关注点放在一些比较重要的方面上。

##Handler是什么
Handler是android给我们提供用来更新UI的一套机制，也是一套消息处理的机制，我们可以发送消息，也可以通过它处理消息。

 - 所有的Activity的生命周期回调方法都是通过Handler去发送消息的
 - 大部分的事件传递都是通过Handler来处理

##为什么要用Handler
Android在设计的时候，就已经封装了一套消息创建、传递、处理机制，如果不遵循这样的机制就没有办法更新UI信息的，就会抛出异常信息。

##Handler怎么用
看官方文档是一条捷径

我们创建一个Handler的时候，它会默认和一个MessageQueue绑定。
Handler的用途是定时去发送一个Message或者Runable对象，我们可以在一个线程处理和执行自己定义的Action。
你创建一个程序的时候，会创建一个main线程即UI线程，同时会创建一个Looper，这个Looper会和Handler联系在一起。默认创建在Activity Thread中。
需要是围绕四个方法：

 - sendMessage(Message msg) 
 - sendMessageDelayed(Message msg,long delayMills) 
 - post(Runnable r) 
 - postDelayed(Runnable r,long delayMills)

###常用使用方式
那个四个方法主要分为两大类，发送消息sendMessage和直接post Runnable两种，因此使用使用方式主要有两种类型：

 - 自定义Handler(主要重写了handleMessage方法)和sendMessage配合使用 （一般适用于需要传递参数的情况下）
 - Handler默认方法new出来的对象handler，自定义Runnable对象和post方法配合使用（不能传递参数）
Delayed：意思是消息延迟发送的时间。

###其他使用技巧：
如果细心的小伙伴可能会发现，每一次用handler发送消息都要new一个Message对象。其实还可以利用已创建的Handler对象来获得Message对象，具体：

```
Handler handler = new Handler();
Message msg = handler.obtainMessage();
msg.sendToTarget();
```

obtainMessage是一个重载的方法，还有其他四个方法，分别对应初始化Message的几个public变量 what、arg1、arg2和object。

消息被发送，同样消息是可以被拦截的，在自定义Handler对象的时候，我们可以Handler的构造函数里传入Callback参数，callback形如：
```java
private Handler handler = new Handler(new Handler.Callback() {
        @Override
        public boolean handleMessage(Message msg) {
            Toast.makeText(getApplicationContext(),
            "消息被拦截了",Toast.LENGTH_SHORT).show();
            return true;
        }
    }){
        @Override
        public void handleMessage(Message msg) {
            Toast.makeText(getApplicationContext(),
            "消息没被拦截，我能收到",Toast.LENGTH_SHORT).show();
        }
    };
```
##Handler和Looper、MessageQueue的关系
Android为什么只能通过Handler机制来更新UI?
最根本的目的就是解决多线程并发问题，假设如果有一个Activity当中，有多个线程去更新UI，并且都没有加锁机制，那么会产生什么样子的问题？

> 更新界面错乱

如果对更新UI的操作都进行加锁处理的话又会产生什么问题？

> 性能下降

出于对以上目的问题的考虑，Android给我们提供了一套更新UI的机制，我们所要做的就是遵循这套机制。根本不用去关心多线程问题，所以更新UI的操作，都是在主线程的消息队列当中去轮询处理。

###Handler的原理
 
 1. Handler封装了消息的发送和处理（主要包括消息发送给谁）
 2. Looper内部包含了一个消息队列MessageQueue，所有的Handler发送的消息都走向这个消息队列；Looper有个Looper的死循环方法，不断从MessageQueue取消息，如果有就处理，没有消息就阻塞。
 3. MessageQueue，就是一个消息队列，可以添加消息，并处理消息（被包含在Looper中）
 4. Handler创建的时候会和Looper进行关联，就是在Handler的内部可以找到Looper，就可以找到MessageQueue。在Handler中分送消息，其实就是向MessageQueue队列中发送消息。

总结：Handler负责消息的发送，Looper负责接收Handler发送的消息，并直接把消息回传给Handler。而MessageQueue就是存储消息的一个容器。

##Handler与子线程

###HandlerThread是什么

##Handler如何使用
可能在大家在网上看到许多教程上面介绍如何使用Handler的，都是直接在一个类里面定义Handler实例，然后覆写handleMessage函数，但这个方法会有黄色的警告，说明这个使用方法并不是很妥，但也不是不可以这么做。但是作为一个严重强迫症患者的我是无法忍受这些警告的存在，那么要这么知道如何使用呢？三个字：**看源码！！！**

 

 
  
 


 




