# Java的注解（Annotation）

标签（空格分隔）： java

---

##了解注解
注解Annotation是Java1.5的新特性，现已被广泛应用。使用注解是一种趋势。它可以用于创建文档，跟踪代码中的依赖性，甚至执行基本编译时检查。注解是以‘@注解名’在代码中存在的，根据注解参数的个数，我们可以将注解分为：标记注解、单值注解、完整注解三类。它们都不会直接影响到程序的语义，只是作为注解（标识）存在，我们可以通过反射机制编程实现对这些元数据的访问。另外，你可以在编译时选择代码里的注解是否只存在于源代码级，或者它也能在class文件中出现。

注解一般可分为三类：**Java自带的注解**，**第三方注解**和**自定义的注解**。

##Java自带的注解
在编写Java代码中，我们最常见的几个注解莫过于@Override、@SuppressWarnings和@Deprecated;

 - Override： 从字面上我们就可以看出这个注解想表达的意思，就是告诉别人我要重写这个方法。
 - Deprecated：使用这个注解后，别人在调用添加这个注解的方法后，方法名会显示横线，表示这个方法被弃用或是API作者提供了更好的方法来代替这个方法。**所以大家看到自己调用的方法被划横线的时候最好看看有没更好的方法实现**
 - SuppressWarnings：当我们真的要使用被Deprecated注解的方法时候，同时又不想要烦人的警告时候，可以在调用的方法上添加的这个注解来消除警告。

##如何使用自定义的注解
说了这么多最关心的莫关于如何使用注解。在学会跑之前一定要先学会走，那么我们首先要学会的注解是如何定义的。

Talking is cheap,show me source!(废话少说，放码过来)
###如何定义自定义的注解

```java
//target表示注解的作用范围是在类，成员方法还是成员变量等
@Target({ElementType.TYPE,ElementType.METHOD})
//Retention反应注解的生命周期（运行时，还是只是在代码中）
@Retention(RetentionPolicy.RUNTIME)
//表示是否能够继承（只允许类继承，接口继承的注解无法被使用）
@Inherited  
//是否要生产javadoc
@Documented

//@interface 声明这是一个注解
//PS：如何这个注解没有其他需要包含的类一般使用value
public @interface Description {
    String value() default ""; //default可以定义默认值
}
```

###如何使用注解


注解一般是和Java的另一个特性一起使用的——**反射**。

```java
@Description("I am class person")
public interface Person {

	@Description("I am method")
	String callName();
}

try {
	//1 需求类加载器
	Class c = Class.forName("com.practise.annotation.Person");
	//2 找到类上面的注解
	boolean isExist = c.isAnnotationPresent(Description.class );
	if (isExist) {
		 //3 拿到注解实例
		Description d = (Description)c.getAnnotation(Description.class);
		if (d !=null) {
			System.out.println(d.value());
		}
	}
	//4.1 找到方法上的注解
	Method[] ms = c.getMethods();
	for (Method method : ms) {
		boolean isMExist = method.isAnnotationPresent(Description.class);
		if (isMExist) {
			Description d = (Description)method.getAnnotation(Description.class);
			System.out.println(d.value());
		}
	}
	//4.2 找到方法上的注解
	for(Method m : ms){
		Annotation[] as = m.getAnnotations();
		for(Annotation a : as){
			if(a instanceof Description){
				Description d = (Description)a;
				System.out.println(d.value() );
			}
		}
	}
} catch (ClassNotFoundException e) {
	e.printStackTrace();
}
```

上面代码不过是查找代码中是否存在自定义的注解，并将注解中的值打印出来但这并不是注解的主要作用。

###使用自定义注解的一个例子
虽然我不是做后台开发，但注解的学习是在后台开发的一个学习视频中的学到的，所以使用的注解可以更容易完成sql语句拼接

```java
@Table("user")
public class Filter {
	@Column("id")
	private String id;
	@Column("userName")
	private String userName;
	@Column("nickName")
	private String nickName;
	@Column("age")
	private int age;
	@Column("city")
	private String city;
	@Column("email")
	private String email;
	@Column("phoneNum")
	private String phoneNum;

private static String query(Filter f){
    StringBuilder sb = new StringBuilder();
    Class c = f.getClass();
    boolean isTable = c.isAnnotationPresent(Table.class);
    if (!isTable) {
    	return null;
    }
    //1 获取表名
    String tableName = ((Table)c.getAnnotation(Table.class)).value();
    sb.append("select * from ").append(tableName).append(" where 1 = 1 ");
    //2 先获取到所有的字段
    Field[] fs = c.getDeclaredFields();
    String columnName = null;
    //3 遍历字段
    for(Field field : fs){
    	boolean fExist = field.isAnnotationPresent(Column.class);
    	if(!fExist){
    		continue;
    	}
    	//4 查询符合的字段
    	Column column = field.getAnnotation(Column.class);
    	columnName = column.value();
    	//5 获取字段名
    	String filedName = field.getName();
    	String getMethodName = "get"+filedName.substring(0, 1).toUpperCase()+
    			filedName.substring(1);
    	Object fieldValue = null;
    	try {
    	    //获取字段值
    		Method getMehtod = c.getMethod(getMethodName);
    		fieldValue = getMehtod.invoke(f);
    	} catch (Exception e) {
    		// TODO Auto-generated catch block
    		e.printStackTrace();
    	}
    	//字符串拼装
    	if(fieldValue == null ||
    			(fieldValue instanceof Integer && (Integer)fieldValue == 0)){
    		continue;
    	}
    	sb.append(" and ").append(filedName);
    	if(fieldValue instanceof String){
    		sb.append(" = ").append("'").append(fieldValue).append("'");
    	}else if (fieldValue instanceof Integer){
    		sb.append(" = ").append(fieldValue);
    	}
    }
    return sb.toString();
}
```

自定义的Table和Column注解是一个空注解，与之前的演示的Description类似。
